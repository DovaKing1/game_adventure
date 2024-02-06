
from quest_system import quest 
from player_file import make_character, inv_rand, beginning
from economy import shop

weapon = ""
gold = 0
race = ""
name = ""
player_class = ""
health_potions = 0
back_ground = ""

def town_evee():
    print("Where would you like to go\n")
    u_i = input("Would you like to go to the guild[g], to the store[s]: ")

    if u_i == "g":
        quest()
    if u_i == "s":
        shop()


def main():
    make_character()
    inv_rand()
    beginning()
    town_evee()

if __name__ == "__main__":
    main()