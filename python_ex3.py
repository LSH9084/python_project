i = 10
j = 20
if i+j==30:
    print('안녕하세요')
else:
    print('잘가')

run = True

if run:
    print('안녕')
else:
    print('잘가')

# str = input("글자를 입력하세요.")

if str == '가':
    print('나다라마')
elif str == '나':
    print('다라마')
else:
    print('없다')
count = 0
while count <5:
    print(count+1,'번째 연산입니다.')
    num1 = int(input("첫번째 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    op = input("어떤 연산을 하시겠습니까? + - * /")
    result = 0
    if op == '+':
        result = num1+num2
    elif op == '-':
        result = num1-num2
    elif op == '*':
        result = num1*num2
    elif op == '/':
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            result = num1/num2
    else:
        print("다시입력바람")
    print(result)
    count+=1



