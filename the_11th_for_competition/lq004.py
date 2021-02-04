print("**************反倍数**************")
try:
    num = int(input("请输入一个数值:"))

    a,b,c = (int(x) for x in input("请输入3个数值:").split(' '))
    sum = 0
    list = []

    for i in range(1,num + 1):
        if(i % a != 0 and i % b != 0 and i % c != 0):
            sum += 1
            list.append(i)

    print(num,'的反倍数有:',sum,'个')
    print('分别是:',list)
except Exception as e:
    print("输入有误")
