# 诡镇奇谈卡牌数据处理器

<div align="center">

  [![English](https://img.shields.io/badge/🌐-English-blue.svg?style=for-the-badge)](README_EN.md)

  ---

  [![Python](https://img.shields.io/badge/Python-3.6%2B-green.svg)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## 📖 项目概述

这是一个专为《诡镇奇谈：卡牌版》桌游设计的Python工具，用于自动化处理卡牌数据的批量转换和模板化。该工具能够将原始卡牌数据转换为标准化的JSON格式，并生成适用于Tabletop Simulator等虚拟桌游平台的卡牌包。

## ✨ 功能特性

- 🔄 **批量处理** - 自动处理数据源目录中的所有JSON文件
- 🆔 **GUID生成** - 为缺失GUID的卡牌自动生成唯一标识符
- 📋 **模板化转换** - 基于预定义模板将卡牌数据标准化
- 🧹 **文件名清理** - 自动清理文件名，保留中文、字母和数字
- 📦 **列表模板生成** - 自动创建卡牌包的列表配置文件

## 🚀 快速开始

### 系统要求

- Python 3.6+
- 依赖库：`json`, `os`, `random`, `re`, `shutil`, `pathlib`, `typing`

### 安装配置

1. **目录结构**：
   ```
   诡镇奇谈生成内容包/
   ├── card_processor.py    # 主处理脚本
   ├── source/             # 数据源目录
   ├── template/           # 模板目录
   └── output/             # 输出目录（自动创建）
   ```

2. **准备数据**：
   - 将原始JSON文件放入 `source/` 目录
   - 确保文件包含Tabletop Simulator格式的Bag对象

### 运行程序

```bash
python card_processor.py
```

程序将自动处理所有数据文件并生成标准化的卡牌包。

## 📁 输出说明

### 生成文件结构

```
output/
├── 数据包名.GUID/
│   ├── 卡牌1.GUID.json
│   ├── 卡牌2.GUID.json
│   └── ...
└── 数据包名.GUID.json    # 列表模板
```

## ⚙️ 高级配置

### 自定义目录

```python
processor = CardProcessor(
    source_dir='你的数据源目录',
    template_dir='你的模板目录',
    output_dir='你的输出目录'
)
```

## 🔧 故障排除

### 常见问题

| 问题 | 解决方案 |
|------|----------|
| 找不到Bag对象 | 检查源文件是否包含名为"Bag"的对象 |
| 模板文件加载失败 | 验证template目录中的JSON文件格式 |
| GUID生成问题 | 确保random模块正常工作 |

## 📋 版本信息

- **版本号**：v1.0.0
- **发布日期**：2025年1月26日
- **兼容性**：Tabletop Simulator
- **Python要求**：3.6+
- **许可证**：MIT License

---

<div align="center">

  <sub>用 ❤️ 为《诡镇奇谈》爱好者制作</sub>

</div>