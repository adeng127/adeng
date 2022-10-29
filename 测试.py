import random

listb = {"1": '张三', 2: '李四', 3: '王五', 4: '赵六', 5: '王麻子', 6: '包子', 7: '豆浆'}

lista = {'1': '张三', '2': '李四', '3': '王五', '4': '赵六', '5': '王麻子', '6': '包子', "7": '豆浆'}

for c in listb.keys():
    a =random.sample(lista.keys(), 1) # 随机一个字典中的key，第二个参数为限制个数
    print(a)
    b = a[0]
    print(b)
    print(lista[b]) # 打印随机抽取的值
    print(c)
