# 第一周周报


## 工作进度
本周主要调试无人机避障代码，之前提出的2个DQN，一个负责规划路线，一个负责避障的方法难以收敛，改换基于MCTS(蒙特卡洛树搜索的方法)，在不同的树搜索深度下测试碰撞发生的概率，编写baseline对比算法，与树搜索算法进行比较。下一步考虑参考TWC2021一篇文章的场景将此问题的goal改成让各个用户和速率最大的点。后续继续调试代码，绘制图表，准备撰写论文



## 6G大会
可解释性资源调配推理要求利用可解释性AI进行透明、可靠、可担责的按需服务，目前这一方向很少有人提到，相应的可解释性框架也少之又少，可以探索一番。
# 第二周周报


## 工作进度
画架构图以及论文所需的结果图。
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure1.jpg)
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure2.png)
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure3.png)
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure4.png)
## 下周工作安排
尽快撰写完论文，投稿。
# 第三周周报
上周提到的对比算法实现及其性能比较
![Image text](https://github.com/UNIC-Lab/Weekly-Report/raw/main/2023-Spring/Group-2/Yunhao-Quan/pic/figure3.svg)
# 第四周周报
## 修改论文
## 调研XAI在MARL中的应用
   (1)能否采用shapely的方法评估合作MARL过程中的参与者贡献程度
   
   (2)MARL shapely值计算复杂度可能会很高
   
   (3) MARL场景的选取
## 配置环境，在muliti-gym中尝试实现MARL shapely计算。
# 第五周周报
在算法收敛性分析图中，random算法在刚开始会出现小幅度上升，修改环境,debug解决这一问题。

