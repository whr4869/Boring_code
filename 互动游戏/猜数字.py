from 猜数字的引用 import a
temp = input("不妨猜一下数字")
guess = int(temp)

if guess == a:
     print("对了")
else:
     print("错了")

print("游戏结束")

input()

