import os

import pytest
import yaml
from read_data import get_data
import allure


# 多参数多循环
# @pytest.mark.parametrize("name",["谁谁谁"])
# def test_parmametrize(name):
#     print("我是"+name)
# f = open("config/data.yml", 'r', encoding='utf-8')
# data = yaml.safe_load(f)


@pytest.mark.parametrize("name,word", get_data())
def test_parmametrize(name, word):
    print(f'{name}说{word}')

if __name__=="__main__":
    pytest.main()
    os.system("allure generate ./report -o ./report --clean")