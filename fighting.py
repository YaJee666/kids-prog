import random
import time
winTime = 0

for i in range(1, 4):
    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)
    print("——————现在是第{}局——————".format(i))
    while player_life > 0 and enemy_life > 0:
        print("【玩家】\n 血量：{} \n 攻击：{}".format(player_life, player_attack))
        print("-------------------------------------")
        print("【敌人】\n 血量：{} \n 攻击：{}".format(enemy_life, enemy_attack))
        print("-------------------------------------")
        enemy_life -= player_attack
        print("你发起了攻击，【敌人】剩余血量: {}".format(enemy_life))
        player_life -= enemy_attack
        print("敌人向你发起了攻击，【玩家】剩余血量: {}".format(enemy_life))
        if enemy_life < 0:
            print("这是第{}局，你赢了！".format(i))
            winTime += 1
        elif player_life < 0:
            print("第{}局，悲催，敌人把你干掉了！".format(i))
        time.sleep(1)
    print("=====================================")
if winTime >= 2:
    print("【最终结果：你赢了！】")
else:
    print("【最终结果：你输了！】")
    

    