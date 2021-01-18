import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# 不提倡这么用
# from math import sqrt
#
# print("Square root of 16 is", sqrt(16))

# 提倡这么用
import math

print("Square root of 16 is", math.sqrt(16))
