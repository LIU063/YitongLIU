import dgl
import torch
import numpy as np
import cmath
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from dgl.data import DGLDataset
import os
import torch.nn as nn
import dgl.nn as dglnn
import torch.nn.functional as F
from dgl import save_graphs, load_graphs
from dgl.data.utils import makedirs, save_info, load_info
from torch.nn import Sequential as Seq, Linear as Lin, ReLU, ELU, Sigmoid, BatchNorm1d as BN, ReLU6 as ReLU6
import pandas as pd
import random


def generate_channel_graph(n_ap, n_ue_per_ap, n_antenna, radius=0.2, alpha=2, seed=0):
    np.random.seed(seed)
    src = torch.cat([torch.tensor([i] * n_ue_per_ap) for i in range(n_ap)])
    dst = torch.arange(n_ap * n_ue_per_ap)
    # 创建AP到其他AP下设备的边
    src_interferes = torch.cat([torch.tensor([i] * n_ue_per_ap * (n_ap - 1)) for i in range(n_ap)])
    dst_interferes = torch.cat([torch.cat([torch.cat([torch.arange(j * n_ue_per_ap, (j + 1) * n_ue_per_ap) for j in range(n_ap) if j != i])]) for i in range(n_ap)])
    # print(src)
    g_data = {('ap', 'd_link', 'ue'): (src, dst), ('ue', 'u_link', 'ap'): (dst, src), ('ap', 'interferes', 'ue'): (src_interferes, dst_interferes)}
    g = dgl.heterograph(g_data)

    # 给ap节点分配属性
    ap_positions = torch.randn(g.num_nodes('ap'), 2)  #位置属性
    g.nodes['ap'].data['pos'] = torch.randn(g.num_nodes('ap'), 2)
    power_vector = torch.complex(torch.randn(g.num_nodes('ap'), n_ue_per_ap, n_antenna), torch.randn(g.num_nodes('ap'), n_ue_per_ap, n_antenna))  #下属所有设备的波束属性
    g.nodes['ap'].data['power_vector'] = power_vector

    # 给ue节点分配属性
    ue_positions = torch.zeros(n_ap * n_ue_per_ap, 2)
    for i in range(n_ap):
        for j in range(n_ue_per_ap):
            theta = 2 * np.pi * np.random.rand()  # 随机角度
            r = radius * np.sqrt(np.random.rand())  # 随机距离（这样生成的点会均匀地分布在圆内）
            dx, dy = r * np.cos(theta), r * np.sin(theta)
            ue_positions[i * n_ue_per_ap + j, :] = ap_positions[i, :] + torch.tensor([dx, dy])
    g.nodes['ue'].data['pos'] = ue_positions  #位置属性

    # 给d_link边分配属性
    # 计算AP到设备边的路径损失
    path_losses_connect = torch.complex(torch.zeros((len(src), n_antenna), dtype=torch.float), torch.zeros((len(src), n_antenna), dtype=torch.float))
    for i in range(len(src)):
        ap_pos = ap_positions[src[i]]
        device_pos = ue_positions[dst[i]]
        dist = torch.sqrt(torch.sum((ap_pos - device_pos)**2))  # 计算距离
        path_loss_vector = []
        for j in range(n_antenna):
            path_loss = 1 / cmath.sqrt(2) * (np.random.randn() + 1j * np.random.randn()) / (dist**alpha)
            # path_loss = torch.tensor(1 / cmath.sqrt(2) * (np.random.randn() + 1j * np.random.randn()))
            # path_loss = abs(path_loss)
            path_loss_vector.append(path_loss)
        stacked_tensor = torch.stack(path_loss_vector)
        path_losses_connect[i] = stacked_tensor
    g.edges['d_link'].data['path_loss'] = path_losses_connect

    # 给interferes边分配属性
    # 计算AP到其他AP下设备边的路径损失
    path_losses_interferes = torch.complex(torch.zeros((len(src_interferes), n_antenna), dtype=torch.float), torch.zeros((len(src_interferes), n_antenna), dtype=torch.float))
    for i in range(len(src_interferes)):
        ap_pos = ap_positions[src_interferes[i]]
        device_pos = ue_positions[dst_interferes[i]]
        dist = torch.sqrt(torch.sum((ap_pos - device_pos)**2))  # 计算距离
        path_loss_vector = []
        for j in range(n_antenna):
            path_loss = 1 / cmath.sqrt(2) * (np.random.randn() + 1j * np.random.randn()) / (dist**alpha)
            # path_loss = torch.tensor(1 / cmath.sqrt(2) * (np.random.randn() + 1j * np.random.randn()))
            # path_loss = abs(path_loss)
            path_loss_vector.append(path_loss)
        stacked_tensor = torch.stack(path_loss_vector)
        path_losses_interferes[i] = stacked_tensor
    g.edges['interferes'].data['path_loss'] = path_losses_interferes
    g.edges['interferes'].data['interference_product'] = torch.zeros((len(src_interferes), 1), dtype=torch.float)
    # print(g.nodes['ap'])
    # print(g)
    # print(g.ntypes)
    # print(g.etypes)
    # print(g.canonical_etypes)  # 查看关系类型三元组
    # print(src)
    return g


class WiFi_Dataset(DGLDataset):
    def __init__(self, n_graphs, n_ap, n_ue_per_ap, seed_list, data_name, n_antenna=2, radius=0.2, alpha=2):
        self.n_graphs = n_graphs
        self.n_ap = n_ap
        self.n_ue_per_ap = n_ue_per_ap
        self.n_antenna = n_antenna
        self.radius = radius
        self.alpha = alpha
        self.path = '.\\'
        self.seed_list = seed_list

        super().__init__(name=data_name)

    def build_graph(self, seed):
        graph = generate_channel_graph(self.n_ap, self.n_ue_per_ap, self.n_antenna, self.radius, self.alpha, seed)
        return graph

    def process(self):
        # 将原始数据处理为图、标签和数据集划分的掩码
        self.graph_list = []
        for i in range(self.n_graphs):
            graph = self.build_graph(self.seed_list[i])
            self.graph_list.append(graph)

    def __getitem__(self, idx):
        # 通过idx得到与之对应的一个样本
        return self.graph_list[idx]

    def __len__(self):
        # 数据样本的数量
        return self.n_graphs

    def save(self):
        # 保存图和标签

        graph_path = os.path.join(self.path, self.name, 'WiFi_dgl_graph_Loss_ap{}_per_ue{}_n_antenna{}_n{}.bin'.format(self.n_ap, self.n_ue_per_ap, self.n_antenna, self.n_graphs))
        save_graphs(graph_path, self.graph_list)
        # # 在Python字典里保存其他信息
        # info_path = os.path.join(self.save_path, '_info.pkl')
        # save_info(info_path, {'num_classes': self.num_classes})

    def load(self):
        # 从目录 `self.save_path` 里读取处理过的数据
        graph_path = os.path.join(self.path, self.name, 'WiFi_dgl_graph_Loss_ap{}_per_ue{}_n_antenna{}_n{}.bin'.format(self.n_ap, self.n_ue_per_ap, self.n_antenna, self.n_graphs))
        self.graph_list = load_graphs(graph_path)
        # self.labels = label_dict['labels']
        # info_path = os.path.join(self.save_path, self.mode + '_info.pkl')
        # self.num_classes = load_info(info_path)['num_classes']


    # def has_cache(self):
    #     # 检查在 `self.save_path` 里是否有处理过的数据文件
    #     graph_path = os.path.join(self.save_path, self.mode + '_dgl_graph.bin')
    #     info_path = os.path.join(self.save_path, self.mode + '_info.pkl')
    #     return os.path.exists(graph_path) and os.path.exists(info_path)
def collate(samples):
    '''DGL collate function for graph-only data'''
    graphs = samples
    batched_graph = dgl.batch(graphs)
    return batched_graph


def MLP(channels, batch_norm=True):
    return Seq(*[Seq(Lin(channels[i - 1], channels[i]), ReLU6(), BN(channels[i])) for i in range(1, len(channels))])


class EarlyStopping:
    def __init__(self, patience=7, verbose=False, delta=0):
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = float('inf')
        self.delta = delta

    def __call__(self, val_loss, model):

        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        if self.verbose:
            print(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        torch.save(model.state_dict(), './MU-MIMO_Train{}_Loss_ap{}_per_ue{}_n_antenna{}_Train_n{}_Test_n{}.pt'.format(training_epochs, n_ap, n_ue_per_ap, n_antenna, train_n_g, test_n_g))  # 这里会将最优模型参数保存为 checkpoint.pt 文件
        self.val_loss_min = val_loss


class CustomConv(nn.Module):
    def __init__(self, mlp1, mlp2, mlp3, num_antenna):
        super(CustomConv, self).__init__()
        self.mlp1 = mlp1
        self.mlp2 = mlp2
        self.mlp3 = mlp3
        self.num_antenna = num_antenna

    def aggregate_interferes(self, g):

        # 消息函数
        def interferes_message(edges):
            # output_old = []
            # for i in range(len(edges)):
            #     infer_vector1 = torch.bmm(edges.src['power_vector'][i].conj().unsqueeze(0), edges.data['path_loss'][i].view(1, -1, 1))
            #     sum_ap_infer1 = torch.sum(torch.norm(infer_vector1, dim=-1)**2)
            #     output_old.append(sum_ap_infer1)

            infer_vector = torch.sum(edges.src['power_vector'].conj(), dim=1) * edges.data['path_loss']
            sum_ap_infer = torch.norm(infer_vector, dim=-1)**2
            edges.data['interference_product'] = sum_ap_infer.view(-1, 1)
            # output_new = sum_ap_infer.view(-1, 1)
            # 检查两者的输出是否相同
            # print(torch.allclose(torch.tensor(output_old), output_new, atol=1e-6))

            return {'m': edges.data['interference_product']}

        # reduce函数
        def interferes_reduce(nodes):
            # 对所有消息求和
            # max_infer = torch.max(nodes.mailbox['m'], dim=1).values
            sum_infer = nodes.mailbox['m'].sum(dim=1)
            return {'ue_all_interference': sum_infer}

        interferes_subg = g['ap', 'interferes', 'ue']
        # print(g.nodes['ue'])
        interferes_subg.update_all(interferes_message, interferes_reduce)
        # print(g.nodes['ue'])
        # 将结果拷贝回原始图的目标节点
        # g.nodes['ue'].data['ue_all_interference'] = interferes_subg.nodes['ue'].data['ue_all_interference']

    def mlp_aggregate_interferes(self, g):
        # 消息函数
        def mlp_interferes_message(edges):

            interferes_features = torch.cat([edges.data['path_loss'], torch.sum(edges.src['power_vector'], dim=1)], dim=1)
            cat_interferes_features = torch.cat([torch.real(interferes_features), torch.imag(interferes_features)], dim=1)
            ue_power_vector = self.mlp2(cat_interferes_features)

            edges.data['mlp_interference_product'] = ue_power_vector
            return {'m': edges.data['mlp_interference_product']}

        # reduce函数
        def mlp_interferes_reduce(nodes):
            # 对所有消息求和
            # max_infer = torch.max(nodes.mailbox['m'], dim=1).values
            mlp_sum_infer = nodes.mailbox['m'].sum(dim=1)
            return {'mlp_ue_all_interference': mlp_sum_infer}

        interferes_subg = g['ap', 'interferes', 'ue']

        interferes_subg.update_all(mlp_interferes_message, mlp_interferes_reduce)

    def update_ue_power_vector(self, g):
        def apply_dlink(edges):

            src_idx, dst_idx, edges_idx = edges.edges()
            ue_p_ap = edges.src['power_vector'].size()[1]
            # in_infer_list = torch.ones(len(edges), 1).to(device)
            # for i in dst_idx:
            #     iner_infer = torch.matmul(edges.src['power_vector'][i].conj(), edges.data['path_loss'][i].view(-1, 1))
            #     norm_iner_infer = torch.norm(iner_infer, dim=-1).view(1, -1)**2
            #     mask = torch.ones_like(norm_iner_infer)
            #     mask[:, i % ue_p_ap] = 0  # 不希望自己这条dlink参与求和
            #     in_infer_list[i] = torch.sum(norm_iner_infer * mask)

            iner_infer1 = torch.bmm(edges.src['power_vector'].conj(), edges.data['path_loss'].unsqueeze(-1))
            norm_iner_infer1 = torch.norm(iner_infer1, dim=-1)**2

            mask1 = torch.ones(len(edges), ue_p_ap).to(device)
            mask1[torch.arange(len(edges)), dst_idx % ue_p_ap] = 0

            in_infer_list1 = torch.sum(norm_iner_infer1 * mask1, dim=1).view(-1, 1)

            return {'inner_infer': in_infer_list1}

        # 消息函数
        def dlink_message(edges):
            # edges.src['power_vector']
            # edges.data['path_loss']
            # edges.dst['ue_all_interference']
            # power_vector_real = torch.real(edges.src['power_vector'].view(len(edges), -1))
            # power_vector_imag = torch.imag(edges.src['power_vector'].view(len(edges), -1))
            path_loss_real = torch.real(edges.data['path_loss'])
            path_loss_imag = torch.imag(edges.data['path_loss'])
            inner_infer = edges.data['inner_infer']
            ue_all_interference = edges.dst['mlp_ue_all_interference']

            UE_all_h_features = torch.cat([
                inner_infer,
                path_loss_real,
                path_loss_imag,
                ue_all_interference,
            ], dim=1)
            ue_power_vector = self.mlp1(UE_all_h_features)
            output_reshaped = ue_power_vector.view(len(edges), 2, -1)
            # 从reshape后的tensor中获取实部和虚部
            real_part = output_reshaped[:, 0, :]
            imag_part = output_reshaped[:, 1, :]

            # 使用torch.complex将实部和虚部组合成复数Tensor
            complex_tensor = torch.complex(real_part, imag_part)
            return {'power_vector': complex_tensor}

        # reduce函数
        def dlink_reduce(nodes):
            # 对所有消息求和
            # max_infer = torch.max(nodes.mailbox['m'], dim=1).values
            # sum_infer = nodes.mailbox['m']
            return {'ue_power_vector': nodes.mailbox['power_vector'].squeeze(1)}

        dlink_subg = g['ap', 'd_link', 'ue']

        dlink_subg.apply_edges(apply_dlink)
        dlink_subg.update_all(dlink_message, dlink_reduce)
        # print(g.nodes['ue'])
        # # # 将结果拷贝回原始图的目标节点
        # g.nodes['ue'].data['ue_all_interference'] = interferes_subg.nodes['ue'].data['ue_all_interference']

    def update_ap_power_vector(self, g):
        def ulink_message(edges):
            ue_power_vector = edges.src['ue_power_vector']
            return {'m': ue_power_vector}

        # reduce函数
        def ulink_reduce(nodes):
            # 对所有消息求和
            # nodes.mailbox['m']
            old_size = nodes.mailbox['m'].size()
            input_tensor = nodes.mailbox['m'].view(old_size[0], -1)
            # 计算每个元素的模
            magnitudes = torch.abs(input_tensor)

            # 对每一行进行归一化
            row_sums = magnitudes.sum(dim=-1, keepdim=True)
            normalized_tensor = input_tensor / row_sums
            normalized_tensor = normalized_tensor.view(old_size)
            return {'power_vector': normalized_tensor}

        ulink_subg = g['ue', 'u_link', 'ap']
        # g.ndata['ue_power_vector']
        ulink_subg.update_all(ulink_message, ulink_reduce)

    def get_output(self, g):
        # 选择边('ap', 'd_link', 'device')
        # srctype, etype, dsttype = g.canonical_etypes[0]
        output_power = g.ndata['power_vector']['ap']
        return output_power

    def forward(self, g):
        self.aggregate_interferes(g)
        self.mlp_aggregate_interferes(g)
        # print(g.edges['interferes'].data['interference_product'])
        # print(g.nodes['ue'].data['ue_all_interference'])
        self.update_ue_power_vector(g)
        self.update_ap_power_vector(g)
        self.aggregate_interferes(g)
        # print(g.edges['interferes'].data['interference_product'])
        # print(g.nodes['ue'].data['ue_all_interference'])
        output = self.get_output(g)
        return g, output


class WFHGCN(nn.Module):
    def __init__(self, num_antenna):
        super(WFHGCN, self).__init__()
        self.num_antenna = num_antenna
        # self.mlp1 = MLP(input_dim=5 * num_antenna, hidden_dim=256, output_dim=1 * num_antenna).to(device)
        # self.mlp2 = MLP(input_dim=5 * num_antenna, hidden_dim=256, output_dim=1 * num_antenna).to(device).to(device)

        # self.mlp3 = MLP(input_dim=5 * num_antenna, hidden_dim=256, output_dim=1 * num_antenna).to(device).to(device)

        self.mlp1 = MLP([3 * num_antenna + 1, 64, 2 * num_antenna])
        self.mlp2 = MLP([2 * 2 * num_antenna, 64, 1 * num_antenna])
        # self.mlp2 = Seq(*[self.mlp2, ReLU()])
        # self.mlp3 = MLP([5 * num_antenna, 256, 1 * num_antenna])
        self.mlp3 = None
        self.conv = CustomConv(self.mlp1, self.mlp2, self.mlp3, self.num_antenna).to(device)

    def forward(self, g):
        x1, _ = self.conv(g)
        # x2, _ = self.conv(x1)
        _, output_power = self.conv(x1)

        return output_power


# 信道增益为虚数时
def rate_loss(g, output_power):
    B = 60

    # 计算噪声功率
    N = N0 * B
    # interference_product = g.edges['interferes'].data['interference_product']
    interference_product = g.nodes['ue'].data['ue_all_interference']
    src, dst = g.edges(etype='d_link')
    rate_list = []
    for i in range(0, n_ap * n_ue_per_ap):
        src_power_vector = output_power[src[i]]
        path_loss = g.edges['d_link'].data['path_loss'][i]

        # iner_infer = src_power_vector.conj() * path_loss

        # norm_iner_infer = torch.norm(iner_infer, dim=-1)**2
        norm_iner_infer = torch.abs(torch.matmul(src_power_vector.conj(), path_loss))**2
        norm_iner_infer = norm_iner_infer.view(1, -1)
        mask = torch.ones_like(norm_iner_infer)
        mask[:, i % n_ue_per_ap] = 0  # 不希望自己这条dlink参与求和
        in_infer_list = torch.sum(norm_iner_infer * mask)
        rx_power = torch.sum(norm_iner_infer * (1 - mask))
        all_infer = in_infer_list + interference_product[i] + N
        i_SNR = torch.div(rx_power, all_infer)
        i_rate = B * torch.log(1 + i_SNR)
        rate_list.append(i_rate)
    # print(in_infer_list, rx_power)
    sum_rate = torch.stack(rate_list)
    loss = -torch.sum(sum_rate)
    min_loss = -torch.min(sum_rate)
    return loss, min_loss


# 传统wifi用MIMO时,计算MIMO的预编码矩阵
# def compute_mimo_rate(B, H, num_users, num_antennas, noise_power):
#     """
#     B: 带宽
#     H: 信道矩阵，shape=(num_users, num_antennas)，复数矩阵
#     num_users: 用户数量
#     num_antennas: 天线数量
#     noise_power: 噪声功率
#     """

#     # 计算零力预编码矩阵
#     # W = torch.linalg.pinv(H)

#     I = torch.eye(H.size(0)).to(H.device)  # identity matrix
#     W = H.conj().t() @ torch.inverse(H @ H.conj().t() + noise_power * I)

#     # 初始化功率向量（这里假设每个用户的功率相同）
#     P = torch.ones(num_users).to(device)

#     # # 归一化功率
#     P = P / torch.sum(P)

#     # 计算每个用户的SINR
#     SINRs = []
#     for k in range(num_users):
#         numerator = P[k] * torch.abs(torch.vdot(H[k, :], W[:, k]))**2
#         interferences = torch.zeros(1).to(device)
#         for j in range(num_users):
#             if j != k:
#                 interferences += P[j] * torch.abs(torch.vdot(H[j, :], W[:, k]))**2
#         denominator = interferences + noise_power
#         # denominator = noise_power
#         SINRs.append(numerator / denominator)
#     SINRs = torch.stack(SINRs)
#     # SNR = 10 * torch.log10(SINRs.real)
#     # print(SNR)
#     # 计算每个用户的速率
#     rates = B * torch.log2(1 + SINRs)

#     return rates

# 传统wifi用MIMO时
# def norm_rate_loss(g):
#     # np.random.seed(1)
#     B = 20

#     # 计算噪声功率
#     N = N0 * B
#     inner_path_loss = g.edges['d_link'].data['path_loss']
#     # inner_path_loss_imag = g.edges['d_link'].data['path_loss_imag']
#     # num_devices_per_ap = int(len(inner_path_loss) / n_ap)
#     num_devices_per_ap = n_ue_per_ap
#     # dst_interferes = torch.cat([torch.cat([torch.cat([torch.arange(j * num_devices_per_ap, (j + 1) * num_devices_per_ap) for j in range(n_ap) if j != i])]) for i in range(n_ap)])
#     rate_list = []
#     SNR_list = []

#     ap_ids = list(range(n_ap))  # 假设AP编号是0到9
#     selected_ap_ids = random.sample(ap_ids, 3)
#     # print(selected_ap_ids)
#     # for a in range(0, n_ap):
#     for a in selected_ap_ids:
#         device_ids = np.arange(a * num_devices_per_ap, (a + 1) * num_devices_per_ap)

#         H = inner_path_loss[device_ids]

#         i_rate = compute_mimo_rate(B, H, num_devices_per_ap, n_antenna, N)

#         rate_list.append(i_rate)

#     sum_rate = torch.stack(rate_list)
#     loss = -torch.sum(sum_rate)
#     min_loss = -torch.min(sum_rate)
#     return loss, min_loss


# 传统wifi不用MIMO时
def norm_rate_loss(g):
    # np.random.seed(1)
    B = 20

    # 计算噪声功率
    N = N0 * B
    inner_path_loss = g.edges['d_link'].data['path_loss']
    # inner_path_loss_imag = g.edges['d_link'].data['path_loss_imag']
    num_devices_per_ap = int(len(inner_path_loss) / n_ap)
    # dst_interferes = torch.cat([torch.cat([torch.cat([torch.arange(j * num_devices_per_ap, (j + 1) * num_devices_per_ap) for j in range(n_ap) if j != i])]) for i in range(n_ap)])
    rate_list = []
    SNR_list = []
    ap_ids = list(range(n_ap))  # 假设AP编号是0到9
    selected_ap_ids = random.sample(ap_ids, 3)
    # print(selected_ap_ids)
    # for a in range(0, n_ap):
    for a in selected_ap_ids:
        # for u in range(0, num_devices_per_ap):
        device_ids = np.arange(a * num_devices_per_ap, (a + 1) * num_devices_per_ap)
        i = np.random.choice(device_ids)
        # i = 0

        H = inner_path_loss[i]

        # ZF法计算赋型向量
        H_H = torch.conj(H)
        # W = H_H / (torch.sqrt(torch.dot(H, H_H)) + N)
        W = H_H / (torch.norm(H) + N)
        # 计算信号功率
        S = torch.abs(torch.matmul(W.conj(), H.t()))**2
        # print('H:{}'.format(H))
        # print('w:{}'.format(W))
        # print('S:{}'.format(S))
        # 计算SNR
        i_SNR = S / N
        # 计算速率
        i_rate = B * torch.log2(1 + i_SNR)
        # SNR = 10 * torch.log10(i_SNR)
        # SNR_list.append(SNR)
        # print(SNR)
        rate_list.append(i_rate)

    sum_rate = torch.stack(rate_list)
    # print(torch.mean(torch.stack(SNR_list)))
    loss = -torch.sum(sum_rate)
    min_loss = -torch.min(sum_rate)
    return loss, min_loss


def train(epoch, train_loader):
    """ Train for one epoch. """
    model.train()
    # torch.autograd.set_detect_anomaly(True)
    loss_all = 0
    min_loss_all = 0
    # optimizer.zero_grad()
    for g in train_loader:
        #data = data.to(device)
        # g = datag.generate_channel_graph(3, 3)
        optimizer.zero_grad()

        g = g.to(device)
        # train_g = g.clone()
        # optimizer.zero_grad()

        # output = model(train_g)
        # # print(output)
        # # 将大图分解成小图
        # g_list = dgl.unbatch(train_g)
        output = model(g)
        # print(output)
        # # 将大图分解成小图
        g_list = dgl.unbatch(g)

        # # 将输出收集起来
        # outputs_list = torch.split(output, [g.num_nodes() for g in small_graphs])
        total_loss = 0.0
        outputs_list = torch.split(output, n_ap, dim=0)
        for i in range(0, len(g_list)):
            loss, min_loss = rate_loss(g_list[i], outputs_list[i])
            total_loss += loss
            loss_all += loss.item()
            min_loss_all += min_loss.item()
        # 对总的损失进行反向传播
        total_loss.backward()
        optimizer.step()

    return loss_all / train_n_g, min_loss_all / train_n_g


def test(epoch, test_loader):
    """ Train for one epoch. """
    model.eval()
    # torch.autograd.set_detect_anomaly(True)
    test_loss_all = 0
    norm_loss_all = 0
    test_min_loss_all = 0
    norm_min_loss_all = 0
    with torch.no_grad():
        for g in test_loader:
            g = g.to(device)
            # test_g = g.clone()
            # output = model(test_g)
            # g_list = dgl.unbatch(test_g)
            output = model(g)
            g_list = dgl.unbatch(g)
            outputs_list = torch.split(output, n_ap, dim=0)
            for i in range(0, len(g_list)):
                # print(output)
                test_loss, test_min_loss = rate_loss(g_list[i], outputs_list[i])
                norm_loss, norm_min_loss = norm_rate_loss(g_list[i])

                test_loss_all += test_loss.item()
                norm_loss_all += norm_loss.item()
                test_min_loss_all += test_min_loss.item()
                norm_min_loss_all += norm_min_loss.item()

            # print('Epoch {:03d}, Train Rate: {:.4f}, Test Rate: {:.4f}'.format(epoch, -test_loss, norm_loss))
    # print(loss_all)

    return test_loss_all / test_n_g, norm_loss_all / test_n_g, test_min_loss_all / test_n_g, norm_min_loss_all / test_n_g


import time

start = time.time()

for i_ap in range(4, 10):
    N0 = 0.05
    n_ap = i_ap
    n_ue_per_ap = 4
    n_antenna = 4
    train_n_g = 1000
    test_n_g = 500
    # 假设你有1000个种子
    print('n_ap:{}, n_ue_per_ap:{}, n_antenna:{}, train_n_g:{}, test_n_g:{}\n'.format(n_ap, n_ue_per_ap, n_antenna, train_n_g, test_n_g))
    total_seeds = train_n_g + test_n_g

    # 将种子打乱
    np.random.seed(0)  # 你可以选择任何你喜欢的种子，如0
    seeds = np.random.permutation(total_seeds)

    # 将种子分为训练集和测试集
    train_seeds = seeds[:int(train_n_g)]  # 假设你将80%的数据用于训练
    test_seeds = seeds[int(train_n_g):]  # 剩下的20%用于测试
    train_data = WiFi_Dataset(train_n_g, n_ap, n_ue_per_ap, train_seeds, data_name='Train_WiFi_dataset', n_antenna=n_antenna)
    test_data = WiFi_Dataset(test_n_g, n_ap, n_ue_per_ap, test_seeds, data_name='Test_WiFi_dataset', n_antenna=n_antenna)
    batch_size = 64
    train_loader = DataLoader(train_data, batch_size, shuffle=True, collate_fn=collate)
    test_loader = DataLoader(test_data, batch_size, shuffle=False, collate_fn=collate)
    print(train_data)
    print(test_data)
    end1 = time.time()

    print('Data_Time: ', end1 - start)
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    device = 'cpu'
    model = WFHGCN(n_antenna).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
    # optimizer = torch.optim.Adagrad(model.parameters())
    # optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.9)
    train_loss_list = []
    test_loss_list = []
    norm_loss_list = []
    train_min_loss_list = []
    test_min_loss_list = []
    norm_min_loss_list = []
    training_epochs = 1000
    patience = 100
    early_stopping = EarlyStopping(patience=patience, verbose=True)
    for epoch in range(0, training_epochs):
        start = time.time()
        train_loss, train_min_loss = train(epoch, train_loader)
        end2 = time.time()

        print('Train_Time: ', end2 - start)
        test_loss, norm_loss, test_min_loss, norm_min_loss = test(epoch, test_loader)
        end3 = time.time()

        print('Test_Time: ', end3 - end2)
        train_loss_list.append(train_loss)
        test_loss_list.append(test_loss)
        norm_loss_list.append(norm_loss)
        train_min_loss_list.append(train_min_loss)
        test_min_loss_list.append(test_min_loss)
        norm_min_loss_list.append(norm_min_loss)
        # test_loss = 0
        # norm_loss = 0
        #调整学习率
        scheduler.step()
        print('Epoch {:03d}, Train Rate: {:.16f} Min:{:.16f}, Test Rate: {:.16f} Min:{:.16f},Norm Rate: {:.16f} Min:{:.16f}'.format(epoch, -train_loss, train_min_loss, -test_loss, test_min_loss, -norm_loss, norm_min_loss))
        early_stopping(train_loss, model)

        if early_stopping.early_stop:
            print("Early stopping")
            break

        df = pd.DataFrame({'Train_epochs': [i for i in range(epoch + 1)], 'Train_loss': train_loss_list, 'Test_loss': test_loss_list, 'norm_loss': norm_loss_list, 'Train_min_loss': train_min_loss_list, 'Test_min_loss': test_min_loss_list, 'norm_min_loss': norm_min_loss_list})
        df.to_csv('./MU-MIMO_Train{}_Loss_ap{}_per_ue{}_n_antenna{}_Train_n{}_Test_n{}.csv'.format(training_epochs, n_ap, n_ue_per_ap, n_antenna, train_n_g, test_n_g))