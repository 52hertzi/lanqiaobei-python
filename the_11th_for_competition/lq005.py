print("****************凯撒密码******************")
try:
    content = str(input("请输入需要加密的内容:"))
    list(content)
    for i in content:
        str = ord(i) + 3        #转换为Ascii码
        if(str > ord('z')):
            str = str - ord('z') + ord('a') - 1
        print(chr(str),end='')
except Exception as e:
    print("输入有误")
