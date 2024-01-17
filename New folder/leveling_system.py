
import player_file

level = 0
strength = 5
defense = 5
health = 100
amount = 100
experience = 0
experience_to_next_level = 100

def gain_experience(amount):
        global experience

        experience += amount
        print(f"{player_file.name} gained {amount} experience!")
        check_level_up()

def check_level_up():
    global experience
    global experience_to_next_level
    global level

    while experience >= experience_to_next_level:
        level += 1
        experience -= experience_to_next_level
        experience_to_next_level = int(experience_to_next_level * 1.5)
        print(f"{player_file.name} leveled up to level {level}!")
        print(f"{player_file.name} needs {experience_to_next_level} experience for the next level.")


