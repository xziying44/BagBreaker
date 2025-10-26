#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
卡牌数据处理器
用于处理诡镇奇谈卡牌数据的批量转换和模板化
"""

import json
import os
import random
import re
import shutil
from pathlib import Path
from typing import Dict, List, Any


class CardProcessor:
    def __init__(self, source_dir: str = "数据源", template_dir: str = "模板", output_dir: str = "输出"):
        self.source_dir = Path(source_dir)
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)

        # 确保输出目录存在
        self.output_dir.mkdir(exist_ok=True)

        # 加载模板
        self.card_template = self._load_template("单个卡牌.json")
        self.list_template = self._load_template("列表模板.json")

    def _load_template(self, template_file: str) -> Dict[str, Any]:
        """加载模板文件"""
        template_path = self.template_dir / template_file
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"加载模板文件 {template_file} 失败: {e}")
            return {}

    def generate_guid(self) -> str:
        """生成6位随机GUID，每位为1-9和小写a-f"""
        chars = '123456789abcdef'
        return ''.join(random.choice(chars) for _ in range(6))

    def clean_filename(self, nickname: str) -> str:
        """清理文件名，只保留中文和字母"""
        # 移除所有符号，只保留中文、字母和数字
        cleaned = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', nickname)
        return cleaned if cleaned else "Unknown"

    def process_source_files(self):
        """处理所有数据源文件"""
        for source_file in self.source_dir.glob("*.json"):
            print(f"正在处理文件: {source_file.name}")
            self.process_source_file(source_file)

    def process_source_file(self, source_file: Path):
        """处理单个数据源文件"""
        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"读取文件 {source_file} 失败: {e}")
            return

        # 查找Bag对象
        bag_object = self._find_bag_object(data)
        if not bag_object:
            print(f"在文件 {source_file} 中未找到Bag对象")
            return

        bag_guid = bag_object.get("GUID", "")
        if not bag_guid:
            print(f"Bag对象GUID为空，跳过处理")
            return

        # 创建输出目录
        output_subdir = self.output_dir / f"{source_file.stem}.{bag_guid}"
        output_subdir.mkdir(exist_ok=True)

        # 获取卡牌列表
        cards = bag_object.get("ContainedObjects", [])
        if not cards:
            print(f"Bag对象中没有找到卡牌数据")
            return

        print(f"找到 {len(cards)} 张卡牌")

        # 处理每张卡牌
        card_files = []
        updated_cards = []

        for i, card in enumerate(cards):
            if card.get("Name") != "Card":
                continue

            # 检查并生成GUID
            if not card.get("GUID") or card.get("GUID") == "":
                new_guid = self.generate_guid()
                card["GUID"] = new_guid
                print(f"为卡牌 {i + 1} 生成GUID: {new_guid}")

            # 创建模板化卡牌
            template_card = self.create_template_card(card)

            # 生成文件名
            nickname = card.get("Nickname", f"Card_{i + 1}")
            clean_name = self.clean_filename(nickname)
            filename = f"{clean_name}.{card['GUID']}.json"

            # 保存卡牌文件
            card_path = output_subdir / filename
            with open(card_path, 'w', encoding='utf-8') as f:
                json.dump(template_card, f, ensure_ascii=False, indent=2)

            card_files.append(filename.replace('.json', ''))
            updated_cards.append(card)

        # 更新源文件中的GUID
        bag_object["ContainedObjects"] = updated_cards
        with open(source_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # 创建列表模板
        self.create_list_template(output_subdir, bag_guid, card_files)

        print(f"处理完成，输出到: {output_subdir}")

    def _find_bag_object(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """查找Bag对象"""
        object_states = data.get("ObjectStates", [])
        for obj in object_states:
            if obj.get("Name") == "Bag":
                return obj
        return None

    def create_template_card(self, card: Dict[str, Any]) -> Dict[str, Any]:
        """创建模板化的卡牌对象"""
        template = self.card_template.copy()

        # 填充字段
        template["CardID"] = card.get("CardID", 0)
        template["CustomDeck"] = card.get("CustomDeck", {})
        template["GMNotes"] = card.get("GMNotes", "")
        template["GUID"] = card.get("GUID", "")
        template["Nickname"] = card.get("Nickname", "")
        template["SidewaysCard"] = card.get("SidewaysCard", False)

        return template

    def create_list_template(self, output_dir: Path, bag_guid: str, card_files: List[str]):
        """创建列表模板"""
        template = self.list_template.copy()

        # 填充字段
        template["ContainedObjects_order"] = card_files
        template["ContainedObjects_path"] = output_dir.name
        template["GUID"] = bag_guid

        # 保存列表模板
        list_file = self.output_dir / f"{output_dir.name}.json"
        with open(list_file, 'w', encoding='utf-8') as f:
            json.dump(template, f, ensure_ascii=False, indent=2)

        print(f"创建列表模板: {list_file}")


def main():
    """主函数"""
    print("开始处理卡牌数据...")

    processor = CardProcessor(source_dir='source', template_dir='template', output_dir='output')
    processor.process_source_files()
    processor.process_source_files()

    print("处理完成！")


if __name__ == "__main__":
    main()
