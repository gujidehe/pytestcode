import pytest
def test_a():
    print('test_a')
    return 1*0

def test_b():
    print('test_b')
    return 1/0

# if __name__== '__main__':
#     pytest.main(["-s"])