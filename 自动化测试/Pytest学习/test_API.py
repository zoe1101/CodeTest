import pytest
from pytest import approx  ##断言两个数字(或两组数字)在某个容差范围内彼此相等。
import numpy as np

print((0.1 + 0.2,0.2 + 0.4) == approx((0.3,0.6)))
print({'a': 0.1 + 0.2,'b': 0.2 + 0.4} == approx({'a': 0.3,'b': 0.6}))
print(np.array([0.1,0.2]) + np.array([0.2,0.4]) == approx(np.array([0.3,0.6])))
print(np.array([0.1,0.2]) + np.array([0.2,0.1]) == approx(0.3))  #numpy标量的数组
print(1.0001 == approx(1,rel=1e-3))  #更改相对容差
print(1.0001 == approx(1,abs=1e-3))  #绝对容差

#如果您指定abs但不指定rel,则比较将不会考虑相对容差。换句话说,1e-6如果超过指定的绝对容差,则默认相对容差范围内的两个数字仍将被视为不相等。如果同时指定两个abs和rel,如果满足任一公差,则数字将被视为相等：
print(1 + 1e-8 == approx(1,rel=1e-6,abs=1e-12))
# if __name__ == '__main__':
#        pytest.main(["-s","test_API.py"]) # 调用pytest的main函数执行测试