'''利用朴素贝叶斯进行文言白话的判断'''

import json
import jieba


from config import *
from utils import mul


def get_words_count(words:set[str], category_name:str) -> tuple[int]:
    '''获得各个分词在所指类别模型中的频数'''
    category_path = model_path / (category_name+".category")
    if not category_path.is_file():
        raise Exception(f"找不到目标路径 {category_path}")
    with open(category_path, "r", encoding="UTF-8-sig") as f:
        category_data:dict = json.load(f)
    return ((category_data["data"].get(word, 0)+1)  for word in words if word not in punctuation) #进行了拉普拉斯平滑



def bayes(sentence:str, logger=True) -> int:
    '''
    利用贝叶斯分类器进行分类
    :rtype: 返回分类结果，-1为白话，0为无法区分，1为文言
    '''
    words = set(jieba.cut(sentence, cut_all=True))
    categories_res = []
    
    for category in categories_info:
        cnt = get_words_count(words, category["name"])
        res = mul(cnt)
        if logger: print(f"类别【{category['name_cn']}】公式计算值得 {res}")
        categories_res.append((res, category["name"], category["name_cn"]))

    # 由于已知只有两个类别
    # 可以直接比较两类别的计算值得出结论
    # 我们还可以方便的设置一个结果为“无法区分”的区间
    if logger: print("=========")

    if (1/res_retio) < (categories_res[1][0] / categories_res[0][0]) < res_retio:
        if logger: print("该句子无法分辨出文言或白话")
        return 0
    else:
        final_res = max(categories_res)
        if logger: print(f"该句子分类为【{final_res[2]}】")
        for category in categories_info:
            if category["name"] == final_res[1]:
                if category["rflag"]:
                    return category["rflag"]
                else:
                    raise Exception(f"类别 {category['name']} 的返回值不能设置为 0.")

    


if __name__ == '__main__':
    # sentence = " 晋太元中，武陵人捕鱼为业。缘溪行，忘路之远近。忽逢桃花林，夹岸数百步，中无杂树，芳草鲜美，落英缤纷。渔人甚异之，复前行，欲穷其林。 "
    # sentence = "适可而止矣。涓埃之事，亦央原神。夫原神者，其一未犯尔，其二固道，尔以何素愚辱之？米哈游者，欲彰华夏之文涵于天下，殚精竭虑。尔等竖子，仗键盘跋扈于网路，构陷良企于冤雪，不舍昼夜。华夏娱戏之前景，皆败于尔属！"
    # sentence = """时间永是流驶，街市依旧太平，有限的几个生命，在中国是不算什么的，至多，不过供无恶意的闲人以饭后的谈资，或者给有恶意的闲人作“流言”的种子。至于此外的深的意义，我总觉得很寥寥9，因为这实在不过是徒手的请愿。人类的血战前行的历史，正如煤的形成，当时用大量的木材，结果却只是一小块，但请愿是不在其中的，更何况是徒手。"""
    # sentence = """君所言甚是，然吾每日戏于原神可得原石百又五十，月进五千有余，得易五千美金于当世，计银三万两，吾虽年未志学，然赀巨程罗，富甲天下，傲睨之凭，皆原神所赐也。​"""
    # sentence = "魏武行役失汲道，三军皆渴，乃令曰：“前有大梅林，饶子，甘酸可以解渴。”士卒闻之，口皆出水，乘此得及前源。"
    sentence = "叨筊先与约，若通达无难，三笑俱阳、圣而无阴；"
    bayes(sentence)