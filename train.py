'''利用训练集进行训练'''

from pathlib import Path
from collections import Counter
from dataclasses import dataclass, field
from utils import check_file
import jieba
import json

from config import *


@dataclass
class Category:
    name:str
    cnt:int = 0
    data:dict[str, int] = field(default_factory=Counter)

    def new_sentence(self, words:set[str]):
        '''增加新句子的特征'''
        self.cnt += 1
        self.data += Counter(words)

    def to_dic(self) -> dict:
        '''转化为字典'''
        return {
            "count": self.cnt,
            "data": self.data
        }

    def save_model(self, file_path:Path):
        '''将Category模型保存为json文件'''
        check_file(file_path)
        with open(file_path, "w", encoding="UTF-8-sig") as f:
            json.dump(self.to_dic(), f)
        print(f"类别 {self.name} 的统计模型已保存。")


def statistic(path:Path, name:str = '', result:Category=None, max_count = 0):
    '''对目标训练文本目录进行递归统计，并保存结果'''
    if not result:
        result = Category(name)
    for sub in path.iterdir():
        if sub.is_file():
            with open(sub, "r", encoding="UTF-8-sig") as f:
                while (sentence := f.readline()) and (max_count and result.cnt < max_count):
                    words = set(jieba.cut(sentence, cut_all=True))
                    result.new_sentence(words)
        else:
            statistic(path, result=result, max_count=max_count)
    save_path = model_path / f"{name}.category"
    result.save_model(save_path)
    

if __name__ == '__main__':
    for category in categories_info:
        statistic(category["path"], category["name"], max_count=max_count)
    print("所有标签已训练完成~")