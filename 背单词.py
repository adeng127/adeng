
import random
contact={"China":"中国","Japan":"日本"}
def add():
    cj=input("添加？(Y/N):)")
    if cj=="y" or cj=="Y":
        h=str(input("请输入要添加的单词："))
        s=str(input("释义是："))
        contact[h]=s
    else:
        print("结束输入。")
    

def find():
    find=input("请输入要查询的单词或释义：")
    for i,j in contact.items():  # items()读取所有的键值，i 是键 ，j 是值
        if j == find:
            print(i)
        if i==find:
            print(j)
    

def text():
    print('随机5个单词的测试:')
    num=0
    i=0

    while i<5:
        a= random.sample(contact.keys(),1)
        b=a[0]
        print("单词为：",b)
        s=input("请输入释义:")
        if contact[b] == s:
            print("恭喜你，答对了")
            num+=1
        else:
            print("很遗憾，答错了")
               
        i+=1
        print(' ')
    s=num/5
    print('您的正确率为：',s)


p=''
while p !="0":
    p=input("""请输入要使用的功能
------1:添加单词
------2:查找单词的汉语或英语含义
------3:随机测试
------4.输入0结束使用""")
    if p=="1":
        add()
    if p=="2":
        find()

    if p=="3":
        text()
    if p=="0":
        print("感谢您的使用，下次再会~")
    