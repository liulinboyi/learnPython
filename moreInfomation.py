# 传递元组
def get_error_details():
    return (2, 'details')


errnum, errstr = get_error_details()
print(errnum)
# 2
print(errstr)
# 'details'

# 交换两个变量的最快方法
a = 5
b = 8
print(a, b)
# (5, 8)
a, b = b, a
print(a, b)


# (8, 5)


# 魔术方法

# __init__(self, ...)
# - 在返回新创建可以使用的对象之前调用此方法。

# __del__(self)
# -在对象被销毁之前调用（具有不可预测时机，所以避免使用它）

# __str__(self)
# -当我们使用 print 函数或使用 str() 时调用。

# __lt__(self, other)
# -使用小于（ less than ）运算符（<）时调用。 同样，所有运算符都有特殊的方法（+，> 等）

# __getitem__(self, key)
# -使用 x[key] 索引操作时调用。

# __len__(self)
# -当内置的 len() 函数用于序列对象时调用。


# Lambda 格式


# 在函数中接收元组和字典

def powersum(power, *args):
    """返回每个参数指定幂次的总和。"""
    total = 0
    for i in args:
        total += pow(i, power)
    return total
    # 因为我们在`args`变量上有一个`*`前缀，所有传递给函数的额外参数都作为元组存储在`args`中。 如果使用了`**`前缀，那么额外的参数将被认为是字典的键/值对。


print(powersum(2, 3, 4))
# 25
print(powersum(2, 10))
# 100


# assert 语句
# assert语句应该是明智地使用。 大多数情况下，最好能捕获异常、处理问题或向用户显示错误消息然后退出。
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
# 'item'
assert len(mylist) >= 1
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AssertionError


