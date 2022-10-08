'''相关小工具'''

from typing import Union
from pathlib import Path


def check_dir(path: Union[str, Path]) -> bool:
    '''
    检查目录是否存在，并递归创建目标目录，若目录已存在则不进行更改。
    :param path: 目标目录路径
    :rtype: 返回该目录是否本就存在
    '''
    path = Path(path)
    if path.is_dir():
        return True
    else:
        check_dir(path.parent)
        path.mkdir()
        return False


def check_file(path: Union[str, Path]):
    '''
    检查文件是否存在，并递归创建父目录和该文件，若文件已存在则不进行更改。
    :param path: 目标文件路径
    :rtype: 返回该文件是否本就存在
    '''
    path = Path(path)
    if path.is_file():
        return True
    else:
        check_dir(path.parent)
        with open(path, "w"):
            pass
        return False


def mul(nums:list[Union[float, int]]) -> Union[float, int]:
    '''
    将数组中元素一一相乘
    '''
    ans = 1
    for num in nums:
        ans *= num
    return ans