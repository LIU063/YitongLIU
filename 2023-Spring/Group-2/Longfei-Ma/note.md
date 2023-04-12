# Week1 进行metacom终稿修改
# Week2 进行DTforRL magazine文章撰写工作 
## 绘制场景图
<img width="828" alt="1679907252610" src="https://user-images.githubusercontent.com/63155472/227892420-a630ce0a-81e2-406a-8a47-70d54adb1aa3.png">
<img width="445" alt="1679907342461" src="https://user-images.githubusercontent.com/63155472/227892792-59c9f0ba-9cca-4df4-bd47-00b697894df7.png">
<img width="461" alt="1679907367885" src="https://user-images.githubusercontent.com/63155472/227892899-053d127c-ec4b-4d91-b4b5-2b32cfc7eb6d.png">

## 阅读文献：PATHWAYS: ASYNCHRONOUS DISTRIBUTED DATAFLOW FOR ML

# Week3 撰写DTforRL magazine
## 进行case study仿真实验：urllc场景下的AP选择
<img width="370" alt="1680746292010" src="https://user-images.githubusercontent.com/63155472/230253246-88d08eb0-2db8-4cf6-8693-21d8fe05508f.png">

## Fig1
<img width="927" alt="1680761788328" src="https://user-images.githubusercontent.com/63155472/230287697-45a10737-9581-4547-8252-3e5eb1b4a645.png">

# Week4 
## 修改DTforRL magazine
## 探索offline RL在通信场景下的应用
传统的online RL算法难以在实际的通信场景部署的原因

1.训练需要智能体与环境进行大量交互，训练成本高，速度慢。

2.在实际场景中进行随机探索可能会导致不良结果。

offline RL——agent不和环境进行交互，利用固定的数据集进行训练。
<img width="1190" alt="1681307165449" src="https://user-images.githubusercontent.com/63155472/231477979-6816ffe9-d93c-4452-9468-3fc719aa6f3b.png">

存在挑战：

1.无法进行随机探索 

2.受数据集质量的影响 

3.训练策略与行为策略存在分布偏移 

导致经典RL算法往往在离线设定下学习效果较差。

主流方法：策略约束，值函数正则，不确定性估计

计划使用offline RL做一些通信上的task，比如之前做的UAV轨迹优化、资源分配等。
