try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))

# 按下 ctrl + d
# $ python exceptions_handle.py
# Enter something --> Why did you do an EOF on me?

# 按下 ctrl + c
# $ python exceptions_handle.py
# Enter something --> ^CYou cancelled the operation.

# $ python exceptions_handle.py
# Enter something --> No exceptions
# You entered No exceptions
