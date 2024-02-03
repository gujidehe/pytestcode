import pytest


def setup_module():
    print("准备测试数据")


def teardown_module():
    print("清理测试数据")


@pytest.fixture()
def before():
    print('before')


@pytest.fixture()
def login():
    print('login')
    return "user"


@pytest.mark.usefixtures('before')
def test_1():
    print('test_1()')


def test_2(login):
    print('test_2()', login)


if __name__ == '__main__':
    pytest.main(["-s", "test_py4.py"])
