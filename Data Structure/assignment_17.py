#DSA-Assgn-17

def find_matches(country_name):
    match_list_1=[]
    for i in match_list:
        if(country_name in i):
            match_list_1.append(i)
    return match_list_1
def max_wins():
    win_dict={}
    match_list_1=[]
    for i in match_list:
        match_list_1.append(i.split(":"))
    matches=[]
    for i in match_list_1:
        if(i[1] not in matches):
            matches.append(i[1])
    for i in matches:
        team=[]
        win=-1
        for j in match_list_1:
            if(j[1]==i and int(j[3])>int(win)):
                win=j[3]
        for k in match_list_1:
            if(k[1]==i and k[3]==win):
                team.append(k[0])
        win_dict[i]=team
    return win_dict

def find_winner(country1,country2):
    match_list_1=[]
    country1_score=0
    country2_score=0
    for i in match_list:
        match_list_1.append(i.split(":"))
    for i in match_list_1:
        if(i[0]==country1):
            country1_score+=int(i[3])
        if(i[0]==country2):
            country2_score+=int(i[3])
    if(country1_score>country2_score):
        return country1
    elif(country2_score>country1_score):
        return country2
    else:
        return "Tie"
    

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print(find_matches("AUS"))
print(max_wins())
print(find_winner("AUS","IND"))