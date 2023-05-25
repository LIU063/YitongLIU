import pandas as pd
import pickle
import numpy as np
import networkx as nx
import random


# 函数用于计算SNR和速率
def calculate_snr_and_rate(h, P=1, B=20, N0=0.1):
    SNR = P * abs(h)**2 / N0 / B
    SNR = 10* np.log10(SNR)    #dB
    rate = B * np.log2(1 + SNR)  # 计算速率  Mbps
    return SNR, rate



# 函数用于模拟传统WiFi通信
def simulate_wifi_traditional(graphs):
    i = 0
    # 遍历图列表
    for graph in graphs:
        # 创建一个空的数据框来存储仿真结果
        df_results = pd.DataFrame(columns=['AP', 'Device', 'Time', 'SNR', 'Rate', 'TransmissionTime'])
        # 遍历每个时间步
        for t in range(len(graph.nodes[next(dev for dev in list(nx.nodes(graph)) if 'Dev' in dev)]['data_flow'])):

            # 按照AP分组设备
            ap_to_devs = {}
            for node in graph.nodes:
                if 'AP' in node:
                    ap_to_devs[node] = [dev for dev in graph.neighbors(node) if (graph.nodes[dev]['data_flow'][t] > 0 and f'Dev{node[2:]}' in dev)]

            # 对每个AP进行模拟
            for node, devs in ap_to_devs.items():
                if devs:
                    # 随机选择一个设备进行传输
                    chosen_dev = random.choice(devs)

                    # 计算SNR和速率
                    SNR, rate = calculate_snr_and_rate(graph[node][chosen_dev]['h'][t])

                    # 计算传输时间
                    data_to_transmit = graph.nodes[chosen_dev]['data_flow'][t]
                    transmission_time = data_to_transmit / rate

                    # 保存结果
                    df_results = df_results.append({'AP': node, 'Device': chosen_dev, 'Time': t, 'SNR': SNR, 'Rate': rate, 'TransmissionTime': transmission_time}, ignore_index=True)

                    # 更新下一时刻的数据流
                    if t < len(graph.nodes[chosen_dev]['data_flow']) - 1:
                        graph.nodes[chosen_dev]['data_flow'][t + 1] += graph.nodes[chosen_dev]['data_flow'][t] - data_to_transmit

        # 保存结果
        df_results.to_csv('results{}.csv'.format(i), index=False)
        i += 1


# 读取图列表
with open('graphs.pkl', 'rb') as f:
    graphs = pickle.load(f)

# 运行模拟
simulate_wifi_traditional(graphs)
