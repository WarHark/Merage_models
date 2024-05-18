# Introduction : Merage_models

**Merage two different  models into one model which model has the ability of both different models**

# How to use

**1.创建环境**

```
conda create -n zipit python=3.7
conda activate zipit
pip install torch torchvision torchaudio
pip install -r requirements.txt
```

**2 训练,train, you can use cifar_resnet_training (datasets:cifar10) or cifar5_resnet_training (datasets:cifar100)**

```
nohup python -u -m non_imnet_training_scripts.cifar_resnet_training >> out.log 2>&1 & 
```

**会在checkpoints文件中存储初始模型结果**

**3 评估,evaluation**
**3.1 初始模型的效果get the base models evaluation**

```
python  -m non_imnet_evaluation_scripts.base_model_concept_merging
```

**3.2 合并模型的效果get the merage model's evaluation**

```
python  -m non_imnet_evaluation_scripts.zipit_concept_merging
```

**结果会保存在csv文件中，可用excel表打开，查看结果数据**

