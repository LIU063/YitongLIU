# 20230713周报

## 本周工作：
  
  1. wifi仿真建模:
    
    (1) 增加了扩展性实验： 模型迁移到不同ap数或不同ue数场景的性能

  ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/30def21d-1319-48b9-be19-9e0fe061a1c1)
  
  ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/ab71154e-757b-4c6a-a2a7-e30524dbd673)

     (2) 优化器参数已经确定, lr_scheduler参数还在调整, 现在存在过拟合问题。
  
  ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/464979b0-6a9b-433d-b7cd-c5ba3dbbe5d8)

  2. 修改wifi ppt:
     
  ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/a08a95cd-6c51-43f5-8351-2b183c4f287d)

  3. ADMM算法学习及UAV计算任务卸载场景调研：  

     J. Su, S. Yu, B. Li and Y. Ye, "[Distributed and Collective Intelligence for Computation Offloading in Aerial Edge Networks](https://ieeexplore.ieee.org/abstract/document/9745464)," in IEEE Transactions on Intelligent Transportation Systems, vol. 24, no. 7, pp. 7516-7526, July 2023, doi: 10.1109/TITS.2022.3160594.

问题场景：

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/c70b9f83-413d-452f-9cab-edf4a6c9e93d)

优化问题：所有地面用户设备的能源消耗最小

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/ebfbfa19-9a35-4b3e-a38c-8e847dc9ea40)

地面用户设备k的计算任务卸载的总能耗为：

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/2b2d1a08-0437-4c4e-8749-80afdf07758a)

通过增广拉格朗日乘子法，可以将问题分解

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/6fd46813-a5ce-4462-bf6d-097042e499f0)

利用迭代更新参数变量

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/16fcef37-dda4-4389-87bc-33d17118d87c)



## 下周工作 
  
  1. WIFI仿真添加全频率复用同时传输的对比方法，完善初步结果 PPT。
    
  2. 不动点算法 场景代码复现。
   

# 20230706周报

## 本周工作：
  
  1. wifi仿真建模:
  
  (1) 重写训练模块：
  
      利用dgl库中dgl.batch()和dgl.unbatch()代码。将图数据批量的输入模型，再计算loss时再拆成单图计算。
  
      利用batch大大降低了训练时间，也不用针对拼接的大图重写loss function。
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/bbca97fd-2c1e-43b5-90b9-2261f061e818)

  
  (2) 已将GNN中for循环计算改用矩阵运算，并降低模型推理时间。
     
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/132f1bc0-6aed-4b72-991c-4b9ed0ac1a94)

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/b6a18c90-c0a5-46ef-9e5d-9629538274df)

  (3) 模型调参，目前在修改模型宽度和优化器。
  
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/54303771-cd3f-4264-9516-a71d4e0d9a5d)


![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/0875a70a-ce94-4273-96e2-c5ff13d3460a)

  2. 已完成修改知识驱动综述文献物理层部分。

## 下周工作 
  
  1. WIFI仿真添加全频率复用同时传输的对比方法，修改初步结果PPT。
    
  2. 不动点算法调研：主要是ADMM算法在资源调度方向的paper，并学习ADMM算法的收敛性分析。
   

# 20230629周报

## 本周工作：
  
  1. wifi仿真建模: 已完善异构GNN设计部分，并跑出部分测试结果

     ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/f211aef2-5728-4bff-a35c-bdf821ef8060)

      ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/c320562f-e5f2-46f3-92bf-00a7bec6261f)

      ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/58a0536e-86be-45e1-a1e4-a470eba79114)
 
  2. 修改知识驱动综述文献物理层部分，目前还有Loss function一章需要完善。

## 下周工作 
  
  1. 将目前集中式的GNN改为分布式GNN.
     优化GNN模型，尽可能使用矩阵运行，避免循环查找，从而加快训练收敛收敛

  2. 修改知识驱动综述文献物理层部分

# 20230615周报
## 本周工作：
  
  1. 中期答辩工作准备
  
   之前的研究内容：![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/cd9fa034-da7e-42ea-bff0-667afb135d30)
   
   现在的研究内容：![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/0cdada1d-d53e-41f1-84a6-a5dcf782de3f)


  
  2. 完成知识驱动magazine的模型图
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/96988a76-1371-4949-8779-ea97e0ece157)

  3. wifi仿真建模: 异构GNN已经能跑出数据，但测试集效果不好，目前在调参
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/06c01b2c-be1d-43ea-b8db-79fa3d0ea948)

## 下周工作 
  
  1. 完善GNN设计部分，并训练测试
  2. 修改知识驱动综述文献物理层部分

# 20230608周报

## 本周工作：
  
  1. GNN论文修改并投递 
  
  3. 知识驱动综述文献物理层部分: 完成初稿撰写，目前在修改文献描述
 
  2. wifi仿真建模: 构建异构图神经网络 和 DGL数据集

## 下周工作 
  
  1.完善GNN设计部分，并训练测试


# 20230524周报

## 本周工作：
  
  1. 撰写知识驱动综述文献物理层部分
 
  2. wifi仿真建模: 构建环境通信图环境和传统退避重传的wifi通信
  
  通信图数据结构：[gdata.py](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-4/Hao-Yang/code/wifi%20demo/gdata.py)
  
  ![Figure_1](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/2d978b3d-c34e-43a1-a697-4e222939c602)
  
  退避重传的wifi通信实验结果 [test.py](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-4/Hao-Yang/code/wifi%20demo/test.py)
  
  ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/04a9a42a-a3ff-4621-95fe-d2e0c524b8d3)


## 下周工作 
  
  1.完善WiFi仿真方案，设计GNN训练部分
  

# 20230517周报

## 本周工作：
  
  1. wifi仿真建模
  
  [仿真环境调研-ns3(https://github.com/UNIC-Lab/Weekly-Report/2023-Spring/Group-4/Hao-Yang/picture/ns3.md)
  ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/3d812944-59ac-458c-9dbd-e5027b5fe337)
  ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/d79c8f5e-f4a8-4ad5-b0fa-a9432b24a3fc)
  
  仿真对比设计：(1)分频通信 (2)频率复用
  
  2. 撰写知识驱动综述文献物理层部分
  
## 下周工作 
  
  1.完善WiFi仿真方案，设计初步实验环境
  
  2.继续撰写知识驱动综述文献物理层部分。



# 20230510周报

## 本周工作：

1. 修改论文。

3. 调研wifi仿真建模
![image](./picture/2023-05-11_070907.jpg) 
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/922366dd-0ec9-47c7-890f-8f431e7b524b)

- 1 [matlab 产生WiFi信号](https://blog.csdn.net/Winds_Up/article/details/113762177)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/6a9e9529-33a9-4ead-8613-75f0f43948be)
- 2 wirelessWaveformGenerator
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/ebd1d8b0-ee09-4797-9584-4d94e94c9f3f)

使用此应用程序，可以产生如下无线信号及应用：

（1）生成自定义的OFDM、QAM和PSK调制波形。

（2）产生正弦波测试波形。

（3）生成WLAN（802.11™) 调制波形。此功能需要WLAN工具箱。

（4）生成LTE调制波形。此功能需要LTE工具箱。

（5）通过添加射频损伤（如AWGN、相位偏移、频率偏移、直流偏移、IQ不平衡和无记忆三次非线性）来扭曲波形。

（6）在星座图、频谱分析仪、OFDM网格和时间范围图中可视化波形。

（7）将波形导出到工作区或文件。
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/a6be6814-b3d3-4a49-b137-1ee11450c666)

- 3 openwifi硬件仿真 [https://github.com/open-sdr/openwifi](https://github.com/open-sdr/openwifi)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/1f6d9331-7d8c-42c7-a073-77955da179e6)
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/90384476/7349df8c-e0ba-4541-a00e-d832573efaf2)


3. 撰写知识驱动综述文献物理层部分

## 下周工作 

  继续撰写知识驱动综述文献物理层部分。
  
# 20230503周报

## 本周工作：

1. 修改论文摘要，重画样本数据图，删去最后一个实验。
![image](https://user-images.githubusercontent.com/90384476/236106548-a368285a-6f2a-4b99-bcf0-3eb2cd261703.png)


2. 撰写知识驱动综述文献物理层部分

## 下周工作 

  继续撰写知识驱动综述文献物理层部分。
  
# 20230419周报

## 本周工作：

1. 修改论文，重画场景图，修改摘要  [论文链接](https://cn.overleaf.com/read/hcqfjvdbjdck "Graph Neural Network based D2D Resources Management: An Unrolling-Driven Method")

2. 撰写知识驱动综述文献物理层部分

![image](https://user-images.githubusercontent.com/90384476/232952436-784401e0-dc89-49e9-83ed-df73ecc2e9f7.png)

3. 整理[GPT Prompt Tips](https://github.com/UNIC-Lab/Weekly-Report/blob/main/Miscellaneous/GPT-Academic%20Writting/Prompt%20Tips.md) 

## 下周工作 

  继续撰写知识驱动综述文献物理层部分。
  
# 20230412周报
## 本周工作：

1. 修改论文全文细节

   (1)重写了WMMSE介绍，减少了中间问题公司，压缩文章篇幅。
   
   (2)撰写论文摘要

   版本1：The allocation of network resources in the future requires high timeliness, which the traditional iterative optimization algorithms do not satisfy due to latency constraints. The advent of neural networks presents a viable solution for the timely resolution of NP-hard wireless resource allocation problems. Nonetheless, current neural networks suffer from inadequate generalization and poor interpretability. Consequently, knowledge-driven neural networks represent a promising solution. By integrating domain expert knowledge, the inference ambiguity in neural networks and random exploration space are minimized, resulting in improved model generalization and interpretability. This paper proposes a novel architecture for graph neural networks (GNNs), referred to as the unrolling WMMSE algorithm graph neural networks (UWGNN), to address the power control problem in N-user interference channels. The UWGNN architecture is knowledge-driven by algorithmic unrolling of the iterative weighted minimum mean squared error (WMMSE) method. Specifically, each GNN module corresponds to a segment of the WMMSE algorithm formulation, enabling a single layer of the neural network to align with one iteration of the algorithm. The unrolling method is demonstrated to be effective, and a neural network model parameter migration method is proposed for the iterative optimization problem. Experimental results indicate that UWGNN effectively captures the WMMSE iterative structure, facilitating faster convergence, better scalability, and lower sample complexity. Furthermore, UWGNN exhibits excellent generalization performance when dealing with diverse data distributions and communication topologies without requiring retraining. Moreover, The proposed parameter migration method enables on-demand reduction of communication network resource allocation delay.
   
   版本2：This study investigates a novel approach for managing radio resources in Device-to-Device (D2D) networks using a Graph Neural Network (GNN) model architecture, inspired by the unrolling of the Weighted Minimum Mean Square Error (WMMSE) algorithm. Addressing the limitations of existing algorithms in meeting the millisecond-level timeliness and scalability required for emerging intelligent services, our proposed method incorporates the WMMSE algorithm’s structure and domain knowledge, thereby reducing computational delay and sample complexity while adapting to various data distributions. We present the UWMMSE-GGNN, a GNN architecture that employs the summation and power calculation components of the WMMSE algorithm to design the aggregation and update functions of the GNN, enhancing model generalization and interpretability. Theoretical analysis and simulation results demonstrate the robustness, scalability, and strong performance of the proposed architecture across diverse communication topologies without retraining. Our findings contribute to the development of efficient and scalable wireless resource management solutions for intelligent industries.
   
   版本3：In this paper, a novel graph neural network based on unrolling WMMSE algorithm (UWGNN) is proposed to address the problem of power control in wireless communication systems. Traditional iterative optimization algorithms cannot satisfy the millisecond-level execution time and scalability requirements. By incorporating the structure of the WMMSE algorithm and related domain knowledge into the neural network, model generalization and interpretability are improved. Each GNN module in the proposed network structure corresponds to a fragment of the WMMSE algorithm formula, thus enabling each layer of the network to correspond to one iteration of the algorithm. Experimental results demonstrate that the proposed algorithm effectively captures the WMMSE iteration structure, accelerates the convergence rate, improves scalability and reduces sample complexity, and can handle different data distributions and communication topologies. Moreover, the proposed algorithm exhibits excellent generalization and scalability, and enables instant reduction in communication network resource allocation latency.
   
2. 调研不动点网络论文
 
 ![image](./picture/2023-04-12_185443.jpg) 
   
## 下周工作 

  撰写知识驱动综述文献物理层部分。
  
# 20230405周报
## 本周工作：

1. 修改论文全文逻辑

  （1）intro部分修改
  
  ![image](./picture/2023-04-05_1.jpg) 
  
  ![image](./picture/2023-04-05_2.jpg)  
  （2）修改实验部分：描述+结论
  
2. 整理知识驱动综述文献，按照孙老师要求，细化文献分类，补充部分章节文献

   ![image](./picture/2023-04-05_232716.jpg)  
 
3. 修改gpt插件代码，新增功能模块

![image](./picture/2023-04-05_232616.jpg)

原文摘要： The use of terahertz (THz) frequencies has been recommended to achieve high-speed and ultra-low latency transmissions. Although there exist very large bandwidths in the THz frequency bands, THz channels are significantly dynamic and complicated, which is challenging for channel estimation. To improve the energy efficiency of wireless networks, THz channel power gains need to be precisely evaluated for determining optimal THz transmission frequencies and power control. Therefore, this work presents a novel conditional generative adversarial networks (GAN) based channel power gain estimation solution in the THz vehicle-to-infrastructure (V2I) networks with leakywave antennas, where the THz frequency has a big effect on the antenna gain, path loss and atmospheric attenuation. Simulation results confirm that our solution can accurately estimate the channel power gains versus the THz frequencies at a fast speed.

生成摘要： This article discusses the potential of using terahertz (THz) transmission for wireless communication and the challenges faced in implementing traditional antenna arrays in THz systems. The use of leaky-wave antennas is proposed for efficient channel estimation and power control. The article proposes a new GAN-based channel power gain estimation framework for THz vehicle-to-infrastructure (V2I) networks, which leverages received signal strengths (RSSs) as the conditional information. The proposed solution overcomes the drawbacks of Doppler shift and conventional methods that depend on state information in the prior time. The results confirm the accuracy and fast convergence speed of the proposed solution. The proposed solution has the potential to revolutionize the wireless communication industry and pave the way for the next-generation radio technology.
## 下周工作安排：

1. 撰写知识驱动综述文献第七章：物理层部分。

2. 根据不动点网络特性，寻找通信模型。

 
 # 20230329周报
## 本周工作：
1. 整理知识驱动综述文献，按照知识驱动方式对通信物理层的80篇文献进行了分类。
2. 修改论文第二、三章
3. 对智能wifi系统建模

  ![image](./picture/智能wifi.jpg) 
  
5. 与本科生讨论，无人机网络计算卸载模型，思考不动点网络具体应用方式
## 下周工作安排：
1. 修改论文第五章实验部分，修改图片描述，扩充实验结论

# 20230322周报
## 本周工作：
1.修改论文

（1）修改第四章证明过程。

  学习端到端映射困难，unroll将一步映射展开为多步映射，降低模型学习难度
  
![image](./picture/2023-03-21_110640.jpg)

  unroll 收敛方向与算法一致，增加了特征相关性
  
![image](./picture/2023-03-21_112147.jpg)

（2）修改场景与网络拓扑结构图

![image](./picture/2023-03-21_150606.jpg)

（3）重画实验图

2. 阅读不动点网络相关文献

   [Yu W, Shen Y, He H, et al. An Adaptive and Robust Deep Learning Framework for THz Ultra-Massive MIMO Channel Estimation[J]. arXiv preprint arXiv:2211.15939, 2022.](https://arxiv.org/abs/2211.15939)
   
   本文将符合压缩感知理论的迭代算法，拆成线性部分与非线性部分，利用神经网络替换非线性部分，只需满足Lipschitz常数小于1，即可从数学上证明不动点网络的收敛性。
   ![image](./picture/2023-03-21_114633.jpg)
   
   ![image](./picture/2023-03-21_114257.jpg)
  ## 下周工作安排：
  
  1. 进一步完善论文
  2. 思考不动点网络的通信应用场景，构建数学模型。 
  
  ## 6G大会-论坛F:6G通感算架构及关键技术20230324
 
  1.未来通感算典型特征：

  一是多要素深度融合。多要素深层次融合以实现感知维度的拓展、通讯的效率提升、算力的泛在化

  二是多频段的协同。低、中、高多频段协同是实现我们宏观广覆盖、探测与微观重点感知相互补充与增强。

  三是网络协作的通感算。利用移动通讯网络中大量部署的节点来进行协作，可进一步扩大感知范围，实现连续覆盖，并可利用快速的联合处理来实现及时的感知精度提升。

  2.未来研究挑战：

  一是通感算融合理论的研究：
  如何以合适的指标来表征融合的效果，如何平衡通讯容量、感知性能、计算能力之间的关系，需要进一步的理论研究来支撑。

  二是通感算融合网络的架构设计：
  通感算融合网络系统架构涵盖了物理基础设施层、逻辑功能层和应用层三层，将受到网络统一的编排和管理。

  三是通感算空口融合的设计方面：
  空口设计关乎通感算网络的极致性能实现，在融合波形结构参考信号、波束赋形及波束管理等方面，需要结合多元化的应用场景、业务、优先级业务需业务量的需求来灵活设计。

  四是通感算组合的融合设计方面：
  需要综合考虑低、中、高、多频段衰落特性、通讯能力、感知能力等，构建各频段互补与增强的全谱融合的同感杆网络，实现广覆盖探测，以围观精准感知。对于目标、对于网络协作的通感算，还需要从系统性能、复杂度等角度出发，持续优化组网的资源配置，降低组网干扰的不利影响。

  五是通感算硬件结构的设计：
  当前通感算融合网络在采用单节点感知时仍面临自干扰的挑战，能否突破该技术对通感算融合网络下的基站形态将产生重要的影响。
  
 
  
