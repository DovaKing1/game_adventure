

class QuestBoard:
    def __init__(self, quest_name, quest_description, quest_reward):
        self.quest_name =  quest_name 
        self.quest_description = quest_description
        self.quest_reward = quest_reward

    def display_quests(self):
        print("Quest Board:")
        print(f"Quest: {self.quest_name}")
        print(f"Description: {self.quest_description }")
        print(f"Reward: {self.quest_reward}")
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



if __name__ == "__main__":
    quest_board = QuestBoard()

    # # Adding quests to the quest board
    quest_board.append('Monster hunt', 'Hunt a goblin.', '5 gold')

    # # Displaying available quests (if needed)
    quest_board.display_quests()

    # # Accepting and completing quests (example usage)
    quest_board.accept_quest('Rescue the Princess')
    quest_board.complete_quest('Rescue the Princess')

    # # Displaying updated quest board (if needed)
    quest_board.display_quests()
