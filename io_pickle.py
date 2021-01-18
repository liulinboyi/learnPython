import pickle

# 这里我们将存储对象的文件的名称
shoplistfile = 'shoplist.data'
# 要买的东西的清单
shoplist = ['apple', 'mango', 'carrot']

# 写入文件
f = open(shoplistfile, 'wb')
# 将对象存储到文件
pickle.dump(shoplist, f)
f.close()

# 销毁 shoplist 变量
del shoplist

# 从存储中读回
f = open(shoplistfile, 'rb')
# 从文件加载对象
storedlist = pickle.load(f)
print(storedlist)

# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)
