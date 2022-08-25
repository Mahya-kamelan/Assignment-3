sh=0
m=0
h=0

while True:
    x=input("Enter the desired scale( h ya s) ")
    if x=="s":
        t=int(input("Enter the time in seconds "))
        s=t%60
        h=t//3600
        m=t//60-h*60
        print("time: ",h,"hour",m,"minutes",s,"second ")
        continue
    elif x=="h":
        h=int(input("Enter the hour "))
        m=int(input("Enter the minute "))
        s=int(input("Enter seconds "))
        time=(h*60*60)+(m*60)+(s)
        print("Time in seconds :",time)
        continue
