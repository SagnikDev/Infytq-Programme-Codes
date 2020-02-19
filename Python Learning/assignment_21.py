#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    next_day=day
    next_month=month
    next_year=year
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(month==2):
        if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
            months[1]=29
            print("Leap Year")

    if(day==31 and month==12):
        next_year=year+1
        next_month=1
        next_day=1
        print(next_day,"-",next_month,"-",next_year)
        return
    elif(day+1>months[month-1]):
        next_month=month+1
        next_day=1
    else:
        next_day+=1
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(31,8,2000)