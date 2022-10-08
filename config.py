'''程序相关配置'''
from pathlib import Path


# 模型训练相关设置

model_path = Path("./model/")
'''模型保存目录'''

max_count = 100000
'''单个模型最多取样数'''

categories_info = [
    {
        "name_cn": "文言",
        "name": "wenyan",
        "rflag": 1, # 分类器返回值
        "path": Path("./train_data/wenyan")
    },
    {
        "name_cn": "白话",
        "name": "baihua",
        "rflag": -1,
        "path": Path("./train_data/baihua")
    }
]
'''各种类别信息'''

categories_name = [(category["name"], category["name_cn"]) for category in categories_info]
'''类别名称'''

# 分类器相关设置

punctuation = "，。、；‘【】、·~：\"”“{}（）,./;'[]\`!@#$%^&*()_+\\|123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM \n\r"
'''排除字符'''

res_retio = 10
'''能得出结果的最小计算值比例，过小则易误判，过大则更难取得结论'''

# 测试相关设置

test_path = Path("./test_data/")
'''测试集存放目录'''