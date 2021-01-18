number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # 这会导致 while 循环停止
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
# 在 while 循环中可以有一个 else 从句
else:
    print('The while loop is over.')
    # 你可以在此处继续进行其它你想做的操作

print('Done')
