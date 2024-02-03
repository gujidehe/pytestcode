import pytest
# 单参数多循环
# @pytest.mark.parametrize("name",["谁谁谁"])
# def test_parmametrize(name):
#     print("我是"+name)

@pytest.mark.parametrize("name",["安琪拉","刘禅","呜呜呜"])
def test_parmametrize(name):
    assert name == "安琪拉"