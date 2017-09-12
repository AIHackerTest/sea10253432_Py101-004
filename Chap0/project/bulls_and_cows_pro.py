import random

def invalidinput(guessnum):
    if guessnum[0] == 0 or len(guessnum) != 4:
        return False
    guessset = set(guessnum)
    if len(guessnum) == len(guessset):
        return True
    else:
        return False

listNum = random.sample(range(0,9),4)

while listNum[0] == 0:
    listNum = random.sample(range(0,9),4)

#print("%r" %listNum)

print("""欢迎参与猜数字小游戏！您有10次机会猜一个四位数，
这个数大于1000且每一位上的数字不同，开始吧！""")

for i in range (0,10):
    prompt = "第 %d 次：" % (i + 1)
    guessnum = list(input(prompt))
#    print("%r" % guessnum)


    if not invalidinput(guessnum):
        print("请输入一个大于1000的四位数数字，并且每一位数字不同!")
        continue

    for j in range(0, 4):
        guessnum[j] = int(guessnum[j])
#    print("%r" % guessnum)

    if guessnum == listNum:
        print("您猜中了！祝贺您！")
        exit(0)

    anums = 0
    bnums = 0
    for j in range(0, 4):
        if(guessnum[j] == listNum[j]):
            anums += 1
        elif guessnum[j] in listNum:
            bnums += 1

    print("A%dB%d" %(anums, bnums))

print("您已经用完了10次机会，游戏结束！")
