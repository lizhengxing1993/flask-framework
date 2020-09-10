# flask基础架构

## 项目目标
    集成了中小型web项目使用的工具类组件，让用户无需考虑项目搭建，只开发自己的业务逻辑就好了
## 项目结构
```text

flask-framework
    |-- .tox
    |-- apps # 蓝图，放所有的app
    |-- logs # 日志
    |-- test # 测试
    |-- tools # 工具
    |-- app.py # 项目入口
    |-- config.py # 配置文件
    |-- requirements.txt # 项目依赖包
    |-- tox.ini # 虚拟环境配置
```  
## 项目开发
### 依赖python版本
    python3.7
### 安装tox
    pip install tox
### 创建虚拟环境
    tox -e dev
### 启动项目
    .tox/dev/bin/python app.py
