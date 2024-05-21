# boolean = True

# while boolean :

#     list = []

#     count = int(input('몇개의 글자를 받을까요?'))
#     for num in range(count): 
#         input_val = input('글자를 입력하세요')
#         list.append(input_val)
        
#     for str in list:
#         print(str)
    
boolean = True

while boolean :

    dic = {}

    count = int(input('몇개의 글자를 받을까요?'))
    for num in range(count): 
        input_key = input('키를 입력하세요')
        input_val = input('값을 입력하세요')
        dic[input_key] = input_val
        
    for key,value in dic.items:
        print('key:', key ,'value:', value )

