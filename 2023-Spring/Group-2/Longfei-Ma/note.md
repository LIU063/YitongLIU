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

# Week5 
## 进行知识蒸馏辅助训练初步实验

系统模型为D2D通信模型，优化目标为最大化和速率（参照沈逸飞GNN论文）

神经网络模型采用PCNet

<img width="696" alt="1681830753795" src="https://user-images.githubusercontent.com/63155472/232822016-ced53b4a-45e5-4161-8ec0-be1ad76e676b.png">
<img width="703" alt="1681830777783" src="https://user-images.githubusercontent.com/63155472/232822126-9f4306dc-5d41-4643-827a-4ae0a01d82aa.png">

对比算法为监督学习（利用优化算法解出标签），无监督学习（沈逸飞论文训练方式）

知识蒸馏方法所用损失函数为上述两种方法的损失函数加权求和


<img width="473" alt="1681831186893" src="https://user-images.githubusercontent.com/63155472/232824062-fba328de-5e09-48d1-8260-5c9c011ae2c6.png">


# Week6 
## 撰写RB分配任务代码
已完成部分：

1.随机生成信道状态、动作数据，计算得到速率，通过监督学习的方式对critic网络进行预训练

2.基于预训练的critic模型，在线训练actor和critic 


下一步计划：

1.生成一定量的离线数据对actor和critic进行离线训练，而后进行在线微调

2.探讨离线过程中标签数据对模型性能的影响


# Week7 
## 继续进行RB分配任务实验

<img width="1193" alt="1683772181904" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/30a1e482-c90c-42e8-aa22-d19930e579ff">

# Week8 
## 继续进行RB分配任务实验
采用不同优化器的性能对比

<img width="447" alt="1684373286066" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/d83bc4aa-d136-4bd7-a27a-fd18f2b92509">
<img width="452" alt="1684373372452" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/5afe1909-f8f6-46bb-aab8-f73bf49467bb">

不进行探索的性能对比

<img width="448" alt="1684373468114" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/8fcd5ffd-b38a-400d-8496-98aa5966479e">
<img width="447" alt="1684373491780" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/3134039e-7add-4369-8e95-2d4aa2a09072">

# Week9 
## 继续进行RB分配任务实验
不同优化器探索/非探索性能

<img width="1187" alt="1684946710655" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/35468e30-dc9f-4d84-b77c-f8540af524a8">

不同标签来源

<img width="906" alt="1684946762775" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/6ea55410-7df6-498c-907c-83044b8cc3b6">




