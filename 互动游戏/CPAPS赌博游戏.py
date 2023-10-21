from random import randint  # 导入 randint 函数，用于生成随机数

money = int(input('请输入初始资产：'))# 设置玩家的总资产

while money > 0:  # 当玩家的总资产大于 0 时，开始循环
    print('你的总资产为:', money)  # 输出当前玩家的总资产
    needs_go_on = False  # 设置一个变量表示是否需要继续游戏
    while True:  # 用于获取玩家下注金额，如果输入有误就一直循环
        debt = int(input('请下注: '))  # 获取玩家输入的下注金额
        if 0 < debt <= money:  # 如果下注金额符合要求（大于 0 小于等于总资产）
            break  # 退出循环
    first = randint(1, 6) + randint(1, 6)  # 随机生成两个骰子点数，计算总点数
    print('玩家摇出了%d点' % first)  # 输出玩家的点数
    if first == 7 or first == 11:  # 如果总点数为 7 或 11，玩家胜利
        print('玩家胜!')
        money += debt  # 玩家赢得下注金额，总资产增加
    elif first == 2 or first == 3 or first == 12:  # 如果总点数为 2、3 或 12，庄家胜利
        print('庄家胜!')
        money -= debt  # 玩家输掉下注金额，总资产减少
    else:  # 否则，进入下一轮循环
        needs_go_on = True  # 标记需要继续游戏
    while needs_go_on:  # 如果需要继续游戏
        needs_go_on = False  # 先将标记重置为 False
        current = randint(1, 6) + randint(1, 6)  # 随机生成两个骰子点数，计算总点数
        print('玩家摇出了%d点' % current)  # 输出玩家的点数
        if current == 7:  # 如果总点数为 7，庄家胜利
            print('庄家胜')
            money -= debt  # 玩家输掉下注金额，总资产减少
        elif current == first:  # 如果总点数与第一次投掷时的点数相同，玩家胜利
            print('玩家胜')
            money += debt  # 玩家赢得下注金额，总资产增加
        else:  # 否则，继续下一轮循环
            needs_go_on = True
print('你破产了, 游戏结束!')  # 如果玩家的总资产小于等于 0，游戏结束，输出信息
input()
