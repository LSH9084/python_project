def fnprint(str):
    print(str)


def account(num1,num2):
    return num1+num2


def inputval():
    num1 = input('첫번째 숫자를 입력하세요.')
    num2 = input('두번째 숫자를 입력하세요.')
    return num1,num2

pnum1, pnum2 = inputval()
fnprint(account(pnum1,pnum2))
