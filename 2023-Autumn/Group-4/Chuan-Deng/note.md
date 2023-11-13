# 20231009周报
## 本周进展：
**1**.完成李沐课程的学习并回顾相关代码   
**2**.阅读gnn的综述   
**3**.进行凸优化算法的学习   
## 困难和解决办法
**问题**：因为李沐的课程中没有涉及gnn的讲解，所以看gnn综述的时候更像是囫囵吞枣，没办法深入理解    
**解决办法**：找到了gnn的博客和b站上李宏毅的gnn讲解视频进行学习    

# 20231030周报
**1**.进行凸优化课程的学习      
**2**.进行通感一体化研究方向的调研     

# 20231107周报
**1**.继续凸优化课程的学习
**2**.进行Radio map-aided研究方向的调研    

# 20231113周报   
&ensp;&ensp;联合通信和雷达/无线电传感(JCAS)是一种将通信和传感集成到一个系统中的有吸引力的解决方案。它也被称为不同的术语，如Radar-communications (RadCom),joint radar (and) communications (JRC)，joint communications (and)radar (JCR)，dual-function(al) radar communications (DFRC)，integrated sensing and communications (ISAC)。

&ensp;&ensp;根据[1]在2010年之前，国内系统对JCAS的研究有限。在过去的十年中，JCAS的研究既基于简单的点对点通信，如车载网络[2]、[3]、[4]，[5]、[6]也基于复杂的移动/蜂窝网络[7]、[8]。前者可以在自动驾驶中找到很好的应用，而后者可能会彻底改变当前仅用于通信的移动网络。    

    [1] J. A. Zhang et al., "Enabling Joint Communication and Radar Sensing in Mobile Networks—A Survey," in IEEE Communications Surveys & Tutorials, vol. 24, no. 1, pp. 306-345, Firstquarter 2022, doi: 10.1109/COMST.2021.3122519.
    [2] F. Liu, W. Yuan, C. Masouros and J. Yuan, "Radar-Assisted Predictive Beamforming for Vehicular Links: Communication Served by Sensing," in IEEE Transactions on Wireless Communications, vol. 19, no. 11, pp. 7704-7719, Nov. 2020, doi: 10.1109/TWC.2020.3015735.    
&ensp;&ensp;[2]提出了一个extended Kalman filtering (EKF)框架，该框架建立在回波信号的测量和车辆的状态演化模型之上。为了在保证下行quality-of-service (QoS)的同时最小化多车在卡尔曼迭代中的跟踪误差，提出了一种基于优化的功率分配方案，该方案在给定的和速率阈值和功率预算下，最小化角度估计和距离估计的后交cramsamr-rao界(PCRB)。能够最小化，从而以实现可达到的最大传输速率。  

    [3] W. Yuan, F. Liu, C. Masouros, J. Yuan, D. W. K. Ng and N. González-Prelcic, "Bayesian Predictive Beamforming for Vehicular Networks: A Low-Overhead Joint Radar-Communication Approach," in IEEE Transactions on Wireless Communications, vol. 20, no. 3, pp. 1442-1456, March 2021, doi: 10.1109/TWC.2020.3033776. 
&ensp;&ensp;[3]中出了一种新的基于dual-functional radar-communication(DFRC)的车用网络波束形成方案，它只需要很低的信号开销来进行波束跟踪。从贝叶斯的角度出发，基于RSU(roadside unit)接收到的回波信号和车辆的状态转移模型，构建了联合后验分布。对联合分布进行充分分解，用因子图表示，利用消息传递算法对未知变量进行估计。采用二阶泰勒展开式逼近非线性反三角函数。因此，因子图上的消息以封闭形式确定，为所考虑的波束跟踪问题提供了低复杂度的解决方案。   

    [4] Junsheng Mu, Integrated Sensing and Communication-Enabled Predictive Beamforming With Deep Learning in Vehicular Networks.CL 2021. [5] M. L. Rahman, J. A. Zhang, X. Huang, Y. J. Guo, and R. W. Heath Jr.,“Framework for a perceptive mobile network using joint communication and radar sensing,” IEEE Trans. Aerosp. Electron. Syst., vol. 56, no. 3, pp. 1926–1941, Jun. 2020.    
&ensp;&ensp;[4]中建立了一个由三层全连接层搭建的神经网络，从反射信号样本中提取车辆的历史角度信息。然后，预测了车辆下一时刻的angel of arrival（AoA）信息，再利用预测得到的AoA信息并设计了波束形成器，使其与AoA对齐，以实现可达到的最大传输速率。  

    [5] C. Liu et al., "Learning-Based Predictive Beamforming for Integrated Sensing and Communication in Vehicular Networks," in IEEE Journal on Selected Areas in Communications, vol. 40, no. 8, pp. 2317-2334, Aug. 2022, doi: 10.1109/JSAC.2022.3180803.
&ensp;&ensp;[5]提出了一种基于深度学习的预测波束形成框架，设计了一个HCL-Net，HCL-Net采用了卷积LSTM结构，进一步提高了波束形成性能。  

    [6] Zihuan Wang; Vincent W.S. Wong, Deep Learning for ISAC-Enabled End-to-End Predictive Beamforming in Vehicular Networks, ICC 2023.   
    
&ensp;&ensp;在[6]中开发了一种端到端的预测波束形成方法：ISAC-enabled end-to-end(E2E-PB)，即搭建了一个基于注意力机制的LSTM网络，与[3]的不同之处在于网络输入是提取是波束形成器形前τ时隙接收信号样本的特征，输出直接就是波束形成矢量，相当于绕过了参数估计部分减少了误差的引入，提升了性能。  
<div align=center><img width="500" alt="1699858274063" src="https://github.com/UNIC-Lab/Weekly-Report/assets/130338829/7b6ae13b-58e7-4b60-9912-7cbab63b2467">
<div align=center><img width="500" alt="1699858536697" src="https://github.com/UNIC-Lab/Weekly-Report/assets/130338829/0710e805-7383-4974-940f-2e2679f36d50">   
    
wn是波束形成矢量；hn为RSU与车辆在n时隙的通道矢量。σ^2表示复高斯分布噪声的方差。


    [7] M. L. Rahman, J. A. Zhang, X. Huang, Y. J. Guo and R. W. Heath, "Framework for a Perceptive Mobile Network Using Joint Communication and Radar Sensing," in IEEE Transactions on Aerospace and Electronic Systems, vol. 56, no. 3, pp. 1926-1941, June 2020, doi: 10.1109/TAES.2019.2939611.     
    [8] J. Andrew Zhang, PERCEPTIVE MOBILE NETWORKS Cellular Networks With Radio Vision via Joint Communication and Radar Sensing, IEEE VEHICULAR TECHNOLOGY MAGAZINE.

<p align="left">&ensp;&ensp;感知移动网络中感知参数提取的第一个挑战是由于其复杂的信号结构。针对现代移动网络开发的信道估计技术主要集中在信道系数的估计上，而不是以感知参数为代表的详细信道组成。此外，传统的频谱分析和阵列信号处理技术(如MUSIC和ESPRIT)需要连续观测，这在这里并不总是可用的。因此，需要开发新的传感技术，从复杂和碎片化的信号中估计感知参数。<p>

<p align="left">&ensp;&ensp;感知参数估计的第二个挑战来自于移动网络中的丰富多径。大多数感知参数估计算法只能处理包含有限数量多径信号的信号。在感知移动网络中，我们将杂波定义为包含很少新信息的不需要的多径信号。因此杂波主要是指在传感装置的发射端和接收端都是静态的情况下，来自永久或长周期静态物体的多径信号。由于不同的信号的传播环境、抑制要求和适用的感知算法不同，现有雷达系统的杂波抑制技术，大多是在感知算法之后应用的，因此无法达到减少感知算法多径输入的目的。<p>



