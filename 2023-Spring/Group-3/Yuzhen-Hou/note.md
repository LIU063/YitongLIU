## Week 1 (2023.3.16 – 2023.3.22)

### Work

1. Actor-Critic 算法与 HER 经验回放寄存类编写，具体算法流程如下：

    <div align="center">
        <img src="./assets/img/week1_hindsight_experience_replay_algorithm.png" style="width:40em; margin:1vh auto;" alt="hindsight_experience_replay_algorithm" />
    </div>

    在以上算法流程中将 off-policy RL 算法用 actor-critic 进行了 HER 寄存器的替代实现。

2. 查阅参考文献 [*Sim and Real: Better Together*](https://arxiv.org/abs/2110.00445) 中并行训练逻辑的[代码实现](https://github.com/sdicastro/SimAndRealBetterTogether/tree/main/mpi_utils)（基于 MPI 并行计算库的实现），并参考[文档](https://materials.jeremybejarano.com/MPIwithPython/index.html)使用 MPI 接口进行了基本的进程数据通信功能测试，主要实现同步数据传输与基本计算功能，下周将对并行梯度下降进行实现。

### Plan

1. 实现基于多经验回放寄存器的 DQN/A2C 算法实现，并先对纯模拟环境进行训练代码运行，并观察训练结果

2. 实现基于 MPI 的并行梯度下降方法与 HER 寄存器接口实现

------

## Week 2 (2023.3.23 – 2023.3.29)

### Work

1. 收看全球 6G 技术大会

    - 2023-3-22

        > **论坛 B：天地融合智能组网技术**
        >
        > 陈山枝 —— 6G 及星地融合移动通信发展趋势
        >
        > - 6G 时代的数字孪生、虚拟世界、元宇宙、数字中国，以及未来的数字地球，都需要实现全域覆盖
        >
        > - 6G 两个标志：1) 星地融合		2) 用户为中心
        >
        > - 卫星高速移动带来的问题：
        >
        >     1）传播距离、时延对于信号波形、传输的影响 —— 如何信道建模、链路和系统评估方案、链路预算；
        >
        >     2）网络架构从平面架构到三维立体架构的重新设计 —— 考虑立体的、弹性的可存扩网络，包括引入 AI 模型解决；
        >
        >     3）高低轨卫星之间的干扰问题 —— 频率复用、物理层的关键技术和高层的关键技术

    - 2023-3-23

        > **论坛 C：双碳下的6G网络覆盖**
        >
        > 牛志升 —— 基于超蜂窝架构的柔性覆盖
        >
        > - 6G 低能耗需求与当前支持网络流量 KPI 增长百倍的技术之间存在矛盾，需要提出新的发展模式
        >
        > - 移动通信必须要改变 “按照最坏情况来设计网络覆盖” 的模式，降低整体能耗而非只提高能量效率
        >
        > - 6G 移动基站与边缘服务器的大量部署带来的能耗问题需要提出权衡策略，其中包括：
        >
        >     1）需要将基站的功率消耗设计为按业务动态变化的方式，如何降低功耗或关闭部分基站的同时保证保证全域覆盖；
        >
        >     2）如何定义业务变化；
        >
        >     3）如何保证服务质量
        >
        > - 超蜂窝网架构 —— 实现控制覆盖和业务覆盖分离，以业务覆盖控制降低能耗

    - 2023-3-24

        > **论坛 F：6G通感算架构及关键技术**
        >
        > 欧阳晔 —— 算力内生的通算一体化网络
        >
        > - 通算一体 “算力内生网络” 六大关键技术：通算一体的虚拟化、MEC 边缘卸载、网络无损、算法体系算力内生联邦学习、网络数字孪生面向算力内生网络的实现
        > - 追求设备运营商与网络 “空闲算力” 最大化利用的平衡

2. 高德/百度地图 API 调用研究，基于此实现南北校区间定时请求最短驾车时间

    - 正在针对高德地图 API 定时不精准问题和早晚高峰期路线规划不更改的问题进行资料查阅与问题定位，目前针对所有策略不同的网络请求均尝试过，开放 API 目前普遍存在该问题。

3. 毕设论文的算法实现工作：

    - 完成了 DQN 算法的所有实现编写

    - 对强化学习的状态/动作空间、环境定义、回放寄存进行了代码重构，完成了学习方法类、环境类与寄存器类的解耦；添加了空间的属性动态注册方法（[Github 仓库：UAV_RL](https://github.com/ccdf846153/UAV_RL)）

        > 【代码结构】
        >
        > ```
        > ./
        > │  train.py			    // UAVAgent
        > │  user_loc.npy
        > ├--modules
        > │  │  Net.py			    // Net(nn.Module)
        > │  └--RL.py			    // ReinforcementLearning @abstractclass, DQN
        > ├--utils
        > │  │  buffer.py	                    // ReplayBuffer
        > │  │  env.py			    // UAVEnvironment
        > │  │  env_args.py		    // arg_parse
        > │  │  env_core.py		    // Env @abstractclass
        > │  └--space.py		   	    // Space @abstractclass, ActionSpace, StateSpace
        > └--train_result
        >     │  DQN_model_parameters__2023-03-29_19-48-20.pth
        >     │  rate_list__2023-03-29_19-48-20.npy
        >     └--reward_list__2023-03-29_19-48-20.npy
        > ```
        >
        > 【智能体定义】
        >
        > ``` python
        > class UAVAgent:
        >     def __init__(
        >         self, 
        >         env_list: List[UAVEnvironment],
        >         algorithm: str = 'DQN',
        >         interact_distrib: List[float] = [0.1, 0.9],
        >         sample_distrib: List[float] = [0.5, 0.5]
        >     ):
        >         __slots__ = [
        >             'env_list', 'state_space', 'action_space',
        >             'model', 'interact_distrib', 'sample_distrib',
        >             'num_envs', 'algorithm'
        >         ]
        > ```
        >
        > 【DQN 定义】
        >
        > ``` python
        > self.model: ReinforcementLearning = eval(algorithm)(
        >     state_space = self.state_space,
        >     action_space = self.action_space,
        >     eval_net = Net(
        >         len(self.state_space),
        >         len(self.action_space)
        >     ),
        >     target_net = Net(
        >         len(self.state_space),
        >         len(self.action_space)
        >     ),
        >     gamma = 0.9,
        >     loss_function = nn.MSELoss(),
        >     optim_info = {
        >         'net': 'eval_net',
        >         'type': 'Adam',
        >         'lr': LR
        >     },
        >     buffer_info = {
        >         'type': 'ReplayBuffer',
        >         'capacity': MEMORY_CAPACITY(2000),
        >         'num': len(self.env_list)
        >     }
        > ```

    - 目前正在运行针对一个模拟环境、一个真实环境时，基于分离经验回放寄存器的 DQN 算法

### Plan

1. 针对毕设算法运行结果进行超参数调整与性能分析；改变抽样分布与环境选择分布后进行算法性能对比

