from ast import If, While


PASSWOED=7512
TEMP=0
i=0
res=0
n=0
while i<3:
   
    temp=x=int(input('enter the pass:  '))
    if 1000<=x<=9999:
        if x==PASSWOED:
            print("you are verified ")
            break
        
        else:
            print('you are wrong')
            i+=1
    else:
        continue
if i>2:
    print("acsess denied!!")
