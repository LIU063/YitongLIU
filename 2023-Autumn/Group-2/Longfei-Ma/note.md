# 2024.1.29周报

参考沈逸飞2023年的TWC论文梳理论文大纲

Y. Shen, J. Zhang, S. H. Song and K. B. Letaief, "Graph Neural Networks for Wireless Communications: From Theory to Practice," in IEEE Transactions on Wireless Communications, vol. 22, no. 5, pp. 3554-3569, May 2023, doi: 10.1109/TWC.2022.3219840.
[Graph_Neural_Networks_for_Wireless_Communications_From_Theory_to_Practice.pdf](https://github.com/UNIC-Lab/Weekly-Report/files/14076322/Graph_Neural_Networks_for_Wireless_Communications_From_Theory_to_Practice.pdf)

1.	引言部分，可以考虑分小节写
  
2.	无线通信模型，分别描述D2D功率控制和RB分配任务的系统模型

3.	所提出的训练方法，描述在不同神经网络架构下，不同训练框架下的使用方法。加一些对有效性的分析。（这一部分可以考虑分成两节）

4.	仿真结果，分成两小节，分别分析功率控制和RB分配的仿真结果。


# 20231226周报

## 构造非凸函数，定性解释蒸馏优势

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/515abcde-6aee-4f5c-ab35-8f17aec8988d)

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/843dfc45-4d54-4566-b885-22f7850b7d79)



# 20231212周报

## 绘制RB分配任务实验结果

<img width="854" alt="1702351223627" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/e11fbbf7-65ec-400a-9fcb-8909213239bc">

<img width="865" alt="1702351423411" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/a5b8c5a3-e0f1-45b2-9606-c0a620dae18a">

<img width="863" alt="1702351905802" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/6433504a-0703-44bc-a5c0-0eec140f107f">

<img width="715" alt="1702352123800" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/da25e35f-a613-4ea9-94db-9c6129bc94c1">

<img width="683" alt="1702351977442" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/4dadcc98-a685-4268-abc4-0aeb95dd0f96">

<img width="620" alt="1702352748503" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/682a3985-e395-4a42-9d82-78231fc7e95e">

<img width="599" alt="1702352775520" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/175ae338-fb3e-47ea-8c4b-5bdb2d009fac">











# 20231113周报

## 继续进行RB分配任务实验

目前不同用户数和RB数下的训练结果已经基本跑完，对数据整理完成后绘制阴影图。

对论文方案的进一步讨论：

1.标签质量对训练效果的影响

<img width="777" alt="1699840747824" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/a1f3f3e7-1193-42ce-8fe9-c328e4d4dfa6">

蒸馏效果与监督学习效果并没有对应关系，并且当标签质量下降时，监督学习效果会急剧恶化，后续计划生成更多不同质量的标签进行进一步比较。

2.探索最优权重策略与蒸馏项loss值的关系

3.能否根据实验中所观察到的特征，给出一种样本级别调整权重的策略




# 20231108周报

## 继续进行RB分配任务实验

目前标签数据已经基本跑完，更新了DPG框架下不同用户数和RB数情况下的实验结果：

<img width="790" alt="1699325890003" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/ec35a3b8-484b-4327-83e1-1e4e893ea078">


<img width="775" alt="1699325772194" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/d1f20754-8d54-4226-8d4e-d59eee97cb53">

下一步优化已有实验结果，并争取补充PG框架下的相关结果。


# 20231030周报

## 继续进行RB分配任务实验

目前画图遇到的困难：改变用户数和RB数后生成标签非常耗时，而标签质量下降会导致蒸馏效果显著恶化：

<img width="773" alt="1698625873934" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/e68a1a21-374e-4b6d-84f0-b30dd217f004">

关于标签质量与蒸馏效果的关系，可以考虑在discussion中进行描述

目前跑出了一部分标签数据，以下为用户数为10RB数为2时的蒸馏效果：

<img width="783" alt="1698625999777" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/bf91a6ec-9723-44bd-b510-96086142c023">



# 20231016周报

## 补充算法蒸馏RB分配任务实验，分别在PG和DPG框架下进行蒸馏

<img width="1007" alt="1697377447780" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/0b575578-bf9f-4d4e-b0ae-4129e93d6950">

需思考如何进一步丰富RB分配任务实验结果


# 20230918周报

## 本周工作：修改期刊论文，针对编辑的意见补充传统算法实验
补充了遗传算法实验，数据已经跑完。
仿真结果更新：

<img width="846" alt="1695003862976" src="https://github.com/UNIC-Lab/Weekly-Report/assets/63155472/e310a47a-3fb3-4de8-81c3-213bbab170ec">

由于传统算法推理时延较大，采用两套坐标进行绘图。

# 20230906周报

## 本周工作： 根据审稿意见修改论文，目前主要针对编辑的意见补充实验

审稿意见：

**副编辑评论**：

编辑：

1.利用边缘计算进行任务卸载是 4G 和 5G 的一个成熟课题。论文提到了 6G 网络的使用，但 6G 的定义或论文中使用的具体 6G 网络特征是什么？
```
增加相关解释，主要从任务的时延敏感性（特别是小任务情形），部署环境的多样性，需要考虑到算法本身的推理时延。
```

**2.根据 III.D 中定义的优化问题，这是一个典型的优化问题，其复杂性取决于用户规模。为什么需要使用神经网络算法的重型方法？与传统优化方案相比，其性能如何？这需要从一开始就加以解释，并在结果中对性能进行比较。**
```
尽管传统算法能够获得近似最优解，但复杂度较高，本文所用的神经网络模型复杂度明显低于传统算法。增加传统算法对比实验，目前增加了遗传算法(GA)进行对比。
```

3.关于公式 11 中定义的优化问题的表述，它将延迟和能量结合到同一个方程中。但它们具有不同的性质和单位规模。这就需要解释为什么方程中的组合能带来优化的解决方案，以及系统性能的哪一方面得到了优化。
```
本文所考虑系统性能的主要方面为用户服务时延，其次为系统的能量开销，两者的关注程度可通过改变权重系数来调整。
```

4.我不清楚使用什么数据来训练神经网络，以及从哪里获得这些数据。需要解释清楚。


5.使用强化学习算法存在混淆。你定义了奖励函数，但如何在强化学习算法中使用它？只显示公式 26 而不解释细节是不够的。强化学习采用迭代法，将结果收敛到最佳点。不需要训练。但您在论文中提到了强化学习算法的训练。这一点需要澄清。
```
修改相关表述，增加相关解释。本文所使用的RL训练方法是基于DPG架构而设计的。
```

**审稿人1：**

1.在相关著作中，作者只提到了 DL 方面的著作。除了同一作者撰写的另一篇论文 [1]，是否有任何关于 DyNN 的著作？

2.我仍然不清楚所提出的优化问题的解决方案。有很多参数需要优化。然而，算法 1 似乎只涉及两个输出参数。作者需要进一步解释优化问题是如何解决的。

3.优化问题似乎忽略了服务器的容量限制。然而，当任务负载极重时，服务器可能无法处理这种情况。

4.在模拟中，不清楚模拟参数是如何设置的。例如，为什么 \alpha=1 和 \beta=0.1 ？是否有任何参考文献可以提供？

5.作者在模拟中提出了两种情况。在 MEC 中，一个重要的特征或权衡是是否需要卸载一项任务。因此，情况 1，即所有任务都需要传输到服务器进行处理，也许毫无意义。

6.公式 10 中应解释 T^{MLP}_{j}。

7.在参考文献中，需要给出 "中国航空学报 "的缩写。
