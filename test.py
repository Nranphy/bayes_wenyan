'''利用测试集进行判定'''

from config import *
from bayes import bayes
from pathlib import Path

def single_test(category_name:str, flag:int, logger=True):
    '''
    对目标测试集进行分类测试
    :param flag: 正确的分类器返回值
    :param logger: 是否在控制台输出分类失败和分类错误的句子
    '''
    test_file = test_path / f"{category_name}.test"
    if not test_file.is_file():
        raise Exception(f"找不到目标文件 {test_file}")
    total_cnt, correct_cnt, unkown_cnt = 0,0,0
    false_sentence, unkown_sentence = [],[]
    with open(test_file, "r", encoding="UTF-8-sig") as f:
        while sentence := f.readline():
            result = bayes(sentence, False)
            total_cnt += 1
            if not result:
                unkown_sentence.append("【分类失败】"+sentence)
                unkown_cnt += 1
            elif result == flag:
                correct_cnt += 1
            else:
                false_sentence.append("【分类错误】"+sentence)

    false_sentence = '\n'.join(false_sentence)
    unkown_sentence = '\n'.join(unkown_sentence)
    if logger:
        print(false_sentence)
        print(unkown_sentence)
    result = (
        "=========\n"
        f"类别【{category_name}】测试结果：\n"
        f"测试总数：{total_cnt}\n"
        f"正确数：{correct_cnt}\n"
        f"分类失败数：{unkown_cnt}\n"
        f"正确率:{correct_cnt/(total_cnt-unkown_cnt):.2%} （已去除分类失败数）\n"
        f"错误率:{(total_cnt-unkown_cnt-correct_cnt)/(total_cnt-unkown_cnt):.2%} （已去除分类失败数）\n"
        "=========\n"
        f"分类器 res_retio 值为 {res_retio}\n"
        "=========\n"
        )
    print(result)
    with open(test_path / f"{category_name}.result", "w", encoding="UTF-8-sig") as f:
        f.write(result)
        f.write(false_sentence)
        f.write(unkown_sentence)

def global_test(logger=True):
    '''对config中所提所有类别进行分类测试'''
    for category in categories_info:
        single_test(category["name"], category["rflag"], logger=logger)


if __name__ == "__main__":
    global_test(False)