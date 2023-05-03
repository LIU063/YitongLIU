# 2023.4.26  
   调试代码并修改细节，修改论文。

# 2023.4.26  
   调试代码并修改细节，撰写论文。
# 2023.4.19   
## 1.调研：
### 1.A secure software defined network: for heterogenous network co-exist
[1]流量预测：流量预测是路由优化领域的重要研究课题。流量预测用于通过分析历史流量数据来预测网络流量的模式。SDN控制器利用流量预测结果提前做出高效的流量路由决策，并将动态路由策略分发到数据平面中的设备。路由优化、流量分类都可以用SDN＋机器学习解决。          
[2]SDN中的DDoS攻击与防护：基于动态贝叶斯博弈          
[3]DDoS能耗：提出了一种改进的网络拓扑生成算法，该算法可以综合考虑链路交换能耗和卫星间链路能耗。考虑到卫星网络中异常流量造成的巨大能耗，提出了一种卫星网络中的DDoS缓解机制，旨在减少卫星节点处理异常流量所产生的额外能耗。          
[4]信息传输效率：探讨如何使用SDN技术来改善空中、地面和卫星通信网络的信息传输效率，特别是在SAGIN中实现动态切换的传输控制方案。该方案通过分离控制平面和数据平面以及使用SDN架构、排队博弈模型等来有效地分配SAGINs资源，从而降低数据转发节点控制功能的负载并提高网络性能。         
[5]安全、QoS和路由：提出了一种新的基于SDN的SAGINs安全路由和QoS感知的混合体系结构。在SAGIN中使用不同级别的多个SDN控制器，该架构遵循具有不同级别的不同路由供应层的分层结构，以利用SAGIN的异构性来找到满足安全性和QoS要求的多个路由。         
[6]SDN控制器优化部署管理方案（多控制器）：将SDN引入SAGIN，设计了一种基于分层域的支持SDN的SAGIN架构。提出了一种用于基于分层域的SDN使能的SAGIN的多控制器部署策略。首先，将SDN控制平面分为两层，即主控制器层部署在地面网络上，而次控制器层部署在基于空间的网络上。SDN数据平面由天基、空基和地基网络组成。其次，考虑平均网络延迟和控制器负载，多目标优化模型的构建。为了确定控制器的数量以及交换节点和控制器的相对位置，采用基于k-means的聚类算法对数据平面进行初步划分。最后，为了提高算法的全局搜索能力，采用了基于遗传算法的多目标优化算法。        
[7]提出区块链赋能的动态频谱管理框架，由上层软件定义网络（SDN）控制器组成联盟区块链网络，实现安全高效的网段间/片间频谱资源共享，由上层SDN控制器管理的下层SDN控制器负责片内频谱接入。         

[1]Ghaffar Z, Alshahrani A, Fayaz M, et al. A topical review on machine learning, software defined networking, internet of things applications: Research limitations and challenges[J]. Electronics, 2021, 10(8): 880.         
[2]Li Z, Yang B, Zhang X, et al. DDoS Defense Method in Software-Defined Space-Air-Ground Network from Dynamic Bayesian Game Perspective[J]. Security and Communication Networks, 2022, 2022: 1-13.         
[3]Z. Tu, H. Zhou, K. Li, M. Li and A. Tian, "An Energy-Efficient Topology Design and DDoS Attacks Mitigation for Green Software-Defined Satellite Network," in IEEE Access, vol. 8, pp. 211434-211450, 2020, doi: 10.1109/ACCESS.2020.3039975.         
[4]C. Guo, C. Gong, H. Xu, L. Zhang and Z. Han, "A Dynamic Handover Software-Defined Transmission Control Scheme in Space-Air-Ground Integrated Networks," in IEEE Transactions on Wireless Communications, vol. 21, no. 8, pp. 6110-6124, Aug. 2022, doi: 10.1109/TWC.2022.3146452.         
[5]Hashem Eiza, M and Raschella, A A Hybrid SDN-based Architecture for Secure and QoS aware Routing in Space-Air-Ground Integrated Networks (SAGINs). In: IEEE Wireless Communications and Networking Conference, Glasgow, Scotland, UK. (Accepted)         
[6]C. Chen, Z. Liao, Y. Ju, C. He, K. Yu and S. Wan, "Hierarchical Domain-Based Multicontroller Deployment Strategy in SDN-Enabled Space–Air–Ground Integrated Network," in IEEE Transactions on Aerospace and Electronic Systems, vol. 58, no. 6, pp. 4864-4879, Dec. 2022, doi: 10.1109/TAES.2022.3199191.         
[7]LI Z, WANG W, GUO J, et al. Blockchain‐Empowered Dynamic Spectrum Management for Space‐Air‐Ground Integrated Network[J]. Chinese Journal of Electronics, 2022, 31(3): 456-466.         

###  2.SEN自适应进化网络（Self-Evolving Network）：
&ensp;&ensp;&ensp;&ensp; 是一种基于人工智能和自适应技术的新一代网络架构，它可以在网络运行期间对自身进行学习、优化和演化，以适应不断变化的网络环境和需求。SEN网络可以根据网络流量、网络拓扑结构、用户需求等因素进行智能调整和优化，从而提供更高效、更可靠、更安全的网络服务。SEN的概念实现了多级智能网络管理策略，可以跨不同的网络、运营商甚至生态系统（例如蜂窝或卫星生态系统）执行。        
&ensp;&ensp;&ensp;&ensp; 自组织网络（SONs）：3GPP在4G和5G文档中引入，其主要思路是实现无线网络的一些自主功能，如自配置、自优化、自愈，减少人工参与，降低运营成本。但是SONs无法足够灵活地应对复杂性，异构性和移动性更大的SAGIN。网络需要使其功能适应特定的环境状态，转变为能够在高度动态和复杂的环境中保持其性能的自我演进的网络。          
&ensp;&ensp;&ensp;&ensp; SEN框架包括三个关键组件：SEN引擎、冲突避免和协调管理实体，以及分布式和协作计算。人工智能将作为SEN引擎的核心，并通过机器学习算法实现，其将利用通信环境收集的数据（例如空间和时间的流量分布、用户偏好和移动模式）以及外部信息来源的改进，如新技术、新兴网络组件和先进的通信服务。         
&ensp;&ensp;&ensp;&ensp; SEN能做什么：集成的跨网络优化、扩展网络容量/覆盖范围、智能波束成形、分布式数据卸载和计算         
&ensp;&ensp;&ensp;&ensp; SEN面临的挑战：智能和标准化的冲突解决算法（解决不同运营商、网络或生态系统之间的冲突）、跨网络、运营商和生态系统的信息共享和学习（将联邦学习概念扩展到不同的分布式级别和规模上工作）、学什么及如何学（选择适当的数据范围和持续时间对于避免学习和处理不必要的数据非常重要）、实时和在线学习算法（适应可扩展和高度可变的网络环境）、在未来集成网络中实现Sen概念的成本（数据收集的通信成本、计算资源的部署成本、ML的计算成本）         
&ensp;&ensp;&ensp;&ensp; 集成的垂直异构网络（VHetNet）架构：在空中、地面和卫星等不同网络层次之间实现了紧密的集成和协作。[8][9]        
&ensp;&ensp;&ensp;&ensp; 关于self-evolving算法有很多：[10][11][12]    



[8]Darwish T, Kurt G K, Yanikomeroglu H, et al. A vision of self-evolving network management for future intelligent vertical HetNet[J]. IEEE Wireless Communications, 2021, 28(4): 96-105.    
[9]A. Farajzadeh, M. G. Khoshkholgh, H. Yanikomeroglu and O. Ercetin, "Self-Evolving Integrated Vertical Heterogeneous Networks," in IEEE Open Journal of the Communications Society, vol. 4, pp. 552-580, 2023, doi: 10.1109/OJCOMS.2023.3243870.        
[10]Y. -Y. Lin, J. -Y. Chang and C. -T. Lin, "Identification and Prediction of Dynamic Systems Using an Interactively Recurrent Self-Evolving Fuzzy Neural Network," in IEEE Transactions on Neural Networks and Learning Systems, vol. 24, no. 2, pp. 310-321, Feb. 2013, doi: 10.1109/TNNLS.2012.2231436.        
[11]C. -F. Juang and Y. -W. Tsao, "A Self-Evolving Interval Type-2 Fuzzy Neural Network With Online Structure and Parameter Learning," in IEEE Transactions on Fuzzy Systems, vol. 16, no. 6, pp. 1411-1424, Dec. 2008, doi: 10.1109/TFUZZ.2008.925907.         
[12]S. Wu and T. W. S. Chow, "Self-Organizing and Self-Evolving Neurons: A New Neural Network for Optimization," in IEEE Transactions on Neural Networks, vol. 18, no. 2, pp. 385-396, March 2007, doi: 10.1109/TNN.2006.887556.    
   
                
### 3.A variable trust protocol：    
&ensp;&ensp;&ensp;&ensp; 混合太空架构（HSA）概念是由美国太空军太空作战部长杰伊·雷蒙德将军在2020年的《企业卫星通信愿景》中提出，该架构由多个轨道上的军用和商业卫星组成，设计为一个网络集成能力的“太空互联网”，并提供基础性的网络防护以抵御黑客攻击。该架构集成了新兴小卫星功能和传统美国政府太空系统，可在安全环境中利用利用云、分层和低延迟通信，连接不同的民用、军用、商业和盟军太空系统，将显著提高太空的威慑力和韧性。[13]     
美军动向：AFRL快速架构原型和集成开发（RAPID）实验室专门研究小型卫星和未来混合太空架构；太空军目标在2027年实现混合太空体系架构初始作战能力；国防部设计“防黑客太空互联网”；太空军太空作战分析中心开发“总体太空数据传输力量设计”。     
已确定了四个研究领域：多路径通信（Multi-Path Communications）、可变信任协议（Variable Trust Protocol）、多源数据融合（Multi-Source Data Fusion）和基于云的分析（Cloud-Based Analytics）。     
可变信任协议：该研究领域将使最终用户能够根据风险或任务应用调整信任因素，包括考虑数据源和网络路径。武器使用可能需要高可信度，态势感知的开源信息。网络路径的信任因素包括截获概率、检测概率、抗干扰能力、链路和端到端加密以及零信任连续身份验证。     
美国国防部指出，“我们必须确保通过增加的访问点不引入漏洞。由于参与的网络种类繁多，每个链接和节点将根据其在架构内的观察行为被动态地分配一个信任分数。然后，基于信息的敏感性和时效性，流量可以通过优选的链接进行路由。”这段话强调了通过在网络架构内观察节点行为并为其分配动态信任分数，以保护信息并基于敏感性和时效性来路由流量的可变信任协议的重要性。

<https://mp.weixin.qq.com/s?__biz=MzIzNTE3Mjg1MQ==&mid=2650341314&idx=1&sn=9993c3f48a4a07b9a91b47874c63c527&chksm=f0e7795ec790f048bd1e0863c984b265d631f593439c973798c7119b19375681802f38058dd9&scene=27>         

## 2.代码进度     
&ensp;&ensp;&ensp;&ensp; 现在在做多用户的随机接入。完成了优化p得到系统最优的Rsum=R1+R2+R3的情况，但是存在一些问题。比如有些接入情况下，优化p不能收敛，有些R保密率会出现等于0的情况。初步猜测是跟信道环境有关。    
&ensp;&ensp;&ensp;&ensp; 在做接入选择的训练时，也存在一些问题还没有解决。比如输出是27个值，但是有些值始终为0，目前认为与损失函数的定义有关，后续打算自定义损失函数，给每个输出设置一个惩罚因子和阈值。             
&ensp;&ensp;&ensp;&ensp;   做测试时，接入选择基本都是同一种。    

![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/Rsum.png)
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/pdis.png)
## 下周计划：
&ensp;&ensp;&ensp;&ensp; 将代码修改好，开始写论文。   

# 2023.4.12    
## 1.场景修改：   
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/scene2_1.jpg) 
## 2.代码仿真：    
   用了pytorch-ligntning的框架   
   pytorch-lightning是pytorch的抽象和包装。它的好处是可复用性强，易维护，逻辑清晰等。      
   三层的mlp来训练    
   visdom动态画图    
   [运行结果](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/pdf/square.pdf)
## 3.场景重建：         
多用户多接入问题，共有27种接入方案。针对每种方案，优化p1,p2,p3，得到各种情况下的最优的Rsum。再用mlp，在这种情况下，做智能接入选择。
## 4.下一步工作计划：    
  完成代码
  


# 2023.4.5  
## 场景重建：    
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/scene.jpg)   
## 下一步工作计划  
完成代码编写

# 2023.3.29
## 1.代码编写  
代码部分分为三步：  
（1）优化功率分配，实现保密率最大化。
~~~
S=-(R1+R2+R3)         ###总的负的和保密率最小===保密率最大
print('SUM',S.item())
optimizer_1.zero_grad()
S.backward()
optimizer_1.step()    
~~~
（2）在得到功率分配的基础上，计算得到安全情况最好的接入方案。    

（3）通过深度卷积神经网络的训练，通过人工智能的方式在获取到信道向量的情况下自动选择接入哪个信道。  
~~~
# 定义神经网络
def baseline_model():
    model = Sequential()
    model.add(Conv1D(32, 3, input_shape=(12, 1),padding="same"))
    model.add(Conv1D(32, 3, activation='relu',padding="same"))
    # model.add(MaxPooling1D(3,data_format='channels_last'))
    model.add(Conv1D(64, 3, activation='tanh',padding="same"))
    model.add(Conv1D(64, 3, activation='tanh',padding="same"))
    # model.add(MaxPooling1D(3))
    model.add(Conv1D(64, 3, activation='tanh',padding="same"))
    model.add(Conv1D(64, 3, activation='tanh',padding="same"))
    # model.add(MaxPooling1D(3))
    model.add(Flatten())
    model.add(Dense(3, activation='softmax'))
    plot_model(model, to_file='./model_classifier.png', show_shapes=True)
    print(model.summary())
    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
    return model
    
    
# 显示混淆矩阵
def plot_confuse(model, x_val, y_val):
    predictions = model.predict(x_val)
    predictions = np.argmax(predictions, axis=1)
    # predictions=predictions.argmax(axis=-1)
    predictions=out_label_onehot(predictions)
    print("predieted",predictions)
    truelabel = y_val.argmax(axis=-1)   # 将one-hot转化为label 索引
    print("truelabel",truelabel)
    truelabel=out_label_onehot(truelabel)
    print("truelabel:",truelabel)
    sns.set()
    f,ax = plt.subplots()
    y_true = truelabel
    y_pred = predictions
    C2 = confusion_matrix(y_true,y_pred)
    print(C2)
    a=sum(C2)
    b=a.sum(axis=0)
    print(b)
    sns.heatmap(C2/b,annot=True,ax=ax,cmap="OrRd") #画热力图
    ax.set_title('confusion matrix') #标题
    indices = [0.5,1.5,2.5]
    ax.set_xticks(indices, ['sat', 'bs', 'uav'])
    ax.set_yticks(indices, ['sat', 'bs', 'uav'])
    ax.set_xlabel('predict') #x 轴
    ax.set_ylabel('true') #y 轴\
    plt.show()
    f.savefig('confusion.png')
 ~~~
#### 下图为训练结果，正确率在70%左右。
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/confusion.png)     
（4）MLP网络  
~~~
  def __init__(self, input_num, output_num):
        super(MLP, self).__init__()
        hidden1 = 214   # 第二层节点数
        hidden2 = 214   # 第三层节点数
        self.fc1 = nn.Linear(input_num, hidden1)
        self.fc2 = nn.Linear(hidden1, hidden2)
        self.fc3 = nn.Linear(hidden2, output_num)
        # 使用dropout防止过拟合
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        out = torch.relu(self.fc1(x))
        out = self.dropout(out)
        out = torch.relu(self.fc2(out))
        out = self.dropout(out)
        out = self.fc3(out)
        return out
~~~  
~~~
for step, (x, y) in enumerate(tqdm(train_loader)):
          #  enumerate() 是python内置的迭代方法
          #tqdm 是以进度条的方式可视化运行过程的模块
            logits = model(x)
            loss = criterion(logits, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        viz.line([loss.item()], [epoch], win='loss', update='append')
        if epoch % 5 == 0:
            val_acc = evaluate(model, val_loader)
            # train_acc = evaluate(model,train_loader)
            print("epoch:[{}/{}]. val_acc:{}.".format(epoch, epoches, val_acc))
            # print("train_acc", train_acc)
            viz.line([val_acc], [epoch], win='val_acc', update='append')
            if val_acc > best_acc:
                best_epoch = epoch
                best_acc = val_acc
                torch.save(model.state_dict(), 'best.mdl')
~~~   
#### 训练结果：准确度达到97%以上  
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/confusionmlp1.png)
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/loss.png)
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/valacc.png)

## 2. 6G大会思考  
### 论坛B：天地融合智能组网技术
&ensp;&ensp;&ensp;&ensp; **星地融合路径发展趋势**：5G体制兼容走向6G系统融合。以5G技术为基础，根据卫星链路等差异化，有针对性的修改和优化低轨卫星系统；最大程度复用5G技术，并利用5G规模经济，降低成本，实现差异化竞争优势。6G融合要支持终端在星地间无缝切换    
&ensp;&ensp;&ensp;&ensp; **卫星与地面的差异及关键影响**：无限传播特性不同、传播距离和时延对于信号波形和传输方案影响、卫星高速移动（同步性能影响、多普勒频偏、调制解调性能影响、移动性管理问题）、网络架构影响（立体组网）、高低轨卫星间的干扰规避问题。    
&ensp;&ensp;&ensp;&ensp; **星地面融合需要考虑的关键技术问题：**（1）基础问题：信道建模、链路&系统评估方法、链路预算、频率复用等。（2）网络架构：透明转发VS星上处理、星间链路、立体组网。（3）物理层关键技术：波形、传输参数、调制、参考信号、信道设计、物理层过程。（4）高层关键技术：寻呼、移动性管理、路由、用户面协议。    
&ensp;&ensp;&ensp;&ensp; **6G的6大支柱技术**：原生智能、网络感知、星地融合、极致连接、碳中和、原生可信。    
&ensp;&ensp;&ensp;&ensp;  **6G主要特征**：**全覆盖**（立体时变：大延时、高动态；环境复杂：空间环境、安全环境；全球覆盖：万级节点，亿级用户；资源受限：节点受限、频轨受限；场景多样：陆海空天、通导感算）、**全频谱**（sub-6G、毫米波、太赫兹、光频段）、**强智能**（认知能力（立体感知信息元素构建、全面准确及时的多维信息感知和提取）、分析能力（自动挖掘和提取潜在的智能数据模型及其交互）、评估能力（规则优化、特征分析、用于自主推理的容错网络沙箱）、执行能力（灵活网络资源配置、具有高鲁棒性的主动分配）、设计能力（复杂网络演变的动态模型））、**强安全**（安全可靠、审计运算、本地密钥、跨域防护、端到端内生安全、可信基础设施、分布式身份验证、分布式DNS服务、分布式BGP路由通告）    
&ensp;&ensp;&ensp;&ensp; **6G其他特征**：算力网络、数字孪生等。    
&ensp;&ensp;&ensp;&ensp; **6G的未来发展方向**：空天地一体化网络，云-边缘-终端协作，弹性自适应网络，集成接入和自适应传输，资源感知与动态共享    
&ensp;&ensp;&ensp;&ensp;6G的特征标准等尚未统一，在近几年，标准组织开始了对6G的调研，最近几年会开始6G标准的制定。我国的三大运营商和华为等通信企业，都在6G等方面进行了相关研究。其他国家也发布了针对6G发展的规划，我国预计在2030年推进到6G规模化商用阶段。希望我国在6G阶段可以实现全面领跑。

### 论坛G：6G网络安全与隐私保护
&ensp;&ensp;&ensp;&ensp;内生安全是6G发展的趋势，它是一种由系统结构决定的自身的安全，是与网络服务紧耦合的安全，是不可解耦的。关于内生安全问题，要强调安全问题分析、网络弹性、初始协同的可信设计等。尽管我们对内生安全有很高的要求，但是要实现内生安全仍面临许多挑战，比如：去中心化的网络架构下的可信接入难以保证，高度跨域异构融合要求更安全的接入认证。华为方面提出的engine和gear架构是一种很新的角度，因为分布式的网络架构对内生安全来说挑战巨大，华为这种方式与常规的内生安全有所不同，值得借鉴思考。中国电信方面，更是提出了一种开放式的安全，让人耳目一新。6G内生安全的关键技术主要有：网络内生安全、人工智能安全、机密计算、供应链安全、拟态防御架构、无线内生安全、抗量子密码、区块链。我所做的毕业设计在某种意义上涉及了人工智能安全和无线内生安全两种技术。

### 论坛C：双碳下的6G网络覆盖
&ensp;&ensp;&ensp;&ensp;双碳下，通信网络的设计要考虑将碳排放降低，能量效率提高。要以更少的能量来传递更多的信息。未来要做到基站能耗和边缘服务器能耗相互协调。移动通信必须要改变“按照最坏情况来设计网络覆盖”的模式。在现在网络蜂窝覆盖下，能耗主要在：**2/3/4/5G基站密集部署且24h运行，大量基站没有充分运用但是仍在运行  要根据业务调整基站的开关和部署  控制覆盖和业务覆盖分离**。  
&ensp;&ensp;&ensp;&ensp;面向6G的低碳智能覆盖：太阳能覆盖支持的非地面网络，可能在运行时达到0碳排。建站时要考虑部署效率和能量效率的折中。控制数据分离已经成为主流方向，未来肯定能做到按需智能数据覆盖。期待能用低频解决广覆盖，高频解决容量问题。6G标准化可能面临分离的场景，需要加强国际合作。   
&ensp;&ensp;&ensp;&ensp;移动通信网络运营成本里面有大概40%都是来自于电费，基站能耗的80%来自于中射频，20%左右是来自于基带，因此对中射频和空口的设计是整个网络实现双碳的核心。在设计过程中，要非常清晰地认识到每个链路层天花板在哪里，同时要知道它是在功率受限场景，还是在带宽受限的场景。资源管理技术：随着用户分布和需求而调整功率、广覆盖来兜底等。NTN的链路功耗较大，但是广覆盖能够降低地面功耗。   
&ensp;&ensp;&ensp;&ensp;终端辅助基站节能。终端向网络侧发送一些上行换信号或终端辅助信息，帮助基站选择何时进入节能状态。    
&ensp;&ensp;&ensp;&ensp;覆盖是网络最基础的指标，但是覆盖跟容量、能量密切相关，没办法只去提高覆盖，然后不考虑能量、不考虑容量的需求。把信号用算法算力做的预处理放在通用或集中的地方或云化部署，能降低网络能效。高铁上可以用RIS来提高性能体验。 
## 3. 下周工作计划  
&ensp;&ensp;&ensp;&ensp;待定

# 2023.3.22
## 1.场景建模
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
## 2.开题答辩
  撰写开题报告5000字，完成开题答辩。
## 3.学习调研
   学习b站视频《跟李沐学ai》,看完1/3，复习线性回归、神经网络等基础知识。学习DQN算法，跑通并读懂DQN最常见的应用车杆游戏的代码。  
![cartpole](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/cartpole.png)
## 4.下一周计划
   完成优化功率分配的代码，完成DQN的大部分内容。
   

