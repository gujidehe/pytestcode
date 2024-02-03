import pytest


def test_1():
    print('test_1============')
    return 1 * 0


def test_2():
    print('test_2============')
    return 1 / 0


def demo_1():
    print('demo_1+++++')
    return 1 * 0


def demo_2():
    print('demo_2+++++')
    return 1 / 0


if __name__ == '__main__':
    pytest.main(["-s", "test_py3.py"])
