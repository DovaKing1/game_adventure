
from quest_system import quest 
from player_file import make_character, inv_rand, beginning
from economy import shop
from out_side import outside

weapon = ""
gold = 0
race = ""
name = ""
player_class = ""
health_potions = 0
back_ground = ""

def town_evee():
    true_false = True
    while true_false:
        print("Where would you like to go")
        u_i = input("Would you like to go to the guild[g], to the store[s], to leave the town[l]: ").lower()
        u_i.lower()

        if u_i == "g":
            true_false = False
            quest()
        elif u_i == "s":
            true_false = False
            shop()
        elif u_i == "l":
            true_false = False
            outside()
        else:
            print("\nIncorrect input, please enter [g] or [s]\n")
        


def main():
    make_character()
    inv_rand()
    beginning()
    town_evee()

if __name__ == "__main__":
    main()