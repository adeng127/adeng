
import random    #------------random，随机选择模块

def guess():   #-------------定义猜单词函数，便于执行
    words=("python","juice","easy","difficult","answer","continue","phone","hello","pose","game")     #------录入单词
    newword=""           #-----空字符

    word=random.choice(words)   #---------随机挑一个单词
    recordword=word  #—--------保存单词，猜的时候对比
    while word:
        s=random.randrange(len(word))         #-----根据word长度，产生word随机位置
        newword+=word[s]                      #-----s位置的字母组合到乱序后的单词
        word=word[:s]+word[(s+1):]            #-----原位置字母用切片删除。
    print("乱序后的单词：",newword)

    x=str(input("让你猜："))
    if x==recordword:
        print("真棒，你猜对了")
    else:
        print("可惜，猜错了")

guess()   #--------首次执行

while True:     #--------------进入循环
    y=input("是否继续？(T/N):")
    if y=="T" or y=="y":
        guess()
    else:
        print("下次再见~")
        break

    

