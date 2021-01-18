
# 三引号
text = '''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

print(text)


print("---------------------------------------------------------------------")


age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

print("---------------------------------------------------------------------")


age = 20
name = 'Swaroop'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

print("---------------------------------------------------------------------")


# 取十进制小数点后的精度为 3 ，得到的浮点数为 '0.333'
print('{0:.3f}'.format(1.0/3))
# 填充下划线 (_) ，文本居中
# 将 '___hello___' 的宽度扩充为 11
print('{0:_^11}'.format('hello'))
# 用基于关键字的方法打印显示 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print("---------------------------------------------------------------------")
print('a', end='')
print('b', end='')



