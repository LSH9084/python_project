# ipC = input('몇개의 숫자를 입력하시겠습니까?')

# for i in range(int(ipC)):
#     input_key = i
#     input_value = int(input('숫자를 입력 하세요.'))
#     ikk = {}
#     ikk[input_key] = input_value



# print(ikk.items)
# sum = 0
# for k in ikk :
#     sum += k

# print(sum)

def oprder():
    count = (int(input('몇개의 숫자를 입력하시겠습니까?')))
    return count

def input_val(count):
    array_val = []
    for i in range(count):
        num = int(input('숫자를 입력해주세요'))
        array_val.append(num)
    return array_val

def account (array_val):
    result = 0
    kk = input('+or-')
    if kk == '+':
        for num in array_val:
            result += num
        return result
    else :
        cnt=0
        if cnt == 0 :
            for num in array_val:
                result -= num
                cnt+= 1
            return result
        
        

count = oprder()
array_val = input_val(count)
print(account(array_val))
