## Tips for Writing an English paper

- 缩写
    - 首次出现的缩写都必须给出名字全称
    - 缩写标准格式：
      - 示例：virtual reality (VR)
      - 注意：全称小写，括号前要空格
    - 在摘要中出现过的**全称（缩写）**，在intro及以后部分第一次出现还要再**全称（缩写）**，后边用到的地方都用缩写形式
- 标点符号注意：
  - 英文中标点符号后要空一格再继续下一句话
  - 括号前需要空格
  
- 全文避免用相同的表达，类似语义的，换方式进行表达
- 关于a/an、the以及复数的用法：
    - a/an以及复数都表示泛指，在论文题目中多采用复数的形式，表示对这一类网络/系统/模型进行研究
    - 在系统模型部分，通常会用the ，表示针对一个具体的典型的系统（当然，不失一般性）来研究 the system model
    - 自己提出的算法，第一次出现时用a/an，后面再次提到时则表示特指，用the proposed algorithm；
- 关于effective和efficient的用法：
    - Effective通常指有效性，简单的说即算法提升了系统性能时，用effective。
    - Efficient则指时间上的效率，当算法复杂度降低，运行效率更快时，用efficient	
- 关于仿真结果的说明
    - 简单的代码仿真用numerical result；experiment results 是需要做实物实验的；simulation results一般是要搭实际的软件仿真平台。像简单的算法仿真，只能是numerical results 



## 摘要
- 关于英文摘要部分，请仔细阅读Victor O. K. Li的[Hints on Writing Technical Papers and Making Presentations](https://ieeexplore.ieee.org/document/762947)；尽量使用被动语态，不允许出现第一人称。有些论文也有个别使用we的情况，如果你不是大牛，建议不要使用。如果是conference paper，可以使用this paper proposes…；如果偏综述性的长文，可以用this article。
- 摘要内容安排：
  - 背景相关的介绍最多占整个摘要的1/3左右，2/3 用语言高度概括本文的工作。
- 介绍背景注意：
  - 背景介绍需要和本文研究工作密切相关，切忌空泛
  - 示例：
 
原文：
```
Virtual reality (VR), as a revolutionary mode of interaction, presents unprecedented opportunities and challenges for the next generation of mobile communication technology. It
is well-known that rendering is the key performance bottleneck in wireless VR systems.
```
修改后：
```
Due to the stringent latency requirements on computation-intensive rendering during the virtual reality (VR) transmission and the limitations of computational resources on VR devices, extensive research has focused on task offloading with joint communication and computing resource scheduling to address these challenges.
```
原文只是很空泛的引入了VR，没有和论文的研究工作相结合。由于该论文是研究如何面对VR时延要求高，计算资源有限所带来的挑战，所以将摘要的背景部分修改为上文。修改后的背景介绍和论文的研究工作联系更紧密，更合适。

- 介绍论文研究工作注意：
   - 介绍时尽量将contribution也夹杂在其中点出来，如果由于篇幅限制，不能将所有的contribution都夹杂在其中都写出来，那尽量写一两个进去。
   - 介绍仿真（数值）结果时，要写清楚在哪一方对比什么有了提升，不要大、空。
     - 示例
       - 原文：
                 ```
                 Finally, numerical results is given to demonstrate the efficiency of the proposed algorithm.
                 ```
       - 修改后：
                 ```
                 Finally, numerical results show that the proposed method significantly reduces online processing latency compared to the BP algorithm and offers higher interpretability compared to data-driven algorithms.
                 ```
## 关键词
- 多个关键词按照字母顺序排列，且仅第一个词首字母大写。

## introduction
- 介绍别人工作时，被动语态用现在时，主动语态用过去时；
- introduction一定要注意**逻辑的连贯性**和逻辑的**层层递进**关系。
   - 示例：
       - 原文：
                 ```
                 As a revolutionary mode of interaction, virtual reality (VR) is poised to become one of the dominant trends in the next generation of mobile communication technology, offering users an unprecedented means to perceive and interact with virtual worlds. VR has garnered widespread attention from both the academic and industrial sectors. Compared to the traditional video transmission, VR video transmission involves an additional rendering process. Rendering refers to the generation of images from a model where a model represents a 3D object or virtual environment. It is worth noting that rendering task demands a substantial amount of computational and transmission resources, but computational resources on VR devices are limited. Furthermore, VR video transmission imposes stricter requirements on latency. The conflict between the substantial computational and communication resource requirements, the demand for ultra-low latency, and the limited resources of VR devices makes the allocation of computational resources and communication resources for rendering task is crucial and more challenging. Mobile edge computing (MEC) servers with additional computational and caching resources is an effective method for the demand of rendering task.····
                 ```
       - 修改后：
                 ```
                 As a revolutionary mode of interaction, virtual reality (VR) is poised to become one of the dominant trends in the next generation of mobile communication technology, offering users an unprecedented means to perceive and interact with virtual worlds. VR aims to provide users with a more immersive and interactive experience. To ensure the user experience, VR transmission imposes strict requirements on latency. As a key technology in VR transmission, rendering 
has been investigated by many studies as it determines the quality and realism of visual effects in the virtual environment. Specifically, rendering refers to the generation of images from a model where a model represents a 3D object or virtual environment . Rendering tasks demand a significant amount of computational resources. Unfortunately, VR devices have limited computational capacity, making it unfeasible to rely solely on the computational resources of VR devices to complete rendering tasks within the required time. Mobile edge computing (MEC) servers with additional computational is an effective method for the demand of rendering task.····
                 ```
            - 说明：
                - 原文第二句话“VR has garnered····”到第三句话“Rendering refers to the”存在不连贯的问题，修改后以“As a key technology in VR transmission”作为过渡，连贯性更好；修改后中的“Specifically, rendering refers to····”中的Specifically，也是起到过渡作用。在写作中，注意使用一些短语，副词将上下文串起来，提升连贯性。
                - 原文“The conflict between the substantial computational and communication resource requirements, the demand for ultra-low latency, and the limited resources of VR devices makes the allocation of computational resources and communication resources for rendering task is crucial and more challenging.”本身逻辑就有问题，同时与后边引入MEC的递进关系也不明显。修改后我们可以看到“VR--rendering task--渲染任务需要大量计算资源--VR设备计算资源有限--引入带有额外计算资源的MEC”清晰的逻辑递进关系。原文中可能通过理解推断也可以得到这个逻辑关系，但是在论文撰写时，我们需要做到直接清晰的把层层递进的逻辑关系展示出来。

## 正文
- 公式相关
  - 字母小写加粗表示向量
  - 字母大写加粗表示矩阵
  - 公式用as、is引出，公式要看作文章整体的一部分，公式后需要根据语义加上相应的“,”或者“.”，在对公式中的项进行介绍时，跨行使用 where 且 不空两格。
  - 在公式中使用min、log、LOS、arctan、exp等固定名称时需要使用\text{}形式。
- 论文中所有的参数均需要写成公式$$形式，而不是直接打出。
- 善用图表，力求表达形式多样，以使人加深理解
    - 图名、图中的legend，x-ylabel、表内名称均为首字母大写
    - 表头所有字母都为大写

## 参考文献
- 关于参考文献的引用
    - 如果超过两句话以上直接引用对方的原话，通常应该打双引号并用斜体表明出处
    - 如果大段引用/抄袭文献又造成读者误解，则视为学术不端，即抄袭
    - 在图表引用时，必需在图表处给出引用的文献，不能仅在正文中提及。
    - 在句首进行参考文献引用时，需要写出第一作者名字 et al.再写出引文。
 
标准引用格式说明
- Please number citations consecutively within brackets [1].The sentence punctuation follows the bracket [2]. Refer simplyto the reference number,as in[3]—do not use“Ref.[3]”or“reference [3]”'except at the beginning of a sentence:“Reference [3] was the first ...”
- Number footnotes separately in superscripts. Place the ac-tual footnote at the bottom of the column in which it wascited. Do not put footnotes in the abstract or reference list.Use letters for table footnotes.
- Unless there are six authors or more give all authors' names;do not use “et al.". Papers that have not been published,even if they have been submitted for publication, should becited as “unpublished”[4]. Papers that have been accepted forpublication should be cited as“in press”[5]. Capitalize onlythe first word in a paper title, except for proper nouns andclement symbols.
- For papers published in translation journals, please give theEnglish citation first, followed by the original foreign-languagecitation [6].

- 标准引用格式示例
[1] G. Eason,B. Noble,and L. N. Sneddon,"On certain integrals of Lipschitz-Hankel type involving products of Bessel functions,”Phil.Trans. Roy.Soc. London,vol.A247, pp. 529-551,Apr. 1955.
[2] J.Clerk Maxwell, A Treatise on Electricity and Magnetism, 3rd ed., vol.2.Oxford: Clarendon,1892,pp.68-73.
[3] L S.Jacobs and C.P. Bean,"Fine particles, thin films and exchange anisotropy,” in Magnetism,vol. III, G.T. Rado and H. Suhl, Eds. NewYork: Academic, 1963, pp. 271-350.
[4] K.Elissa,"Title of paper if known,"unpublished.
[5] R.Nicole, "Title of paper with only first word capitalized,”J. Name Stand.Abbrev., in press.
[6] Y. Yorozu, M. Hirano, K. Oka, and Y. Tagawa,"Electron spectroscopy studies on magneto-optical media and plastic substrate interface,”IEEETransl. J. Magn. Japan, vol. 2, pp. 740-741, Aug. 1987 [Digests 9thAnnual Conf. Magnetics Japan, p. 301,1982].
[7] M. Young, The Technical Writer's Handbook. Mill Valley, CA: University Science,1989.



