b=['가','나','다']
c='디언'
e='라'
f='람쥐'
r = [c,e,f]

for i in b :
    if(i=='가'):{
        print(i+c)
    }
    if(i=='나'):{
        print(i+e)
    }
    if(i=='다'):{
        print(i+f)
    }
        
for i in b:
    for j in r:
        if(i+j == '가디언''나라''다람쥐'):{
            print(i+j)
        }
b = ['나','마','다']
b.append('라')
b.remove('마')
b.sort()
b.insert(0,'가')

for i in b : 
    print(i)


