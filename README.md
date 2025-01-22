# 太空探索 Python 课程环境配置指南

本指南将帮助您配置运行太空探索 Python 课程所需的开发环境。请按照以下步骤操作：

## 前置要求

- 安装 [Anaconda](https://www.anaconda.com/download) 或 [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)

## 环境配置步骤

### 1. 创建并激活 Conda 环境

```bash
# 创建名为 space-py 的 Python 3.8 环境
conda create -n space-py python=3.10

# 激活环境
# Windows
conda activate space-py
# macOS/Linux
source activate space-py
```

### 2. 安装依赖包

```bash
# 确保当前目录包含 requirements.txt 文件
pip install -r requirements.txt
```

### 3. 启动 Jupyter Notebook

```bash
jupyter notebook
```

## 常见问题解决

### Q1: conda 命令未找到
- Windows: 请确保已将 Anaconda 添加到系统环境变量
- macOS: 请确保已运行 `conda init` 初始化命令

### Q2: pip 安装包失败
- 检查网络连接
- 尝试使用国内镜像源：
  ```bash
  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

### Q3: Jupyter Notebook 无法启动
- 确保已正确安装 jupyter：`pip install jupyter`
- 检查是否在正确的 conda 环境中：`conda env list`

## 环境验证

启动 Jupyter Notebook 后，打开 `space_mission_demo.ipynb` 文件，运行第一个代码块进行环境验证。如果没有报错，说明环境配置成功。

## 注意事项

- 请确保使用 Python 3.8 版本，以保证最佳兼容性
- 建议定期更新依赖包：`pip install --upgrade -r requirements.txt`
- 如遇到问题，请先检查是否已激活正确的 conda 环境

## 技术支持

如果您在配置过程中遇到任何问题，请：
1. 查看上述常见问题解决方案
2. 确保使用最新版本的 Anaconda/Miniconda
3. 记录错误信息以便技术支持人员协助解决