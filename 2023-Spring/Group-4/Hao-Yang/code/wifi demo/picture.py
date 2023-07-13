import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# 使用glob找到所有的CSV文件
csv_files = glob.glob('*.csv')

# 遍历所有的CSV文件
for csv_file in csv_files:

    # 从csv文件中读取数据
    # data_path = 'MU-MIMO_Train_Loss_ap3_per_ue5_Train_n2000_Test_n1000'
    filename = os.path.splitext(os.path.basename(csv_file))[0]
    data_path = filename
    data = pd.read_csv(data_path + '.csv')

    # 创建一个新的figure对象
    plt.figure()

    # 绘制Train_loss曲线
    plt.plot(data['Train_epochs'], data['Train_loss'], label='Train Loss')

    # 绘制Test_loss曲线
    plt.plot(data['Train_epochs'], data['Test_loss'], label='Test Loss')
    # 绘制Test_loss曲线
    plt.plot(data['Train_epochs'], data['norm_loss'], label='Norm Loss')
    # 设置图例
    plt.legend()

    # 设置x轴标签
    plt.xlabel('Epochs')

    # 设置y轴标签
    plt.ylabel('Loss')

    # 设置标题
    plt.title('Neural Network Convergence Performance')

    # 显示图形
    # plt.show()
    plt.savefig('./' + data_path + '.svg')
