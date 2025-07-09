<p id="table"></p>

## Table of Contents

- <a href="#1"> Week 1 (2025.07.03 – 2025.07.10)
<br/>

------

<br/>

<p id="1"></p>

# <a href="#table">Week 1 (2025.07.03 – 2025.07.10)</a>

## 进展：
1.预编码初始化改变：初始化两个预编码分别指向两个目标区域。  
2.改用Adam优化器，优化效果更明显，经调参实验lr=0.05最优  
3.双目标区域之间的区域抑制，但是效果并未提升。
![训练迭代图](https://github.com/LIU063/YitongLIU/blob/main/RM-Report/Yitong%20Liu/images/%E8%BF%AD%E4%BB%A3%E5%9B%BE.png)
区域1平均值: 0.80258095  
区域1方差: 0.00079448335  
区域2平均值: 0.69092506  
区域2方差: 0.0011540927  
## 问题1：
发射机功率大的时候波束集中在两个方向的合并区域，发射机功率小的时候容易分波指向目标区域。  
已数学证明该现象：
![证明过程](https://github.com/LIU063/YitongLIU/blob/main/RM-Report/Yitong%20Liu/images/%E8%AF%81%E6%98%8E.jpg)
### 44dbm:
![44dbm](https://github.com/LIU063/YitongLIU/blob/main/RM-Report/Yitong%20Liu/images/44dbm.png)
### 50dbm:
![50dbm](https://github.com/LIU063/YitongLIU/blob/main/RM-Report/Yitong%20Liu/images/50dbm.png)
### 80dbm:
![80dbm](https://github.com/LIU063/YitongLIU/blob/main/RM-Report/Yitong%20Liu/images/80dbm.png)
## 问题2：
尝试了优化发射机位置，也尝试了初始胡化不同起始位置，但是位置的梯度很小（几乎趋近于0），位置信息基本没有更新。  
Grad Pos: [-8.2735956e-04  5.2624124e-05  2.7738390e-03]  
Grad Ori: [-1.12880795e-10 -1.02118782e-11 -2.89631402e-10]  
Step 001 - Rate1: 0.0600, Rate2: 0.0000 | Tx Pos: [10. 10. 10.] | Tx Ori: [ 0.01 -0.01 -0.01]  
Grad Pos: [ 2.3364455e-05  6.2242549e-07 -9.5769916e-05]  
Grad Ori: [-2.80417833e-12  4.03611606e-13 -1.32209365e-11]  
Step 002 - Rate1: 0.0568, Rate2: 0.0000 | Tx Pos: [10. 10. 10.] | Tx Ori: [ 0.02 -0.02 -0.02]  
Grad Pos: [-4.1891197e-03 -7.0448696e-05 -7.2704433e-03]  
Grad Ori: [-2.2894670e-07  4.7367205e-08 -1.0912792e-06]  
Step 003 - Rate1: 0.0247, Rate2: 0.0006 | Tx Pos: [10. 10. 10.] | Tx Ori: [ 0.02 -0.01 -0.01]  
Grad Pos: [0. 0. 0.]  
Grad Ori: [0. 0. 0.]  
Step 004 - Rate1: 0.0739, Rate2: 0.0000 | Tx Pos: [10. 10. 10.] | Tx Ori: [ 0.03 -0.01 -0.01]  
