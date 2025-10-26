# Arkham Horror Card Data Processor

<div align="center">

  [![中文](https://img.shields.io/badge/🌐-中文-red.svg?style=for-the-badge)](README.md)

  ---

  [![Python](https://img.shields.io/badge/Python-3.6%2B-green.svg)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## 📖 Project Overview

This is a Python tool specifically designed for the *Arkham Horror: The Card Game* board game, used for automated batch processing and templating of card data. This tool converts raw card data into standardized JSON format and generates card packs suitable for virtual tabletop platforms like Tabletop Simulator.

## ✨ Features

- 🔄 **Batch Processing** - Automatically processes all JSON files in the source directory
- 🆔 **GUID Generation** - Automatically generates unique identifiers for cards missing GUIDs
- 📋 **Template Conversion** - Standardizes card data based on predefined templates
- 🧹 **Filename Cleanup** - Automatically cleans filenames, retaining Chinese characters, letters, and numbers
- 📦 **List Template Generation** - Automatically creates list configuration files for card packs

## 🚀 Quick Start

### System Requirements

- Python 3.6+
- Dependencies: `json`, `os`, `random`, `re`, `shutil`, `pathlib`, `typing`

### Installation & Setup

1. **Directory Structure**:
   ```
   Arkham Horror Card Generator/
   ├── card_processor.py    # Main processing script
   ├── source/             # Source directory
   ├── template/           # Template directory
   └── output/             # Output directory (auto-created)
   ```

2. **Prepare Data**:
   - Place raw JSON files in the `source/` directory
   - Ensure files contain Tabletop Simulator formatted Bag objects

### Run Program

```bash
python card_processor.py
```

The program will automatically process all data files and generate standardized card packs.

## 📁 Output Description

### Generated File Structure

```
output/
├── PackName.GUID/
│   ├── Card1.GUID.json
│   ├── Card2.GUID.json
│   └── ...
└── PackName.GUID.json    # List template
```

## ⚙️ Advanced Configuration

### Custom Directories

```python
processor = CardProcessor(
    source_dir='your_source_directory',
    template_dir='your_template_directory',
    output_dir='your_output_directory'
)
```

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Bag object not found | Check if source file contains an object named "Bag" |
| Template file loading failed | Verify JSON file format in template directory |
| GUID generation issues | Ensure random module is working properly |

## 📋 Version Information

- **Version**: v1.0.0
- **Release Date**: January 26, 2025
- **Compatibility**: Tabletop Simulator
- **Python Requirements**: 3.6+
- **License**: MIT License

---

<div align="center">

  <sub>Made with ❤️ for Arkham Horror enthusiasts</sub>

</div>