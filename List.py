import random 

number_random=0

number = []
Number_to_the_power_of2=[]
while True:
    number_random = random.randint(1 , 100)
    number.append(number_random)

    if len(number) == 20:
        break

print("Default number: " , number)

for i in number:
    Number_to_the_power_of2.append(i**2)
print("Number_to_the_power_of2 : ", Number_to_the_power_of2)
