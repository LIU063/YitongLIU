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
