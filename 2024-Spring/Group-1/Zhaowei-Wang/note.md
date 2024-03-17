# 2024.3.17
## 本周进展
1. globecom 扩展
![model](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2024-Spring/Group-1/Zhaowei-Wang/figure/gc1.jpg)
2. 存在的问题：（1）access selection没有被训练到，始终是0.33，0.33，0.34。--→对图抽样训练，选择抽样效果最好的（过于复杂，下下策）
              （2）现在图里包括user node，server node，正在思考如何处理窃听者问题.--→修改图结构：加入eve node//或者从user node中分出eve node.
              （3）
