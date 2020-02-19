#PF-Tryout

#debug the below code
counter1=0
counter2=5
temp=counter2
while(counter1 < 5):
    star=""
    while(counter2>0):
        star=star+ "*"
        counter2-=1
    print(star)
    counter1+=1
    temp-=1
    counter2=temp