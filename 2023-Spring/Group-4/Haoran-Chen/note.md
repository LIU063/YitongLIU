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
