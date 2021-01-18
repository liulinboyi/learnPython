# 列表元组和字符串都是序列的一种
# 三种序列：列表、元组和字符串。它们还有另一种特殊的操作 —— 切片 ，切片操作让我们可以得到序列的一部分。

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# 字符串索引 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# 列表切片 #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 字符串切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

print(shoplist[::1])

print(shoplist[::2])

