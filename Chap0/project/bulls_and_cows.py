# _*_ coding:utf-8 _*_
"""猜数字小游戏"""

import random
from sys import exit

random_num = random.randint(1, 19)

print("""这是一个小游戏，请猜一个 20 以内的数字，
你有 10 次机会哦，开始吧！""")

for i in range(0,10):
    prompt = "第 %d 次：" % (i + 1)
    input_num = int(input(prompt))
    if input_num == random_num:
        print("正确！恭喜你猜中了！！！游戏结束！")
        exit(0)
    elif input_num > random_num:
        print("大了，再来一次！")
    else:
        print("小了，再来一次！")

print("你已经用完了所有的机会，游戏结束！")
