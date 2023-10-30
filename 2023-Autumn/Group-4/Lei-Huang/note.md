# week 10.23-10.27  
1. 写6G全场景按需服务架构章节内容
2. 写知识意图双驱动的6G全场景按需服务架构专利  

# week 10.9-10.15
## 继续建模  
### 根据大小时间尺度确定两个子问题   
![问题建模](https://github.com/loafluls/report_images/blob/main/%E9%97%AE%E9%A2%98%E5%BB%BA%E6%A8%A1%E5%9B%BE/%E9%97%AE%E9%A2%98%E5%BB%BA%E6%A8%A1.jpg)   
![大](https://github.com/loafluls/report_images/blob/main/%E9%97%AE%E9%A2%98%E5%BB%BA%E6%A8%A1%E5%9B%BE/%E5%A4%A7%E5%B0%BA%E5%BA%A6.jpg)   
![小](https://github.com/loafluls/report_images/blob/main/%E9%97%AE%E9%A2%98%E5%BB%BA%E6%A8%A1%E5%9B%BE/%E5%B0%8F%E5%B0%BA%E5%BA%A6.jpg)  
利用二元函数判断凹凸性的方法可证明小时间尺度问题是非凸的，采用传统迭代方法进行解决

## 本周工作安排
1. 将小尺度问题进行简化，找出闭式解，半闭式解或者最优解
2. 继续阅读论文，找寻有无更好地改进算法架构的方法，能更多或者更明显地提升系统的性能
![问题建模](https://github.com/loafluls/report_images/blob/main/%E9%97%AE%E9%A2%98%E5%BB%BA%E6%A8%A1%E5%9B%BE/H-ppo%E6%9E%B6%E6%9E%84%E5%9B%BE.jpg) 

# week 2
## 继续建模  
### 1.调研大小时间尺度如何运作，确定两个子问题    
### 2.阅读文献  
#### 2.1大小时间尺度  
##### [1]D. Liu, J. Zhao, C. Yang and L. Hanzo, "Accelerating Deep Reinforcement Learning With the Aid of Partial Model: Energy-Efficient Predictive Video Streaming," in IEEE Transactions on Wireless Communications, vol. 20, no. 6, pp. 3734-3748, June 2021, doi: 10.1109/TWC.2021.3053319.
##### [2]Z. Jing, Q. Yang, M. Qin, J. Li and K. S. Kwak, "Long-Term Max-Min Fairness Guarantee Mechanism for Integrated Multi-RAT and MEC Networks," in IEEE Transactions on Vehicular Technology, vol. 70, no. 3, pp. 2478-2492, March 2021, doi: 10.1109/TVT.2021.3059944.
#### 2.2 时隙 (key word: Lyapunov+delay+RL)  
##### [1]F. Zhou, L. Feng, M. Kadoch, P. Yu, W. Li and Z. Wang, "Multiagent RL Aided Task Offloading and Resource Management in Wi-Fi 6 and 5G Coexisting Industrial Wireless Environment," in IEEE Transactions on Industrial Informatics, vol. 18, no. 5, pp. 2923-2933, May 2022, doi: 10.1109/TII.2021.3106973.
##### [2]Adaptive and Robust Network Routing Based on Deep Reinforcement Learning with Lyapunov Optimization
##### [3]Reinforcement Learning Neural Network-Based Adaptive Control for State and Input Time-Delayed Wheeled Mobile Robots

## 下周工作安排
1. 阅读论文
#### [1]D. Han et al., "Two-Timescale Learning-Based Task Offloading for Remote IoT in Integrated Satellite–Terrestrial Networks," in IEEE Internet of Things Journal, vol. 10, no. 12, pp. 10131-10145, 15 June15, 2023, doi: 10.1109/JIOT.2023.3237209.  
#### [2]Q. Ye, W. Shi, K. Qu, H. He, W. Zhuang and X. Shen, "Joint RAN Slicing and Computation Offloading for Autonomous Vehicular Networks: A Learning-Assisted Hierarchical Approach," in IEEE Open Journal of Vehicular Technology, vol. 2, pp. 272-288, 2021, doi: 10.1109/OJVT.2021.3089083.
2. 与老师讨论运作机理

# Week 1
## 建模公式: 
<https://www.overleaf.com/read/dkrgpzbmqqkw>  
开始写环境部分代码
## 本周工作安排
继续代码编写，先完成没有知识引入的版本
