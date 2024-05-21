
num1 = input('첫번쨰 숫자를 입력하세요.')
str1 = input('+or-')
num2 = input('첫번쨰 숫자를 입력하세요.')
str2 = input('+or-')
num3 = input('첫번쨰 숫자를 입력하세요.')
def plusFun():
    print(int(num1)+int(num2)+int(num3))

def minusFun():
    print(int(num1)-int(num2)-int(num3))

def plmiFun():
    print(int(num1)+int(num2)-int(num3))

def miplFun():
    print(int(num1)-int(num2)+int(num3))
if str1 == str2 :
    if str1 == '+':
        plusFun()
    else: 
        minusFun()
    
if str1 != str2 :
    if str1 == '+':
        plmiFun()
    else :
        miplFun()








