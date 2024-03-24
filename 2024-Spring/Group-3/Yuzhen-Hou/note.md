<p id="table"></p>

## Table of Contents

- <a href="#4">Week 4 (2024.3.11 – 2024.3.17)</a>

<br/>

------

<p id="4"></p>

## <a href="#table">Week 4 (2024.3.11 – 2024.3.17)</a>

### Work

1. 论文调研

   - \[1\] <a href="https://ieeexplore.ieee.org/abstract/document/10419579">F. Shi et al., "**Radio Frequency Fingerprint Identification Based on Length-Robust Representation and Incremental Learning**," _2023 IEEE 23rd International Conference on Communication Technology (ICCT)_, Wuxi, China, 2023, pp. 236-240, doi: 10.1109/ICCT59356.2023.10419579.</a>
   - \[2\] <a href="https://www.sciencedirect.com/science/article/pii/S1000936121002934">Ya Tu, Yun Lin, Haoran Zha, Ju Zhang, Yu Wang, Guan Gui, Shiwen Mao, **Large-scale real-world radio signal recognition with deep learning**, _Chinese Journal of Aeronautics_, Volume 35, Issue 9, 2022, Pages 35-48, ISSN 1000-9361, https://doi.org/10.1016/j.cja.2021.08.016.</a>
   - \[3\] <a href="https://ieeexplore.ieee.org/abstract/document/10360105">X. Yang and D. Li, "**LED-RFF: LTE DMRS-Based Channel Robust Radio Frequency Fingerprint Identification Scheme**," in _IEEE Transactions on Information Forensics and Security_, vol. 19, pp. 1855-1869, 2024, doi: 10.1109/TIFS.2023.3343079.</a>
   - \[4\] <a href="https://ieeexplore.ieee.org/abstract/document/10397582">Y. Zhang, Q. Zhang, H. Zhao, Y. Lin, G. Gui and H. Sari, "**Multisource Heterogeneous Specific Emitter Identification Using Attention Mechanism-Based RFF Fusion Method**," in _IEEE Transactions on Information Forensics and Security_, vol. 19, pp. 2639-2650, 2024, doi: 10.1109/TIFS.2024.3353594.</a>
   - \[5\] <a href="https://ieeexplore.ieee.org/abstract/document/10419769">T. Wu, Y. Zhang, C. Ben, Y. Peng, P. Liu and G. Gui, "**Specific Emitter Identification Based on Multi-Scale Attention Feature Fusion Network**," 2023 _IEEE 23rd International Conference on Communication Technology (ICCT)_, Wuxi, China, 2023, pp. 1390-1394, doi: 10.1109/ICCT59356.2023.10419769.</a>

2. 数据集调研

   - Datasets for RF Fingerprinting of Bit-similar USRP X310 Radios(ORACLE: WiFi, air, 16devs, 2-62feet)
   - Datasets for RF Fingerprinting on the POWDER Platform(4G LTE/5G BS, air, 4BS+1rec, 300m-1km(wild))

3. 开放集识别实验尝试

   - LoRa数据集，训练集20种设备，开放集测试共30种设备，针对未见设备分类拒绝率小于50%
     
     可能原因：
     - 没有使用论文中使用的信道无关时频谱，而是直接使用原始时频谱送入网络，需要思考不依靠协议本身的去噪手段
     - OpenMax架构由于对异常类的检验采用了Weibull分布，本质进行的是1-vs-All的多个二分类，并没有很好地学习到区分设备的特性
    
     考虑的改进：
     - 加入文中采用的信道无关时频谱，或直接将原始信号与导频信号作差得到的噪声信号送入网络进行训练
     - 尝试使用原型卷积网络训练

