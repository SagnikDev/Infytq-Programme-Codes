#DSA-Assgn-4

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
    def __init__(self,player_list):
        self.__players_list=player_list
    def sort_players_based_on_experience(self):
        list_of_players={}
        list_of_sorted_player=[]
        for player in self.__players_list:
            list_of_players[player.get_experience()]=player
        list_of_players_sorted=sorted(list_of_players.items(),reverse=True)
        for player in list_of_players_sorted:
            list_of_sorted_player.append(player[1])
        self.__players_list=list_of_sorted_player
    def display_player_details(self):
        for player in self.__players_list:
            print(player)
    def shift_player_to_new_position (self,old_index_position, new_index_position):
        captain=self.__players_list.pop(old_index_position)
        self.__players_list.insert(new_index_position,captain)

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
#Create object of Game class, invoke the methods and test your program
game1=Game(players_list)
game1.sort_players_based_on_experience()
game1.display_player_details()
print("-------------------------------")
game1.shift_player_to_new_position(0,3)
game1.display_player_details()