import random

num = random.randint(1, 100)

while True:
    guess = int(input('输入一个数字：'))
    if guess > num:
        print('大了！再猜~')
        continue
    if guess < num:
        print('小了！再猜~')
        continue
    print('恭喜你，猜对了！')
    break
