#摄氏度（'C）转换成华氏度（'F）程序
#让使用者入股摄氏度然后打印出华氏度的程序
#公式F=C*9/5+32

c = (input('请输入摄氏度:'))
c = float(c)
print (c)
f = c * 9 / 5 + 32
print ('您输入的摄氏度转换成华氏度应为:', f)