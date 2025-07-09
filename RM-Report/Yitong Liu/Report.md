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
![训练迭代图](https://github.com/LIU063/YitongLIU/blob/main/RM-Report/Yitong%20Liu/images/%E8%BF%AD%E4%BB%A3%E5%9B%BE.png)
## 问题：
发射机功率大的时候波束集中在两个方向的合并区域，发射机功率小的时候容易分波指向目标区域。已数学证明该现象：
![证明过程](https://github.com/LIU063/YitongLIU/blob/main/RM-Report/Yitong%20Liu/images/%E8%AF%81%E6%98%8E.jpg)
![44dbm]()
![50dbm]()
![80dbm]()
