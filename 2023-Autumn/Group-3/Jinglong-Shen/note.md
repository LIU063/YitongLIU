# 20231107


## LeNet5 (CIFAR10 | FMNIST | MNIST)
<div style="display:inline-block">
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/4bd04d78-377a-45f1-af17-deee0d6e191f"/>
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/8a0dea5b-6dc9-4cfc-b539-839ee3b58ee7"/>
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/6623b663-c2fd-4959-8ebc-0be14e0ca312"/>
</div>

## MLP (CIFAR10 | FMNIST | MNIST)
<div style="display:inline-block">
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/d4e43009-9786-48d3-babf-6b30e6dc5128"/>
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/b56663b9-ca8e-4255-9652-d447fea4c459"/>
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/4f2f8643-a132-46dc-ba7d-206ae5d79788"/>
</div>

## Effect of Client Number | Effect of Non-IID Dataset | Ablation Study
<div style="display:inline-block">
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/3c2d6a1e-5b68-4fca-8094-3e0aa2c74bb0"/>
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/79d5b934-c05b-468c-8bec-e4c1e469c6df"/>
  <img width=32% alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/188f2295-0331-4212-9c8f-55c50ec6c364"/>
</div>

![FedTune训练流程](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/51dc5cc8-a427-446b-80ab-8f7bb94fa1b4)

# 20231030

1. 添加新的数据集进行实验：FMNIST，SVHN

2. 攥写论文初稿

# 20231016

## CNN & CIFAR10

![cnn_benchmarks](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/b620e815-59b2-49e9-ae71-795de2637d8b)

## MLP & MNIST

![mlp_benchmarks](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/7dfd78c2-3a77-4064-94a3-ccbe89af03c2)

## Effect of Client Number

![client_num](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/34d7b141-606d-4b0d-821a-d55c3ada1583)

## Ablation Study & Effect of Non-IID Dataset

![ablation](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/b95f7040-cd72-49dc-bf58-efda2f9d9116)

# Week 3

<div style="display:inline-block">
  <img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/154ec383-2ce7-439a-9f4d-02f0bd7d48ba"/>
  <img width="500" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/9d775246-589b-41a5-a0b2-407bc42986c2"/>
</div>

## Reward of Different Clients

<div style="display:inline-block">
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/ee194ed2-b202-4282-a5ee-416e433f65ee"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/d0f0bcf8-2ad4-4b27-97ed-f93d11c2ce1f"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/87bf5feb-7a56-4830-9485-d6e0928656af"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/bf0c636e-285e-422f-94b5-9eeeadfb75eb"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/ea1e9b61-0e67-4eae-b82b-7ebd1a0ab195"/>
</div>

## Sampled Learning Rate of Different Clients

<div style="display:inline-block">
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/7de5521e-6ca7-45c1-ab0b-d06ddc63068c"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/8441331f-a3fc-4276-b981-8fc55105ffb3"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/5b81159e-018d-40ac-b2e8-e1da5571609f"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/ce19bb13-dea9-4ef9-9151-55567a9cb19d"/>
  <img width="198" alt="image" src="https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/81b71c05-24da-4c39-ab13-a572ee6d5564"/>
</div>

## Simulation Plan

### Different Tasks
验证在不同任务下的有效性

- **Text**: Dataset: Twitter(情感分类数据集)
- **Graph** Dataset: Graph-DC(图分类数据集)
- **Image** Dataset: CIFAR10

### Ablation Experiment of Reward Assignment
验证奖励分配机制是否起作用

### Effect of Different $\alpha$
验证数据集Non-IID程度的影响

### Personal v.s. Non-Personal
验证个性化的必要性

# Week 1-2

[Personalized Hyper-parameter Tuning for Federated Learning](/2023-Autumn/Group-3/Jinglong-Shen/assets/Personalized%20Hyper-parameter%20Tuning%20for%20Federated%20Learning.pdf)

## Benchmarks

### Ours

Accuracy (best ever seen): 0.5774  
Communication Cost: 200 rounds

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/45201a7b-4443-4b77-b821-6c2d8fb2e0d2)

### Random Search

Accuracy (best ever seen): 0.5432  
Communication Cost: 711 rounds

<!-- ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/a1d4bb33-0b33-475b-ae73-8b113ff91d6e) -->
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/ef1c2b39-6d22-4d89-b0b0-5e151b41061a)


### Hyperband

Accuracy (best ever seen): 0.47  
Communication Cost: 635 rounds

<!-- ![image](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/cbfcc6b1-6998-431c-a130-87df6cd843d9) -->
![image](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/687e14ac-f0a6-4d6c-b0a1-daec8122ef27)


### Bayesian Optimization

Accuracy (best ever seen): 0.5829  
Communication Cost: 2000 rounds

![image](https://github.com/UNIC-Lab/Weekly-Report/assets/36980478/7b8f0dea-b98c-4ff9-ae79-d23d16ad7d74)

### HPN


---

