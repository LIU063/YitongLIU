## Week 1 (2023.3.16 – 2023.3.22)

### Work

1. Actor-Critic 算法与 HER 经验回放寄存类编写，具体算法流程如下：

    <img src="./assets/img/week1_hindsight_experience_replay_algorithm.png" style="width: 40em; margin: 1vh auto;" alt="hindsight_experience_replay_algorithm" />

    在以上算法流程中将 off-policy RL 算法用 actor-critic 进行了 HER 寄存器的替代实现。

2. 查阅参考文献 [*Sim and Real: Better Together*](https://arxiv.org/abs/2110.00445) 中并行训练逻辑的[代码实现](https://github.com/sdicastro/SimAndRealBetterTogether/tree/main/mpi_utils)（基于 MPI 并行计算库的实现），并参考[文档](https://materials.jeremybejarano.com/MPIwithPython/index.html)使用 MPI 接口进行了基本的进程数据通信功能测试，主要实现同步数据传输与基本计算功能，下周将对并行梯度下降进行实现。

### Plan

1. 实现基于多经验回放寄存器的 DQN/A2C 算法实现，并先对纯模拟环境进行训练代码运行，并观察训练结果

2. 实现基于 MPI 的并行梯度下降方法与 HER 寄存器接口实现

