### 2023.3.22
# 1.场景建模
  合法用户接入到卫星时接收到的信号：y=有用信号+干扰+噪声 
  
  卫星信道：雨水衰减+路径损耗+卫星波束增益
$$h=\sqrt{C_Lb\beta}\exp \left( -j\theta \right)$$
其中
$$C_L=\left( \lambda /4\pi \right) ^2/\left( d^2+h^2 \right)$$
$$b=G\left( \frac{J_1\left( u_0 \right)}{2u_0}-36\frac{J_3\left( u_0 \right)}{u_{0}^{2}} \right) ^2$$
β为对数正态随机变量，服从正态分布  
  
  基站信道：   
$$g=\sqrt{\alpha}g_0$$
$$\alpha =C_0r^{-4}$$
其中 g0服从Nakagami-m分布  
无人机信道： 
$$a=\sqrt{G_L}\left( \sqrt{\frac{K}{K+1}}a_{LoS}+\sqrt{\frac{1}{K+1}}a_{Ray} \right)$$  
$$G_L=\frac{g_0}{U_{d}^{2}+U_{h}^{2}}$$
          a_los服从莱斯分布  a_ray服从瑞利分布  
          
在这个基础上，通过matlab仿真，得到信道状态信息
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/channel.jpg)
# 2.开题答辩
  撰写开题报告5000字，完成开题答辩。
# 3.学习调研
   学习b站视频《跟李沐学ai》,看完1/3，复习线性回归、神经网络等基础知识。学习DQN算法，跑通并读懂DQN最常见的应用车杆游戏的代码。
# 4.下一周计划
   完成优化功率分配的代码，完成DQN的大部分内容。
   

