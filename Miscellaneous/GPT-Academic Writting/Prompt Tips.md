
 # Prompt Tips

为了让ChatGPT更加准确的回答和解决有关论文方面的问题，通常需要一些prompt tips，以下从3个方面展示：

 1. 论文润色 (gpt-3.5)

 2. 摘要生成 (gpt-3.5)

 3. 优化问题求解目标推理 (gpt-4.0)


## 1. 论文润色
ChatGPT是无数语料喂出来的，可以把它想象成许多作家聚在一起，根据海量的文字资料来帮你写东西。如果你只给一个很一般性的要求，它就只能给你生成一个一般性的、用在哪里都行但是用在哪里都不是最恰当的内容。可是，如果你把要求说得更详细，给出的情景更具体，它就能创作出专门为你定制的内容，更符合你的需求。

### 角色设定

在与ChatGPT展开对话之前，一个好的办法是可以先让它进入特定角色，尤其GPT-4有强大的角色扮演能力。

比较常用的一个方法是请他扮演一个专业的论文评审专家，对论文草稿给出评审意见，然后根据意见，去重新审视论文，这样可以让它的表达更加准确。

```
Prompt: You are now acting as an expert in the field of [Put professional fields here…]. From a professional point of view, do you think there is any need to modify the above content? Be careful not to modify the whole text, you need to point out the places that need to be modified one by one, and give revision opinions and recommended revision content.
```

提示：你现在扮演一个[这里放你所研究的领域] 领域的专家，从专业的角度，您认为上面这些内容是否有需要修改的地方？ 注意，不要全文修改，您需要一一指出需要修改的地方，并且给出修改意见以及推荐的修改内容。

### 多版本参考

在润色过程中，ChatGPT可以提供多个版本的修改建议，以便对比和选择。
```
Prompt: Please provide multiple versions for reference.
```

### 及时反馈

如果ChatGPT理解错了你的问题，可以给它一个错误的反馈，让它重新回答
```
Prompt: Note that it is not …, but …

Re-answer the previous question based on what I have added.

```

如果认为回答的不够好，或者方向不对。可以要求重新回答，并且指明侧重方向。比如你只希望去除当前段落的冗余，并不想改动原意思。

```
Prompt：Still the above question, I think your answer is not good enough. Please answer again, this time focusing on removing redundancy from this passage.

```

### 前后对比

如果文本还是过长不利于观察，让它回答具体修改了哪些地方。
```
Prompt：Note that in addition to giving the modified content, please also indicate which paragraphs and sentences have been modified in the revised version.
```

补充：这里可以用markdown table，更加一目了然。

```
List all modification and explain the reasons to do so in markdown table.
```

### 润色方向
根据自己的需求调整润色方式。以下列举了一些常用词汇，可与后文的示例结合使用。


- 更精确的措辞（More precise）：选择更精确的词汇，例如使用“generate”代替“produce”或“analyze”代替“look at”。

- 更简练的表达（More concise）：消除不必要的词语和短语，使句子更加清晰、直接。

- 更客观的语言（More objective）：删除主观性语言，以中立的方式呈现信息。

- 更具体的描述（More specific）：提供更具体的细节，以支持论点或想法。

- 更连贯的表达（More coherent）：确保句子组织良好，逻辑流畅。

- 更一致的风格（More consistent）：确保句子所使用的语言和风格与论文的其余部分一致。

- 更符合学术风格（More academic）：使用学术写作中常用的术语和短语，例如“furthermore”和“thus”。

- 更正式的语法（More formal grammar）：使用正确的语法和句法，例如避免句子碎片或跑题的句子。

- 更具细节的描述（More nuanced）：通过使用词语或短语来传达更复杂或微妙的含义，使句子更具细节。


### 润色程度

在使用ChatGPT的过程中，有时候我们并不希望AI对文本进行大幅修改，这时候可以要求它对润色的程度和方向进行限制，以下是一些可以有助于控制润色程度的口令，请大家尝试加入自己的提示词中。

- “Subtle edits only”: 仅对文本进行微调

- “Minor edits”: 进行一些小的编辑

- “Rephrase for clarity”: 改写以提高表达清晰度

- “Simplify sentence structure”: 简化句子结构

- “Check grammar and spelling”: 检查语法和拼写

- “Enhance flow and coherence”: 提高文本流畅度和连贯性

- “Improve word choice”: 改善用词

- “Revise for style”: 为文本调整风格

- “Significant edits”: 进行重大编辑

- “Restructure content”: 重新构建内容

### 段落润色

#### 可以直接润色，
句内的latex公式会自动识别，但大段公式不会修改，会原样输出。
```
Prompt: Below is a paragraph from an academic paper. Polish the writing to meet the academic style, improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence. 
```

或者

```
Rephase the above for more available to a journal paper writing.
```

#### 也可以一步一步引导它，润色论文。

 Step1: 引导1:
```
I'm going to give you some information before asking you to write an English article. Do you understand?
```
 Step2: 引导2:
```
When it comes to writing content, two factors are crucial, "perplexity" and "burstiness." Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. Al sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Do you understand?
```
 Step3: 重写指令：
```
using the concepts written previously, rewrite the article with a high degree of perplexity and burstiness: ${内容}
```
![image](https://user-images.githubusercontent.com/90384476/232736102-461fb950-ffff-48fa-8c25-70f3c0ab02da.png)


#### 有时，如果英文不够好或者对修改之后的句子感觉不合适，可以接着让它输出一句理由。然后自己再做最终的判断。

```
Prompt：For the sentence “[Before polished sentence]”, why did you polish it to be “[Polished sentence]”.
List all modification and explain the reasons to do so in markdown table.
```

#### 也可以结合特定要求，进一步追问。相比于上面直接的润色，这种方式可能会让它输出一些更丰富的信息。

1）结合背景知识

```
Prompt: According to your knowledge about XXX and XXX, is there a better way to write the above paragraph, please help to revise it so that it can be used in academic papers.
```

2）长句拆分

```
Prompt: This sentence is too long and complex. Consider breaking it up into multiple shorter sentences.
```
3）去除冗余

```
Prompt: This section seems repetitive. Please rephrase to avoid redundancy.
```

### 语法句法

- 整段内容语法检查，参考中科院插件。
```
Can you help me ensure that the grammar and the spelling is correct? Do not try to polish the text, if no mistake is found, tell me that this paragraph is good. If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, put the original text the first column, put the corrected text in the second column and highlight the key words you fixed.
Example:
Paragraph: How is you? Do you knows what is it?
| Original sentence | Corrected sentence |
| :--- | :--- |
| How **is** you? | How **are** you? |
| Do you **knows** what **is** **it**? | Do you **know** what **it** **is** ? |
Below is a paragraph from an academic paper. You need to report all grammar and spelling mistakes as the example before. [内容]
```

- 语态检查

```
Prompt: The subject and verb do not agree in this sentence. Please correct.
```

- 语态转换

被动语态改为主动语态

```
Prompt: I have used a passive voice in this sentence. Consider using an active voice instead.
```

### 场景举例

可以让ChatGPT帮你列举一些之前的方法有局限性的场景，以便用于论文中。 

```
Prompt: Can you give a few examples to demonstrate the scenarios where the previous method has limitations, so that it can be used in academic papers.
```

### 期刊/会议风格

根据期刊会议 (期刊或者会议论文要足够多) 的风格，来润色内容。

```
Prompt: If I wish to publish a paper at a [XXX] conference, please polish the above content in the style of a [XXX] article.
```

### 封装基本事实/原理/背景（必须在同一对话内）

如果一些新兴的理论或原理，GPT可能会错误的修改。如果对内容的润色需要一些背景知识，可以在对话时主动告诉ChatGPT，比如XXX原理。

```
Prompt: Now, in order to help me better polish my thesis, I need you to remember the [XXX] principle: “原理内容”
```

这样就相当于为一段内容，封装了一个函数名称，之后你再次提到XXX原理的时候，ChatGPT就能快速知道你说的是哪些基本事实了。

## 2.摘要生成 (gpt-3.5)

Step1: 引导1:
```
I'm going to give you some information before asking you to write an English academic article about wireless communication and artificial intelligence. Do you understand?
```
Step2: 引导2:
```
When it comes to writing content, two factors are crucial, "perplexity" and "burstiness." Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. Al sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Do you understand?
```
Step3: 重写指令：
```
using the concepts written previously, summarize the content of this article as an abstract no more than 200 words with a high degree of perplexity and burstiness: ${内容}
```
### 也可以根据自己的需求，添加关键词。

Step1: 引导1:

I'm going to give you some information before asking you to write an English academic article about wireless communication and artificial intelligence. Do you understand?
Step2: 引导2:
When it comes to writing content, two factors are crucial, "perplexity" and "burstiness." Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. Al sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Do you understand?
Step3: 重写指令：
using the concepts written previously, summarize the content of this article as an abstract no more than 200 words with a high degree of perplexity and burstiness: ${内容}









## 3.优化问题求解目标推理 (gpt-4.0)

GPT4.0的使用体验，相比于GPT3.5有了完全不一样的提升… 尤其是在逻辑推理阶段。GPT3.5一个明显的特点是你只要对AI的回答进行反驳，它便会立刻改变立场并承认错误。而GPT 4.0则更多地基于事实进行回答，表现出更高的稳定性。

因此，我们可以尝试使用GPT4.0 推理一些经典优化问题。

为了让ChatGPT更加准确的回答和解决有关问题，你需要一步一步引导它思考。

首先，需要将优化问题描述清楚，包括变量物理意义，约束公式等等。公式可以使用letex格式，最好使用表格样式一一对应变量与描述，并且针对优化变量一定要写在优化目标下，如下：



此外，GPT 4.0能够阅读更长的文本，拥有更长的记忆窗口，这使得它能够在通篇润色方面发挥更大作用。  4.0-API申请 https://openai.com/waitlist/gpt-4

逻辑论证辅助
GPT 4.0在逻辑推理方面有显著的提升，可以用于辅助构建更有说服力的论证。
```
Prompt: Please help me analyze and optimize the logical structure of this argument to make it more convincing.

提示：请帮我分析和优化这段论证的逻辑结构，以使其更具说服力。
```
长篇文本处理能力
由于GPT 4.0具有更长的记忆窗口，它可以更有效地进行长篇幅文本的润色。
```
Prompt: Please read and polish the entire paper to ensure consistency and coherence.

提示：请阅读并润色整篇论文，确保一致性和连贯性。（就是这么简单粗暴！）
```
当然，如果论文特别长，可以分为多次喂给它，像下面这样：

给完第一部分之后：

```
Prompt: I have written the XXX section, but I am not satisfied with its structure and coherence. Please help me reorganize the content and improve its coherence.

提示：我写了XXX部分，但我对其结构和连贯性不满意。请帮我重新组织内容，提高其连贯性。
```
```
Prompt: Please review and revise the entire literature review section of my paperensuring that it meets the standards of academic writing and the content iscoherent and well-structured.

提示：请审查并修改我论文的整个文献综述部分，确保符合学术写作标准，内容连贯且结构合理。
```

提供独特见解

```
Prompt: Please provide me with some unique insights that I can discuss in my paper, based on the latest research that you are aware of.

提示：请根据你所了解的最新研究，为我提供一些独特的见解以便我在论文中进行讨论。
```

深度分析与评估

```
Prompt: Please help me to conduct an in-depth analysis of these research methods and data, and provide me with an assessment of their advantages and disadvantages.

提示：请帮助我对这些研究方法和数据进行深度分析，并为我提供关于其优缺点的评估。
```





有研究表明，仅仅是在提示语中加一句「以下是一段论文引言中的话」或者「请依次考虑我给出的中的各个条件」，都能明显提高ChatGPT的准确率。它是个心直口快的AI，有时候就是需要你提醒它刻意进行慢思考。


不妨试试，在提示词后面，紧跟一句“请一步步思考”，“请一步步考虑”，“请务必认真回答”，“如果你认为无法根据已知信息安全修改论文，请回答否”之类的词，可以使得其回答的准确率大大提高。有时候在提示语后面给个提醒，它会变得完全不一样。

也许仅仅是这一条启示，就能给我们莫大的启发。

节省空间

最近自己一直在用的一个提示，可以说终于摆脱了之前一次输出不完整或者中间断网的情况。

这种方式改文章，改代码都可以。
```
Prompt: [Put your requirements here…] , since your output length is limited, in order to save space. Please use ellipses for the parts you don’t think need to be modified.
```
提示：[这里放你的要求…]，由于你的输出长度有限，为了节省空间。请你觉得没必要修改的部分，用省略号即可。

4.0-API申请
https://openai.com/waitlist/gpt-4
