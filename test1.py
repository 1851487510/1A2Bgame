#1A2B猜数字小游戏

import random
def play_1A2B():
    print('游戏开始时，玩家先选择难度（2-9）级（数字跟难度有关，4级难度生成4位数，5级难道生成5位数...），然后电脑随机生成了一个不重复的数字，玩家需根据电脑的反馈猜出这位数字，其中A代表玩家输入的与电脑生成的数字相同且位置相同的个数，B代表玩家输入的与电脑生成的数字相同，但位置不同的个数(输1回退上一级)')
    while True:
        k = input('请输入你想玩的难度（2-9）:')
        k = int(k)
        if 2<=k<=9:
            def play(number):
                def cp_number():
                    a = set()
                    while len(a)!=number:
                        a.clear()
                        b =str(random.randint(10**(number-1),10**number-1))
                        for i in b:
                            a.add(i)
                    return ''.join([str(i) for i in b])
                computer = cp_number()
                #print(computer)

                guess_number = 0
                while True:
                    guess_number +=1
                    player = input('第%d次猜测的数字：'%guess_number)
                    if player=='1':
                        break
                    if (not player.isdigit()) or len(set(player))!=number or len(player)!=number:
                        print('请注意格式')
                    elif player==computer:
                        print('猜对啦')
                        break

                    else:
                        x=y=0
                        for j in range(number):
                            if player[j]==computer[j]:
                                x +=1
                            elif player[j] in computer:
                                y +=1
                        print('%dA%dB'%(x,y))
            play(k)
        if k==1:
            break
        else:
            print('请输入2-9之间的数字')
play_1A2B()