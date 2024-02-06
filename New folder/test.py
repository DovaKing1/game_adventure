
from leveling_system import level
from leveling_system import strength
from leveling_system import defense
from leveling_system import health
from leveling_system import amount
from leveling_system import experience
from leveling_system import experience_to_next_level




class QuestBoard:
    def __init__(self):
        self.quest_board = {}

    def add_quest(self, quest_name, quest_description, quest_reward):
        self.quest_board[quest_name] = {
            'description': quest_description,
            'reward': quest_reward,
            'status': 'Available'
        }

    def display_quests(self):
        print("Quest Board:")
        for quest_name, quest_info in self.quest_board.items():
            print(f"Quest: {quest_name}")
            print(f"Description: {quest_info['description']}")
            print(f"Reward: {quest_info['reward']}")
            print(f"Status: {quest_info['status']}")
            print("--------------")

    def accept_quest(self, quest_name):
        if quest_name in self.quest_board and self.quest_board[quest_name]['status'] == 'Available':
            self.quest_board[quest_name]['status'] = 'In Progress'
            print(f"You have accepted the quest: {quest_name}")
        else:
            print("Quest not available or already in progress.")

    def complete_quest(self, quest_name):
        if quest_name in self.quest_board and self.quest_board[quest_name]['status'] == 'In Progress':
            print(f"Congratulations! You have completed the quest: {quest_name}")
            print(f"Reward: {self.quest_board[quest_name]['reward']}")
            self.quest_board[quest_name]['status'] = 'Completed'
        else:
            print("Quest cannot be completed at this time.")



def quest():
    rank = "F"
    true_false = False

    print("Welcome to the guild")
    while true_false == False:
        input_user = input("What would like to do, get a quest[q], display your states[s], view active quests[a], or leave the guild[l]: ")
        if input_user == "s":
            print("Player states:\nlevel = " + str(level) + "\nstrength = " + str(strength) + 
                    "\ndefense = " + str(defense) + "\nhealth = " + str(health) +"\namount = " + str(amount) +
                    "\nexperience = " + str(experience) + "\nexperience_to_next_level = " + str(experience_to_next_level))
            
        elif input_user == "a":
            print()

        elif input_user == "q": 
            quest_board = QuestBoard()

            print("The following is the quests open for your rank: \n")
            if rank == "F":
                num1 = quest_board.add_quest("Explore the Forest", "Explore the mysterious forest.", "100 gold")
                num2 = quest_board.add_quest('Monster hunt', 'Hunt a goblin.', '5 gold')
                num3 = quest_board.add_quest("Explore the Forest", "Explore the mysterious forest.", "100 gold")
                num4 = quest_board.add_quest('Monster hunt', 'Hunt pack of wolfs.', '300 gold')

                quest_board.display_quests()
            
            user_input = int(input("which quest would you like to accept: "))
            if user_input == 1:
                quest_board.accept_quest(num1)
                true_false = True
            elif user_input == 2:
                quest_board.accept_quest(num2)
                true_false = True
            elif user_input == 3:
                quest_board.accept_quest(num3)
                true_false = True
            elif user_input == 4:
                quest_board.accept_quest(num4)
                true_false = True
            
