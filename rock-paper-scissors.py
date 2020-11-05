import random

# def userChoice():
#   print("请输入你的选择：r代表石头， s代表剪刀， p代表布")
#   while(True):
#     userChoice = input()
#     if (userChoice == 'r' or userChoice == 'p' or userChoice == 's'):
#       return userChoice
#     else:
#       print("输入错误，请重新如输入")

def converToWord(letter):
  if letter == 'r':
    return "石头"
  elif letter == 'p':
    return "布"
  else:
    return "剪刀"

def getComputerChoice():
    choices = ['r', 'p', 's']
    letter = random.choice(choices)
    return letter

def winOrLoseOrDraw(userChoice):
  compChoice = getComputerChoice()
  compShow = converToWord(compChoice)
  userShow = converToWord(userChoice)
  print("[ 计算机输入：{} ] VS [ 用户输入：{} ]".format(compShow, userShow))
  result = userChoice + compChoice
  if result == "rs" or result == "sp" or result == "pr":
    print("你赢了！")
    return 1
  elif result == "sr" or result == "ps" or result == "rp":
    print("你输了！")
  elif result == "rr" or result == "pp" or result == "ss":
    print("平局！")
  else :
    print("非法输入!!")
  return 0


wins, times = 0, 0
flag = True

print("================游戏开始，请按'q'键退出==================\n")
print("====请输入你的选择：r代表石头， s代表剪刀， p代表布======\n")
while(flag):
    times += 1
    userChoice = input()
    if userChoice == 'q':
        flag = False
        break
    wins += winOrLoseOrDraw(userChoice)
    print(">>>>>>>>>>>>这是第{}局游戏，获胜次数为{}<<<<<<<<<<<<<<<<\n".format(times, wins))
