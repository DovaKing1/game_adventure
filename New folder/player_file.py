
import random


def make_character():
    global name
    global weapon
    global race
    global player_class
    global back_ground

    name_first = input("Input your players first name: ")
    name_last = input("\nInput your players last name: ")
    truefalse_race = True
    weapon = ""
    while truefalse_race != False:
        race = input("The advelable races in the world is: elf, dwarf, and human \n Enter your race: ")

        if race == "elf": 
            back_ground = "\nYou are from the forested lands of the south." \
                            "\nYou are from a noble family, you got trained from a young age on how to travel though " \
                           "forested places and how to shoot a bow.\nYou are on a adventure to prove to your self and to "\
                           "others that you are worthy of the" + str(name_last) +  " name.\n"
            truefalse_race = False
        elif race == "dwarf":
            back_ground = "You are from the towering moutains of the north"
            truefalse_race = False
        elif race == "human":
            back_ground = "You are from the rolling grass land of the center of the coutainent"
            truefalse_race = False
        else:
            print("race not included, choose another race in the world")

    truefalse_weapon = True
    weapon = ""
    while truefalse_weapon != False:
        player_class = input("Input your player class: ")

        if player_class == "warrior": 
            weapon = "sword"
            truefalse_weapon = False
        elif player_class == "mage":
            weapon = "staff"
            truefalse_weapon = False
        elif player_class == "assassin":
            weapon = "dager"
            truefalse_weapon = False
        elif player_class == "ranger" or player_class == "archer":
            weapon = "bow"
            truefalse_weapon = False
        elif player_class == "mage":
            weapon = "staff"
            truefalse_weapon = False
        elif player_class == "necromancer":
            weapon = "staff"
            truefalse_weapon = False
        else:
            print("Invalid or class not included, choose another class")

    print("\n===================\n" + "Your name is", name_first,name_last, "\nyou are a", race,
           "\nYour class is", player_class + "\nyour weapon is a",weapon)

def inv_rand():
    global health_potions
    global gold

    rand_num = random.randrange(0, 5)
    if rand_num == 1:
        health_potions = 2
        gold = 30
    elif rand_num == 2:
        health_potions = 4
        gold = 20
    elif rand_num == 3:
        health_potions = 9
        gold = 0
    else:
        health_potions = 3
        gold = 50

def higher_classes():
    
    """
    Warrior: Valor Champion
    Mage: Arcane Sorcerer
    Assassin: Shadowblade Master
    Archer: Precision Marksman
    Necromancer: Deathweaver

    Warrior: Paragon Vanguard
    Mage: Archmagus
    Assassin: Phantom Executioner
    Archer: Seraphic Sharpshooter
    Necromancer: Dreadlord Conduit

    Warrior: Apex Warlord
    Mage: Celestial Archon
    Assassin: Nightshade Mastermind
    Archer: Ethereal Ranger
    Necromancer: Lich Sovereign

    Warrior: Supreme Battlemaster
    Mage: Astral Magus
    Assassin: Ebon Shadowblade
    Archer: Stellar Marksman
    Necromancer: Abyssal Revenant

    Warrior: Arcane warrior
    Mage: Chronomantic Archon
    Assassin: Eclipse Phantom
    Archer: Astral Sagittarius
    Necromancer: Dread Sovereign

    Warrior: Eternal Vanguard
    Mage: Archmage of the Cosmic Arcanum
    Assassin: Abyssal Shadow Seraph
    Archer: Stellar Seraphic Sentinel
    Necromancer: Netherlord

    """


        

def beginning():
    global health_potions
    global gold

    print("You have " + str(health_potions) + " health potions with " + str(gold) + " gold")
    input("Press enter to begin your adventure!!!")
    print("You arrive on a ship in the city of Evee. From the " + str(back_ground))

