import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def generate_channel_graph(num_AP, num_dev, num_time, radius=0.2, alpha=2, noise_level=0.95, p_data_burst=0.7):

    # 创建一个空图
    G = nx.DiGraph()

    # 添加AP节点，并给每个节点分配一个随机位置
    for i in range(num_AP):
        pos = np.random.rand(2)  # 在单位方形内随机分配位置
        G.add_node(f'AP{i}', pos=pos)

    # 添加设备节点，并给每个节点分配一个在AP周围的随机位置
    for i in range(num_AP):
        for j in range(num_dev):
            # 在AP周围的半径为radius的圆内随机分配位置
            theta = 2 * np.pi * np.random.rand()  # 随机角度
            r = radius * np.sqrt(np.random.rand())  # 随机距离（这样生成的点会均匀地分布在圆内）
            dx, dy = r * np.cos(theta), r * np.sin(theta)
            pos = G.nodes[f'AP{i}']['pos'] + np.array([dx, dy])
            G.add_node(f'Dev{i}{j}', pos=pos)

            # 为每个设备节点生成一个数据流，30%的时间步没有数据
            data_flow = np.random.choice([0] + list(range(1, 11)), size=num_time, p=[1 - p_data_burst] + [p_data_burst / 10] * 10)
            G.nodes[f'Dev{i}{j}']['data_flow'] = data_flow

    # 添加边，即生成信道
    for i in range(num_AP):
        for j in range(num_dev):
            for t in range(num_time):
                # 生成AP到自己设备的信道
                pos1 = G.nodes[f'AP{i}']['pos']
                pos2 = G.nodes[f'Dev{i}{j}']['pos']
                dist = np.linalg.norm(pos1 - pos2)  # 计算距离
                if t == 0:
                    h_ap_to_dev = np.array([1 / np.sqrt(2) * (np.random.randn() + 1j * np.random.randn()) / (dist**alpha)])
                else:
                    h_prev = G[f'AP{i}'][f'Dev{i}{j}']['h'][t - 1]
                    noise = 1 / np.sqrt(2) * (np.random.randn() + 1j * np.random.randn()) / (dist**alpha)
                    h_ap_to_dev = np.append(G[f'AP{i}'][f'Dev{i}{j}']['h'], noise_level * h_prev + noise)  # adjust the coefficient 0.9 and the noise level according to your needs
                G.add_edge(f'AP{i}', f'Dev{i}{j}', h=h_ap_to_dev)

                # 生成AP到其他设备的信道
                for k in range(num_AP):
                    if k != i:
                        for l in range(num_dev):
                            pos2 = G.nodes[f'Dev{k}{l}']['pos']
                            dist = np.linalg.norm(pos1 - pos2)  # 计算距离
                            if t == 0:
                                h_ap_to_dev = np.array([1 / np.sqrt(2) * (np.random.randn() + 1j * np.random.randn()) / (dist**alpha)])
                            else:
                                h_prev = G[f'AP{i}'][f'Dev{k}{l}']['h'][t - 1]
                                noise = 1 / np.sqrt(2) * (np.random.randn() + 1j * np.random.randn()) / (dist**alpha)
                                h_ap_to_dev = np.append(G[f'AP{i}'][f'Dev{k}{l}']['h'], noise_level * h_prev + noise)  # adjust the coefficient 0.9 and the noise level according to your needs
                            G.add_edge(f'AP{i}', f'Dev{k}{l}', h=h_ap_to_dev)

    return G


import matplotlib.cm as cm


def draw_channel_graph(G, num_AP):
    pos = nx.get_node_attributes(G, 'pos')

    # # 绘制AP节点，每个AP组用同一个色系中的不同颜色
    # cmap = cm.get_cmap('viridis', num_AP)  # 选择一个色图并将其分为num_AP份
    for i in range(num_AP):
        nx.draw_networkx_nodes(G, pos, nodelist=[f'AP{i}'], node_color='blue', node_size=1000)  # 增大AP节点的大小

    # 绘制设备节点
    dev_nodes = [node for node in G.nodes if node.startswith('Dev')]
    nx.draw_networkx_nodes(G, pos, nodelist=dev_nodes, node_color='red', node_size=500)

    # 绘制边
    nx.draw_networkx_edges(G, pos, edge_color='grey')

    # 绘制节点标签
    nx.draw_networkx_labels(G, pos)

    plt.show()


# 测试
G = generate_channel_graph(3, 3, 30)
draw_channel_graph(G, 3)

# # 输出信道系数
for u, v, data in G.edges(data=True):
    print(f'{u} --> {v}: h = {data["h"]}')

import pickle

N = 10  # 你希望生成的样本数量
graphs = [generate_channel_graph(3, 3, 30) for _ in range(N)]

with open('graphs.pkl', 'wb') as f:
    pickle.dump(graphs, f)
