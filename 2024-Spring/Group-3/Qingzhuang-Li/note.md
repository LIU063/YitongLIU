## week 1  
- 学习openmax代码，使用小型wifi数据集wisig和神经网络resnet、openmax在闭集和开集上进行试验，测试结果在使用resnet在闭集上分类正确率很高，但在开集上，resnet和openmax的分类正确率和对未知类的拒绝率都很差    
  原因：推测是由于数据集太小（6个发射器，12个接收器），resnet造成过拟合。 而openmax的weibull模型只使用两类作为异常类进行拟合，模型的拟合不够好   
  wisig：   
  [Hanna S, Karunaratne S, Cabric D. Wisig: A large-scale wifi signal dataset for receiver and channel agnostic rf fingerprinting[J]. IEEE Access, 2022, 10: 22808-22818.](https://ieeexplore.ieee.org/abstract/document/9721895)  
  openmax：  
  [Bendale A, Boult T E. Towards open set deep networks[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2016: 1563-1572.](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Bendale_Towards_Open_Set_CVPR_2016_paper.html)
- 调研数据集
