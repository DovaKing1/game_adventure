from leveling_system import level, strength, defense, health, amount, experience, experience_to_next_level


class QuestBoard:
    def __init__(self):
        self.quest_board = {}

    def add_quest(self, quest_name, quest_description, quest_reward):
        """Adds a quest to the quest board."""
        self.quest_board[quest_name] = {
            'description': quest_description,
            'reward': quest_reward,
            'status': 'Available'
        }

    def display_quests(self):
        """Displays all available quests."""
        print("\n--- Quest Board ---")
        for idx, (quest_name, quest_info) in enumerate(self.quest_board.items(), start=1):
            print(f"{idx}. Quest: {quest_name}")
            print(f"   Description: {quest_info['description']}")
            print(f"   Reward: {quest_info['reward']}")
            print(f"   Status: {quest_info['status']}")
            print("--------------------")

    def accept_quest(self, quest_name):
        """Marks a quest as 'In Progress' if available."""
        if quest_name in self.quest_board and self.quest_board[quest_name]['status'] == 'Available':
            self.quest_board[quest_name]['status'] = 'In Progress'
            return f"You have accepted the quest: {quest_name}"
        return "Quest not available or already in progress."

    def complete_quest(self, quest_name):
        """Marks a quest as 'Completed' if it was in progress."""
        if quest_name in self.quest_board and self.quest_board[quest_name]['status'] == 'In Progress':
            reward = self.quest_board[quest_name]['reward']
            self.quest_board[quest_name]['status'] = 'Completed'
            return f"Congratulations! You have completed the quest: {quest_name}. Reward: {reward}"
        return "Quest cannot be completed at this time."
    

def signed_up():
    print("Hello, I have noticed that you have not signed up to be an adventurer."
           " since you are new here, I have sign you up. Welcome to the advenures guild!!!")
    return True



def quest():
    is_signed_up = False
    rank = "F"
    quest_board = QuestBoard()


    if rank == "F":
        quest_board.add_quest("Explore the Forest", "Explore the mysterious forest.", "100 gold")
        quest_board.add_quest("Monster Hunt", "Hunt a goblin.", "5 gold")
        quest_board.add_quest("Wolf Hunt", "Hunt a pack of wolves.", "300 gold")

    if rank == "E":
        quest_board.add_quest

    if rank == "D":
        quest_board.add_quest

    if rank == "C":
        quest_board.add_quest

    if rank == "B":
        quest_board.add_quest

    if rank == "A":
        quest_board.add_quest

    if rank == "S":
        quest_board.add_quest

    if rank == "Mithril":
        quest_board.add_quest

    if rank == "Orichalcum": 
        quest_board.add_quest

    if rank == "Adamantite ":
        quest_board.add_quest


    print("\nWelcome to the Guild!")

    if is_signed_up != True:
        is_signed_up = signed_up()

    while True:
        user_input = input(
            "\nChoose an action:\n"
            "[Q] Get a quest\n"
            "[S] Display your stats\n"
            "[A] View active quests\n"
            "[L] Leave the guild\n"
            "Your choice: "
        ).strip().lower()

        if user_input == "s":
            print("\nPlayer Stats:")
            print(f"Level: {level}\nStrength: {strength}\nDefense: {defense}")
            print(f"Health: {health}\nAmount: {amount}")
            print(f"Experience: {experience}\nXP to next level: {experience_to_next_level}")

        elif user_input == "a":
            print("\nActive Quests:")
            for name, info in quest_board.quest_board.items():
                if info['status'] == 'In Progress':
                    print(f"- {name} (Status: {info['status']})")

        elif user_input == "q":
            quest_board.display_quests()
            try:
                user_choice = int(input("Enter the quest number to accept: ")) - 1
                quest_names = list(quest_board.quest_board.keys())

                if 0 <= user_choice < len(quest_names):
                    print(quest_board.accept_quest(quest_names[user_choice]))
                else:
                    print("Invalid quest number.")
            except ValueError:
                print("Please enter a valid number.")

        elif user_input == "l":
            print("You have left the guild.")
            break

        else:
            print("Invalid option. Please choose again.")



