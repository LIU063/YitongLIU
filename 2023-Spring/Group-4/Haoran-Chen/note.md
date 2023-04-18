# 周报 - 20230418
## 本周工作小结
1、建模与实现

![image](./images/20230418-01.png)

2、数据集选择以及yolov5模型选择

数据集：UA-DETRAC，车辆检测和跟踪的大规模数据集，由Cannon EOS 550D相机在中国北京和天津的24个不同地点拍摄的10小时视频组成，类别包括car, bus, van, others

![image](./images/20230418-01.png)

Fig：使用yolov5s.pt预训练模型（在coco数据集上训练），在UA-DETRAC数据集上的训练效果。


## 下一步工作安排

继续完善问题建模细节以及目标识别模型yolov5的实现

<br>

---

<br>

# 周报 - 20230412
## 本周工作小结
1、视频分析系统中的一些动机与结论

![image](./images/20230412-01.png)

![image](./images/20230412-02.png)

Fig4(a)：识别精度关于分辨率的曲线，x1为小目标，x2为行人靠近的过程

Fig4(b)：识别精度关于帧率的曲线，y1为车辆快速移动，y2为交通拥堵场景

凹函数形式：![image](./images/20230412-03.png)

Wang, Can, et al. **"Joint configuration adaptation and bandwidth allocation for edge-based real-time video analytics."** IEEE INFOCOM 2020-IEEE Conference on Computer Communications. IEEE, 2020.

2、问题转化与建模

![image](./images/20230412-04.png)


3、yolov5源码学习

[官方源码测试](https://www.bilibili.com/video/BV1Gv4y1H7aY)


## 下一步工作安排

继续完善模型细节以及识别模型的实现

<br>

---

<br>

# 周报 - 20230405
## 本周工作小结
1、文献阅读

1️⃣Jiang, Xiantao, et al. **"A survey on multi-access edge computing applied to video streaming: Some research issues and challenges."** IEEE Communications Surveys & Tutorials 23.2 (2021): 871-903.

**优化指标**：Energy Consumption，Throughput，QoE，Service Latency，Cost，Fairness，Cache Hit Ratio，Revenue

**MEC场景下视频分析系统（video analytics system）**：object detection, object tracking, and semantic segmentation

2️⃣Kim, Woo-Joong, and Chan-Hyun Youn. **"Lightweight online profiling-based configuration adaptation for video analytics system in edge computing."** IEEE Access 8 (2020): 116881-116899.

**决定因素**：图像帧分辨率和速率（frame resolution and sampling rate）

**矛盾**：计算资源（如GPU）的有限性，需要在保证精度的前提下，对视频流进行合理配置，即resource-accuracy tradeoff。

**思路**：依据目标在视频流中的位置和大小的变化（velocity of objects on location and size）设计配置控制器（configuration controller），而不是凭借经验值（empirically measured value）。

![image](./images/20230405-01.png)

![image](./images/20230405-02.png)

3️⃣Wu, Kun, et al. **"Soudain: Online adaptive profile configuration for real-time video analytics."** 2021 IEEE/ACM 29th International Symposium on Quality of Service (IWQOS). IEEE, 2021.

4️⃣Zhou, Tian, Fubao Wu, and Lixin Gao. **"Profiling-free Configuration Adaptation and Latency-Aware Resource Scheduling for Video Analytics."** 2022 IEEE International Conference on Big Data (Big Data). IEEE, 2022.

2、系统设计和实现

场景：用户端（传感器设备）的计算资源有限，无法运行目标任务，或无法满足时延指标，需要卸载到远程云（计算中心）。但是通信资源不能满足任务整体的传输，因此，需要对其进行配置，或者部分取舍。

业务：任务卸载

模型：YOLO系列

3、审稿：Energy-Efficient Cellular-Connected UAV Swarm Control Optimization

## 下一步工作安排

继续完善和落实实现方案和模型选择


<br>

---

<br>


# 周报 - 20230329
## 本周工作小结
1、无人机基站资源分配

存在问题：PSO算法性能仍不如贪心算法，差距大概在8％-10％，且每次执行时不够稳定，导致算法无法顺利迭代；<br>
在使用搜索能力更强的冯诺依曼局部拓扑之后，并没有明显的改善。

2、视频流数据的信息价值评估

Zhao, Lindong, Dan Wu, and Liang Zhou. **"Quality-of-Decision-Driven Machine-Type Communication."** IEEE Internet of Things Journal 9.17 (2022): 16631-16642.<br>
保留视频流中关键帧的图片信息，舍弃无用帧中的内容，实现减少传输数据量、缓解通信信道负担的目的，同时对决策效果（QoE）的影响微乎其微

Yeung, Serena, et al. **"End-to-end learning of action detection from frame glimpses in videos."** Proceedings of the IEEE conference on computer vision and pattern recognition. 2016.<br>
该任务为动作识别，需要判断动作的开始和结束时间。该工作在观测网络（observation network）的基础上，训练循环网络（recurrent Network）：判断候选帧、预测决策以及时序位置。极大地减少了动作识别任务所需的帧数量。

联系：该机制类似于信息价值评估器的功能，对视频帧进行筛选。

## 下一步工作安排
1、继续调整PSO算法的参数，可能需要重新选择合适算法；<br>
2、确定视频流数据的信息价值评估部分的具体实现方案。

<br>

---

<br>

# 周报 - 20230322
## 本周工作小结
1、算法流程图

**优化目标**：使得用户传输的信息价值最大<br>
**输入**：UE坐标、UE数据量<br>
**优化变量**：UE连接状态（associations、bandwidth）、DBS坐标（coordinates_xyz）<br>
1️⃣**系统初始化**<br>
2️⃣&emsp;DBS坐标初始化<br>
3️⃣&emsp;用户连接（频谱分配）初始化<br>
4️⃣**两步迭代**<br>
5️⃣while：传输的信息价值（数据量）增大<br>
6️⃣&emsp;优化DBS坐标：（水平_xy）位置加权k-means、（垂直_z）搜索<br>
7️⃣&emsp;优化用户连接（频谱分配）：PSO算法，拓扑结构（全局互联、环状拓扑、冯诺依曼拓扑）<br>
8️⃣算法结束

2、部分仿真结果

PSO算法收敛曲线图：<br>
![image](./images/20230322-01.png)

说明：在固定用户UE数量=30，无人机基站DBS数量=3的情况下，PSO算法优化用户UE连接以分配频谱资源。<br>
问题及可能的解决方法：PSO算法其收敛速度介于暴力搜索和贪心算法之间，但其效果相比贪心并没有优势，在尝试不同的拓扑结构之后也并无改善；可能是因为优化变量为离散整数，导致其难以继续搜索解空间，后续可尝试进一步调整算法的各参数。<br>

## 下一步工作安排

（1）继续改进和完善仿真过程，使得算法性能表现超过贪心算法；<br>
（2）接口：基于抽帧的视频数据的信息价值表征方法，明确应用信息价值机制后的数据尺度。<br>

系统模型示意图<br>
![image](./images/20230322-04.png)

粒子群算法的拓扑结构<br>
![image](./images/20230322-02.png)

位置加权k-means算法<br>
![image](./images/20230322-03.png)


