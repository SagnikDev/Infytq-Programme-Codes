#DSA-Tryout
import random
def generate_cards_per_type(card_type):
    list_of_cards=[card_type+str(i) for i in range(2,11)]
    others=["J","Q","K","A"]
    other_cards=[card_type+i for i in others]
    list_of_cards.extend(other_cards)
    return list_of_cards
    

def generate_card_deck():
    types=['C','D','H','S']
    cards=[]
    for i in types:
        cards.extend(generate_cards_per_type(i))
    return cards

def shuffle_card_deck(card_list):
    length=len(card_list)
    mid=len(card_list)//2
    f_index=random.randint(0,mid-1)
    n_index=random.randint(mid,length-1)
    temp=card_list[f_index]
    card_list[f_index]=card_list[n_index]
    card_list[n_index]=temp

def sort_cards_of_each_player(card_list):
    sorted_cards=[]
    cards=generate_card_deck()
    for i in cards:
        if(i in card_list):
            sorted_cards.append(i)
    return sorted_cards

def allocate_cards_to_players(cards_list):
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    index=0
    while(index<len(cards_list)):
        p1.append(cards_list[index])
        index+=1
        p2.append(cards_list[index])
        index+=1
        p3.append(cards_list[index])
        index+=1
        p4.append(cards_list[index])
        index+=1
    return {"Player1":p1,"Player2":p2,"Player3":p3,"Player4":p4}
def prepare_cards():
    first=None
    cards=generate_card_deck()
    for i in range(0,20):
        shuffle_card_deck(cards)
    player_cards=allocate_cards_to_players(cards)
    for i,j in player_cards.items():
        sorted_cards=sort_cards_of_each_player(j)
        if('CA' in sorted_cards):
            first=i
        player_cards[i]=sorted_cards
    return first


first_player=prepare_cards()
print("The first player is:",first_player)
