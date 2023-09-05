<p id="table"></p>

## Table of Contents

- <a href="#1"> Week 1 (2023.09.01 – 2023.09.06)


<br/>

------

<br/>

<p id="1"></p>

# <a href="#table">Week 1 (2023.09.01 – 2023.09.06)</a>

## VoI画图
效果良好，准备这周赶紧写了

## 大模型求解优化问题

把 $x_i$, $f(x_i)$, $f'(x_i)$, $f"(x_i)$, 当作token四个一组的输入到transformer中，sequence长度可以等效成迭代次数，每次大模型输出下一个 $x_{i+1}$, 然后补充 $f(x_{i+1})$, $f'(x_{i+1})$, $f"(x_{i+1})$到sequence中
