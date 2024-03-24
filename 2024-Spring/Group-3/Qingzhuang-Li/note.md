## week 1  
- 学习openmax代码，使用小型wifi数据集wisig和神经网络resnet、openmax在闭集和开集上进行试验，测试结果在使用resnet在闭集上分类正确率很高，但在开集上，resnet和openmax的分类正确率和对未知类的拒绝率都很差    
  原因：推测是由于数据集太小（6个发射器，12个接收器），resnet造成过拟合。 而openmax的weibull模型只使用两类作为异常类进行拟合，模型的拟合不够好   
  wisig：   
  [Hanna S, Karunaratne S, Cabric D. Wisig: A large-scale wifi signal dataset for receiver and channel agnostic rf fingerprinting[J]. IEEE Access, 2022, 10: 22808-22818.](https://ieeexplore.ieee.org/abstract/document/9721895)  
  openmax：  
  [Bendale A, Boult T E. Towards open set deep networks[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2016: 1563-1572.](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Bendale_Towards_Open_Set_CVPR_2016_paper.html)
- 调研数据集
## week2  
- 使用有150类的数据集进行试验在闭集下进行试验，结果有很严重的过拟合，分类精度大概65%左右，而且对噪声很敏感。
- 针对此问题调研了对于数据增强、以及关于数据不平衡问题的论文。   
  - [Wang C, Fu X, Wang Y, et al. Few-shot specific emitter identification via hybrid data augmentation and deep metric learning[J]. arXiv preprint arXiv:2212.00252, 2022.](https://arxiv.org/abs/2212.00252)   
  - [Z. Ren, P. Ren, D. Xu and T. Zhang, "Noise-Tolerant Radio Frequency Fingerprinting With Data Augmentation and Contrastive Learning," 2023 IEEE Wireless Communications and Networking Conference (WCNC), Glasgow, United Kingdom, 2023, pp. 1-6, doi: 10.1109/WCNC55385.2023.10118833.](https://ieeexplore.ieee.org/abstract/document/10118833)   
  - [X. Fan, C. Zhao, L. Xiao and X. Huang, "Random Railings Enhancement For RFF Imbalanced Data Augmentation," 2023 IEEE Wireless Communications and Networking Conference (WCNC), Glasgow, United Kingdom, 2023, pp. 1-6, doi: 10.1109/WCNC55385.2023.10118947.](https://ieeexplore.ieee.org/abstract/document/10118947)
