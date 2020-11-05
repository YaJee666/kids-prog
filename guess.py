import random
answer = random.randint(0, 12)
times = 3
letter = 0
while True:
    if times == 0:
        print("猜谜失败")
        break
    try:
        letter = int(input("请输入在0到12之间的一个数字，你有三次机会\n"))
    except ValueError:
        print("非法输入")
        times -= 1
        continue
    times -= 1
    if letter == answer:
        print("猜谜成功")
        break
    elif letter < answer:
        print("猜小了，再试一次")
    else:
        print("猜大了，再试一次")