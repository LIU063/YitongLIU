# 语义通信中用户侧定制化decoder设计

在基于深度学习的语义通信系统中，常用到基于transformer的en-decoder架构。用encoder实现源数据的语义信息提取，用decoder对语义信息进行恢复。
然而这样一套系统能够work-well，常常需要decoder具有充足的先验知识，能够对网络中传输的各种各样的数据进行理解。
但是网络中的数据复杂多样，想要设计训练一个“全知型”的decoder，必然会很困难。而即使是做出来了，也必然会有庞大的模型参数体量及推理时延，不适合部署于移动设备，也不适合像通信这类时延敏感性应用。
因此根据每一个用户的历史通信数据、(CSI)等，为每一个用户训练一个定制化的decoder是必然趋势。

考虑到训练需要用到用户的历史通信数据、(CSI)等敏感信息，因此我们采用联邦学习范式，将模型的训练任务放在用户侧。
训练时，用户将decoder根据自己最新的数据进行微调或迁移（或其他个性化的手段），而encoder始终保持不变。
local training结束后，被调度到的用户做一次aggregation。

# Attention-based Knowledge Fusion for Decentralized Federated Distillation.

![去中心化蒸馏](./assets/蒸馏.png)

在知识蒸馏中，通常认为Teacher Model比Student Model具有更多的知识。然而在去中心化的设定下，各个节点的地位相等，所训练的模型及所使用的数据集有大有小，各个节点的数据集分布也不相同。导致有时邻居节点的local model对于某一类别的知识可能不如自己的model，这时就不适合将其作为自己teacher model。

例如图中Node2、Node3的数据集比较小，对于类别2的数据含量也比较少。因此其local model对于类别2的数据的分类能力比较弱，强行进行蒸馏的话反而会误导Node1的local model。因此在进行蒸馏时，需要对多个teacher的软标签进行鉴别。

我们第一种直接的方法是对来自多个teacher的软标签进行加权平均，根据各个teacher的数据集分布确定软标签的权重。这种方法可以作为一个baseline，但是它存在两方面的问题：
1. 仅根据数据集分布可能并不能反映出teacher model的知识。因为来自邻居节点的teacher model在训练时还会从它自己的邻居那里蒸馏不属于自己的知识。
2. 这种方法无法考虑到不同节点间模型的异构问题。

因此，我们第二种方法考虑在蒸馏时对软标签的聚合加入注意力机制，将attention value作为各个软标签聚合的权重，使得模型能够在蒸馏时自己学出来各个权重值。具体来说：
1. Node1为其每个邻居节点训练软标签的V矩阵，为自己训练Q矩阵。
2. 将teacher与student输出的logits分别与各自的V、Q矩阵相乘得到v、q向量。
3. q向量与各个v向量做点积，得出attention value。
4. 以attention value为权重得出MutualSoftLabel。
5. 将自己模型输出的logits与MutualSoftLabel计算KD_loss。
6. 将自己模型输出的logits与Label计算正常的Classify_loss。
7. 将两个loss加权求和，并进行反向传播。


# Decentralized Federated Learning under Unreliable Communication Environment

![网络参数恢复](./assets/网络参数补全.png)

# On-demand VR Video Streaming

![On-demand VR Video Streaming](./assets/路由.png)
