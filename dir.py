import sys

# 获取 sys 模块内所有属性的标识符
dir(sys)
# ['__displayhook__', '__doc__',
#  'argv', 'builtin_module_names',
#  'version', 'version_info']
# 这里只列出了部分输出

# 获取当前模块内属性的标识符
# 以列表的形式返回某个对象定义的一系列标识符。如果这个对象是个模块，返回的列表中会包含模块内部所有的函数、类和变量
# 这个函数接收一个可选的参数。当参数是模块名时，函数会返回对应模块的标识符列表。没有参数时则会返回当前模块的标识符列表
dir()
# ['__builtins__', '__doc__',
#  '__name__', '__package__', 'sys']

# 创建一个新的变量 'a'
a = 5

dir()
# ['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# 删除变量 'a'
del a

dir()
# ['__builtins__', '__doc__', '__name__', '__package__', 'sys']

# dir函数对 任何 对象都有效。
# vars函数，它有时能给你对象的属性和它们的值，但这个函数并不总是有效。

