# 2024.4.21
## 本周进展  
1. 代码进展：   
仿真已完成  
<!--![model](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2024-Spring/Group-1/Zhaowei-Wang/figure/test_40_100.jpg) -->
3. 对比算法：  
经过调研，准备与博弈论、遗传算法和强化学习算法进行对比
## 下周计划
实现对比算法，验证本算法的有效性


# 2024.4.21
## 本周进展  
1. isn+星链项目书+ppt  
2. 代码进展  
<!--![model](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2024-Spring/Group-1/Zhaowei-Wang/figure/1.jpg)  -->
![model](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2024-Spring/Group-1/Zhaowei-Wang/figure/2.jpg)  
access 对边的概率进行采样，在采样基础上优化功率，不断迭代   
存在的问题：  
（1）随着训练进行，power 性能变差  
（2） access变化不大
## 下周计划
改正目前存在的问题，思考实现对比算法


# 2024.3.31
## 本周进展
![model](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2024-Spring/Group-1/Zhaowei-Wang/figure/liucheng.png)
写模型融合训练的代码，优化训练的结果作为选择的loss，不断迭代训练选择


# 2024.3.24
## 本周进展
完成了科学研究计划内容撰写  
调研了PLS 的 beamforming ,gnn解决beamforming，以及接入选择的调研


# 2024.3.17
## 本周进展
1. globecom 扩展
![model](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2024-Spring/Group-1/Zhaowei-Wang/figure/gc1.jpg)
2. 存在的问题：  
（1）虽然有收敛，但效果较差--→ 调整代码   
（2）access selection没有被训练到，始终是0.33，0.33，0.34。--→查找模型上的问题//对图抽样训练，选择抽样效果最好的连接图（过于复杂，下下策）   
（3）现在图里包括user node，server node，正在思考如何处理窃听者问题.--→修改图结构：加入eve node//或者从user node中分出eve node.   
（4）优化节点以及约束条件较多   
## 下周计划   
（1）调研撰写攻博期间科学研究计划，针对正在做的globecom扩展写。   
（2）gnn+??? 算法融合，写入研究计划中。
（3）改改代码
