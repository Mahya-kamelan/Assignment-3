from itertools import count
import random
c=0
x=100
a=0
x

print("select a number between 0 to 99")

while True:
     
    number=random.randint(a,x)
    print("is",number,"The numbers you want?")
    y=int(input("1: number is bigger \n"
    " 2 adad dorost ast \n"
    " 3 number is lower \n"))
    c+=1
    if y==1:
        a= number
        continue
    elif y==2:
        break
    elif y==3:
        x=number
        continue
    else:
        print("Choose the correct numbers from the menu")
        a=0
        x=100
        continue
print("hooora The numbers you want :", number ,"with",c ,"Guess done")
