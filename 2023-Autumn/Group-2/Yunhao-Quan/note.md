### 2023.12.26
# 工作
1.完成贝叶斯网络代码，在RML2016.10a数据集上进行性能分析。
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/d562895d-1721-4ab4-97ad-67c2c31b4224)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/df80c13d-570d-4dc1-9a4a-69b37bf92dea)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/0d3f8f64-67ff-43fb-b811-abca7afe1296)
# 下周计划
1.测试贝叶斯网络在不同数据集上的效果以及各种超参数对于性能的影响。
2.思考贝叶斯网络在小样本条件下的应用。










### 2023.11.6
# 继续完成基于贝叶斯网络的调制信号识别。
![output](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/cfd662cd-ea09-44b5-8fd4-249c41ca9267)

![output](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/5975d10f-832e-4327-90bc-faa6c4cc4c8a)


在RML2016.4C数据集上进行初步实验。
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/5da2c49a-b94b-488a-bf38-ce2fdafd4d99)




















### 2023.10.29
# 本周进展

1.整体代码差不多写完了，下周多跑几遍看看性能。

2.考虑采用expected calibration error（ECE）来描述模型可靠性。

3.ECE的思想：

(1) 根据分类器置信分数p(y|x)将其对应的输出分为M个大小相等的区间，再根据置信分数对于测试数据集点进行分类，分入相应的区间中。

(2) 在每个区间对应的仓B中，精度如上
    ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/aeb2d5ed-3dd2-46ae-a201-af7f9700f6fe)
    
(3) 相应的confidence如上
    ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/1484f7c2-96f8-451a-90c1-4417095f5555)
    
(4)ECE计算如上
    ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/dfd43054-1f91-445b-99a5-0e7426174082)



     









### 2023.10.16
# 本周进展
1.贝叶斯网络代码基本完成，读取数据集代码基本完成。

2.阅读相关文献，思考如何量化贝叶斯网络性能。

  [1] Robust parameter estimation with a small bias against heavy contamination（https://www.sciencedirect.com/science/article/pii/S0047259X08000456）

  [2] Robust Bayesian inference via γ-divergence （https://www.tandfonline.com/doi/full/10.1080/03610926.2018.1543765）

#  下周计划

  训练模型，微调代码。











### 2023.9.18
# 本周进展
1.重写贝叶斯网络代码，之前代码逻辑有问题。

2.阅读贝叶斯深度学习综述及相关论文。
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/52443090/7632fd53-d56d-4f2d-9120-8818d3a46bc2)

 1.DNN为点估计，参数为常数，拟合出的参数确定唯一。
 
 2.BNN是一种概率估计参数为概率分布拟合出的图像，它存在一个范围里。




### 2023.9.5
# 本周进展
1.初步撰写贝叶斯神经网络应用于自动调制分类中(AMC)，目前代码存在bug，正在debug

2.学习基于变分推断的BNN训练方法。

3.学习torchbnn框架的使用

# 下周安排
1.继续编写代码，修改程序，debug

2.思考如何通过何种方式准确表示BNN决策置信度 
