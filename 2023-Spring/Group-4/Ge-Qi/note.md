
## 2023.3.29周报
### 本周工作进展
+ 观看6G大会
   - 绿色通信主题
      - 5G能耗相比4G网络提高了14%，而6G相比5G按照目前的技术水平来看，总能耗又会增加不少。但是我国提出双碳的目标，要求未来部署6G的时候总能耗不能再增加了。基于此，专家们展开了激烈的讨论。有以下几个思路供我们借鉴：一是认为对于现在的普通用户来说，现有的网络提供的服务已经满足了他们的需求，所以6G只需要在特定场景下提供更多的服务，以此来减少网络整体能耗；二是利用卫星通信来降低总体能耗。卫星通信覆盖范围很大，利用这一特性，思考如何提高6G网络覆盖率，同时不提高能耗；三是信源信道联合考虑来降低能耗。
   - 论坛B天地融合智能组网
      - 天地融合是非常重要的特征，是研究者们研究6G的共识。
      - 发展趋势：
      	- 面向物：大尺度空间稀疏性连接的广域有效覆盖问题  星地融合
      	- 面向人：小尺度空间密集接入的局部通信容量问题  以用户为中心的弹性可定制网络
      - 星地融合面临的挑战：
            	- 无线传播特性不同
		- 传播距离和时延对于信号波形和传输方案影响
		- 卫星高速移动
	   	 	- 同步性能影响，多普勒频移，调制解调性能影响，移动性管理问题
		- 网络架构影响
		- 高低轨卫星间的干扰规避问题
     - 6G六大支柱技术 ：
            - 原生智能、星地融合、原生可信、网络感知、极致连接、碳中和

    - 论坛F：通感算

+ 学习Belief propagation算法的细节处理
+ 编写毕设仿真代码
   - 已经完成环境的仿真
   - 已经学习完成belif propagation算法的主体部分
   - 生成基站与用户的分布，以及基站与用户之间距离，基站之间的距离
```python
M=10  # 用户数目
S=5  # MEC数目
V = 20 # vr视频fov的数目
loss_mmWavs_l = 2  # 毫米微波通信直视径大尺度衰落损耗指数
loss_mmWavs_NL = 4  #非直视径
power_mmWave_M2V = 500  # MEC向用户发射的功率
gain_mmWave_M2V = 50 # MEC向用户发射的天线增益
B = 100 # 毫米微波总带宽 100Mhz 1Ghz
noise = 20 #表示噪声功率

def environment():
    location_MEC = []
    location_User = []
    # distance_of_MEC = {}
    # distance_of_M2V = {}
    distance_of_MEC = np.zeros((S,S))
    distance_of_M2V = np.zeros((S,M))  #MEC到VR用户之间的距离
    
    # location_User.append(np.random.uniform(0,100,(M,2)))
    # location_MEC.append(np.random.uniform(0,80,(S,2)))
    location_MEC = np.array([[31.89623446,  25.80012538],
       [50.26358657, 34.13710246],
       [68.45931639, 62.00738458],
       [78.77996488, 22.85299854],
       [87.72726464, 34.70996072]])
    location_User = np.array([[57.00384369, 37.1398421 ],
       [24.87054437, 35.25390064],
       [60.77580472, 30.39448567],
       [45.3263015 , 14.68861087],
       [87.10993105, 30.55264912],
       [41.18601161,  5.5938494 ],
       [93.82511157,  8.48631145],
       [79.47706327, 57.52225044],
       [69.26039538, 25.22740118],
       [88.2352694 , 14.05481878]])
    # plt.scatter(np.array(location_MEC)[:,0],np.array(location_MEC)[:,1],c="g")
    # plt.scatter(np.array(location_User)[:,0],np.array(location_User)[:,1],c="r")
    # plt.show()
    # 计算MEC与MEC之间的距离
    for i in range(S):
        for j in range(S):
            d = np.sqrt(np.sum(np.square(location_MEC[i]-location_MEC[j])))
            distance_of_MEC[i][j] = d  #第i个MEC与第j个MEC之间的距离

    #计算基站与MEC之间的距离
    for i in range(S):  # 遍历MEC
        for j in range(M):
            d = np.sqrt(np.sum(np.square(location_MEC[i]-location_User[j])))
            distance_of_M2V[i][j] = d   #第i个MEC与第j个用户之间的距离
    return distance_of_MEC,distance_of_M2V  #print(environment()[1])  输出M2V
distance_of_MEC = environment()[0]
distance_of_M2V = environment()[1]
```
+
    - 仿真用户请求的fov索引
      
```python
   
def user2fov():
    user_ask_fov = []
    user_ask_fov.append(np.random.randint(1,20,(M,1)))  # 随机生成用户请求的fov索引
    return user_ask_fov
user_ask_fov = user2fov()
```
+
	- 仿真MEC与用户之间的连接关系
```python
def link():  #定义MEC与VR用户之间的连接关系,与卸载策略无关
    link = np.zeros((S,M))
    distance_of_M2V = environment()[1]
    for i in range(M):
        location = np.where(distance_of_M2V==np.min(distance_of_M2V,axis=0))
        print(location)
        link[location] = 1
    return link
link = link()

def link_location():
    link_location = np.zeros((M,2))
    for i in range(M):
        for j in range(S):
            if link[j][i] == 1:
                link_location[i] = [i,j]
    return link_location
link_location = link_location()
# print(link_location)
```
+
	- 仿真毫米微波通信时用户与基站之间的通信速率
```python
def mmWave():
    rate_of_M2V = np.zeros((S,M))  
    SINR = np.zeros((S,M))
    distance_of_M2V = environment()[1]
    sum = np.zeros(S)
    print(distance_of_M2V)
    for k in range(S):
        for l in range(M):
            sum[k] = sum[k]+link[k][l]
    # print(sum)

    for i in range(S):
        for j in range(M):
            d = float(distance_of_M2V[i][j])
            y = power_mmWave_M2V * gain_mmWave_M2V
            y = y * pow(d,-4)/noise
            #计算一个基站连接几个用户
            if (sum[i] == 0 or link[i][j]==0):
                print("this MEC is not linked to the VR users")
            else:
                r = B * math.log(1+y,2) / int(sum[i]) 
                rate_of_M2V[i][j] = r              
    return rate_of_M2V
rate_of_M2V = mmWave()  # 逻辑上是对的，具体代入的值还需要查资料
```
+
	- 仿真fov不同版本的内存大小
```python
def video_version():   #计算不同版本fov的内存大小,以及背景内容和前景内容  假设所有fov具有相同的大小
    video_size = np.zeros(5)
    video_size_b = np.zeros(5)
    video_size_f = np.zeros(5)
    compression_ration = [0.65,0.7,0.75,0.8,0.9]
    backround = 0.7   # 背景内容占一个fov的占比
    max_video = 50 * 1024   #定义最大视频内存  50M
    for i in range(5):
        video_size[i] = max_video * compression_ration[i]
        video_size_b[i] = video_size[i] * backround
        video_size_f[i] = video_size[i] - video_size_b[i]
    return video_size,video_size_b,video_size_f
video_size = video_version()[0]
video_size_b = video_version()[1]
video_size_f = video_version()[2]
```
+
	-仿真不同渲染任务卸载策略时用户的时延
```python

CPU_cycel_l = 1000000 # vr设备的计算能力
CPU_cycel_mec = 
CPU_cycle_per_bite = #渲染操作时，每比特数据需要的CPU循环数 
commpression_cycle_per_bite = # 压缩操作时，每bit数据需要的CPU循环数
decommpress_cycle_per_bite = # 解压缩操作时，每bit数据需要的CPU循环数
compression_ratio = # 视频压缩比率
rate_of_fiber = #光纤数据传输速率

def option_location(option):  #用户选择的MEC的编号
    option_location = np.zeros((M,2))
    for i in range(S):
        for j in range(M):
            for m in range(F):
                for n in range(D):
                    if option[i][j][m][n] == 1:
                        option_location[j] = [j,i]
    return option_location
option_location = option_location(option=option)

def delay(rate_0f_M2V,option_location,link_location):
    delay = np.zeros((M,S+1,2,5))  #每个用户选择不同卸载策略对应的时延  M:用户‘S+1：第S+1 是本地卸载方式，
    # 之后依次是第S个MEC；2：0表示非合作；5：5号版本清晰度越高
    for i in range(M):
        for j in range(S+1):
           for m in range(2):
               for n in range(5):
                   if (j == S+1 ):  #本地渲染   不管m取何值，都是本地渲染
                       m = int(link_location[i][1])  #用户i连接的MEC编号
                       t_downlink = video_size[n] / rate_of_M2V[m][i]
                       t_render = video_size[n] * CPU_cycle_per_bite / CPU_cycel_l
                       delay[i][j][m][n] = t_downlink + t_render

                   elif(m == 0 and link_location[i][1] == option_location[i][1]):  # 不合作的MEC渲染  option 不迁移
                        t_render = video_size[n] * CPU_cycle_per_bite / CPU_cycel_mec
                        t_encode = video_size[n] * commpression_cycle_per_bite / CPU_cycel_mec
                        k = int(link_location[i][1])  #用户i连接的MEC编号
                        t_downlink = video_size[n] / compression_ratio /rate_of_M2V[k][i]
                        t_decode = video_size[n] * decommpress_cycle_per_bite / compression_ratio / CPU_cycel_l
                        delay[i][j][m][n] = t_decode + t_downlink + t_encode + t_render

                   elif(m == 0 and link_location[i][1] != option_location[i][1]): # 加上MEC之间传输的MEC渲染
                        t_render = video_size[n] * CPU_cycle_per_bite / CPU_cycel_mec
                        t_encode = video_size[n] * commpression_cycle_per_bite / CPU_cycel_mec
                        k = int(link_location[i][1])  #用户i连接的MEC编号
                        t_downlink = video_size[n] / compression_ratio /rate_of_M2V[m][i]
                        l = int(option_location[i][1])  # 服务用户i 的MEC编号
                        t_trasmission = distance_of_MEC[k][l] / rate_of_fiber
                        t_decode = video_size[n] * decommpress_cycle_per_bite / compression_ratio / CPU_cycel_l
                        delay[i][j][m][n] = t_decode + t_downlink + t_encode + t_render + t_trasmission
                    
                   elif(m == 1 and link_location[i][1] == option_location[i][1]):  # 合作渲染，不加MEC之间的传输
                        # 背景内容
                        t_render = video_size_b[n] * CPU_cycle_per_bite / CPU_cycel_mec
                        t_encode = video_size_b[n] * commpression_cycle_per_bite / CPU_cycel_mec
                        k = int(link_location[i][1])  #用户i连接的MEC编号
                        t_downlink = video_size_b[n] / compression_ratio /rate_of_M2V[k][i]
                        t_decode = video_size_b[n] * decommpress_cycle_per_bite / compression_ratio / CPU_cycel_l
                        t_background =  t_render + t_encode + t_downlink + t_decode
                        #前景内容
                        t_render_f = video_size_f[n] * CPU_cycle_per_bite / CPU_cycel_l
                        t_fusion = video_size[n] * CPU_cycle_per_bite / CPU_cycel_l
                        t_foreground = t_render_f + t_fusion
                        delay[i][j][m][n] = max(t_background,t_foreground) + t_fusion

                   else:  # 合作渲染,加MEC之间的传输
                        # 背景内容
                        t_render = video_size_b[n] * CPU_cycle_per_bite / CPU_cycel_mec
                        t_encode = video_size_b[n] * commpression_cycle_per_bite / CPU_cycel_mec
                        k = int(link_location[i][1])  #用户i连接的MEC编号
                        t_downlink = video_size_b[n] / compression_ratio /rate_of_M2V[m][i]
                        l = int(option_location[i][1])  # 服务用户i 的MEC编号
                        t_trasmission = distance_of_MEC[k][l] / rate_of_fiber
                        t_decode = video_size_f[n] * decommpress_cycle_per_bite / compression_ratio / CPU_cycel_l
                        t_background = t_render + t_encode + t_trasmission + t_downlink + t_decode
                        # 前景内容
                        t_render_f = video_size_f[n] * CPU_cycle_per_bite / CPU_cycel_l
                        t_fusion = video_size[n] * CPU_cycle_per_bite / CPU_cycel_l
                        t_foreground = t_render_f + t_fusion
                        delay[i][j][m][n] = max(t_background,t_foreground) + t_fusion
    return delay
```

### 下周工作计划
   + 完成毕设仿真
## 2023.3.22周报
### 本周任务汇报
+ 模型求解推导
    - 将原优化问题转化为Belief Propagation算法标准形式
       - ![image](./picture/picture.png)
       - ![image](./picture/微信图片_20230322202747.png)
       - ![image](./picture/微信图片_20230322202804.png)
    
    - 绘制因子图
    - 信念传播算法求解步骤
        - ![image](./picture/微信图片_20230322202815.png)
        - ![image](./picture/微信图片_20230322202819.png)
    
+ 求解算法学习
    - 学习了BP算法中因子相关运算的代码

```python
class factor:
    def __init__(self, variables = None, distribution = None):
        if (distribution is None) and (variables is not None):
            self.__set_data(np.array(variables), None, None)
        elif (variables is None) or (len(variables) != len(distribution.shape)):
            raise Exception('Data is incorrect')
        else:
            self.__set_data(np.array(variables),
                            np.array(distribution),
                            np.array(distribution.shape))
    
    def __set_data(self, variables, distribution, shape):
        self.__variables    = variables
        self.__distribution = distribution
        self.__shape        = shape
    
    # ----------------------- Info --------------------------
    def is_none(self):
        return True if self.__distribution is None else False
        
    # ----------------------- Getters -----------------------
    def get_variables(self):
        return self.__variables
    
    def get_distribution(self):
        return self.__distribution
    
    def get_shape(self):
        return self.__shape
    
    # factor product
    def factor_product(x,y):
        if x.is_none() or y.is_none():
            raise Exception('One of the factor is None')    # raise语句引发一个异常，异常/错误对象必须有一个名字，且它们应该是Error 或者Exception的子类

        xy,xy_in_x_ind,xy_in_y_ind = np.intersect1d(x.get_variables(),y.get_variables(),return_indices=True) 
        # np.intersect1d 函数查找两个数组的交集，并返回两个输入数组中都有序的，唯一的值。
        
        if xy.size ==0 :
            raise Exception('Factor do not have common variables') 
         
        if not np.all(x.get_shape()[xy_in_x_ind]==y.get_shape()[xy_in_y_ind]):# 判断共同变量的取值可能数目是否一致
            raise Exception('Commen Variables have different order')
        
        x_not_in_y = np.setdiff1d(x.get_variables(),y.get_variables(),assume_unique=True)
        y_not_in_x = np.setdiff1d(y.get_variables(),x.get_variables(),assume_unique=True)

        x_mask = np.isin(x.get_variables(),xy,invert=True) # 
        y_mask = np.isin(y.get_variables(),xy,invert=True) #

        x_ind = np.array([-1]*len(x.get_variables()), dtype=int)
        y_ind = np.array([-1]*len(y.get_variables()), dtype=int)
    
        x_ind[x_mask] = np.arange(np.sum(x_mask))
        y_ind[y_mask] = np.arange(np.sum(y_mask)) + np.sum(np.invert(y_mask))
    
        x_ind[xy_in_x_ind] = np.arange(len(xy)) + np.sum(x_mask)
        y_ind[xy_in_y_ind] = np.arange(len(xy))
    
        x_distribution = np.moveaxis(x.get_distribution(), range(len(x_ind)), x_ind)
        y_distribution = np.moveaxis(y.get_distribution(), range(len(y_ind)), y_ind)
                
        res_distribution =   x_distribution[tuple([slice(None)]*len(x.get_variables())+[None]*len(y_not_in_x))] \
                       * y_distribution[tuple([None]*len(x_not_in_y)+[slice(None)])]
    
        return factor(list(x_not_in_y)+list(xy)+list(y_not_in_x), res_distribution)
    
    # 边缘概率
    def factor_marginalization(x, variables):
        variables = np.array(variables)
    
        if x.is_none():
            raise Exception('Factor is None')
    
        if not np.all(np.in1d(variables, x.get_variables())):
            raise Exception('Factor do not contain given variables')
    
        res_variables    = np.setdiff1d(x.get_variables(), variables, assume_unique=True)
        res_distribution = np.sum(x.get_distribution(),
                              tuple(np.where(np.isin(x.get_variables(), variables))[0]))
    
        return factor(res_variables, res_distribution)
    #Factor reduction
    def factor_reduction(x, variable, value):  #value值是你要保留变量的取值的索引值
        if x.is_none() or (variable is None) or (value is None):
            raise Exception('Input is None')
    
        if not np.any(variable == x.get_variables()):
            raise Exception('Factor do not contain given variable')
    
        if value >= x.get_shape()[np.where(variable==x.get_variables())[0]]:
            raise Exception('Incorrect value of given variable')
    
        res_variables    = np.setdiff1d(x.get_variables(), variable, assume_unique=True)
        res_distribution = np.take(x.get_distribution(),
                               value,
                               int(np.where(variable==x.get_variables())[0]))
    
        return factor(res_variables, res_distribution)

    # 联合概率分布
    def joint_distribution(ar):
        for element in ar:
            if element.is_none():
                raise Exception('Factor is None')
            
        res = ar[0]
        for element in ar[1:]:
            res = factor.factor_product(res,element)

        return res
```


### 下周工作计划
+ 尽快完成BP算法求解模型的仿真



