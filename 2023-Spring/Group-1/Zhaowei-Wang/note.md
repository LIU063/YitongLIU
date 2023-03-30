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
### 训练结果：准确度达到97%以上  
![channel](https://github.com/UNIC-Lab/Weekly-Report/blob/main/2023-Spring/Group-1/Zhaowei-Wang/picture/confusionmlp1.png）


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
&ensp;&ensp;&ensp;&ensp;将卷积神经网络替换成MLP三层或四层网络，提高准确率到90%及以上。

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
   

