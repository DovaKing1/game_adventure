import random


def make_character():
    """Creates a player character with name, race, class, and background."""
    name_first = input("Input your player's first name: ")
    name_last = input("Input your player's last name: ")

    # Race selection
    races = {
        "elf": "\nYou are from the forested lands of the south." \
                "\nYou are from a noble family, you got trained from a young age on how to travel though " \
                "forested places and how to shoot a bow.\nYou are on a adventure to prove to your self and to "\
                "others that you are worthy of the" + str(name_last) +  " name.\n",

        "dwarf": "You are from the towering mountains of the north, skilled in craftsmanship and battle.",
        "human": "You are from the rolling grasslands at the center of the continent, known for adaptability."
    }

    while True:
        race = input("\nAvailable races: Elf, Dwarf, Human\nEnter your race: ").strip().lower()
        if race in races:
            back_ground = races[race]
            break
        print("\nRace not recognized, please choose Elf, Dwarf, or Human.")

    # Class selection
    classes = {
        "warrior": "sword",
        "mage": "staff",
        "assassin": "dagger",
        "ranger": "bow",
        "archer": "bow",
        "necromancer": "staff"
    }

    while True:
        player_class = input("\nEnter your class (Type 'ls' to see options): ").strip().lower()
        if player_class in classes:
            weapon = classes[player_class]
            break
        elif player_class == "ls":
            print("\nClasses: Warrior, Mage, Assassin, Ranger, Necromancer\n")
        else:
            print("\nInvalid class. Please enter a valid class or type 'ls' for options.")

    print("\n===================")
    print(f"Your name is {name_first} {name_last}")
    print(f"You are a {race.capitalize()} adventurer.")
    print(f"Class: {player_class.capitalize()} | Weapon: {weapon}")
    print(f"Background: {back_ground}")
    print("===================")


def inv_rand():
    """Generates a random starting inventory of health potions and gold."""
    global health_potions, gold
    inventory_options = [(2, 30), (4, 20), (9, 0), (3, 50)]
    health_potions, gold = random.choice(inventory_options)


def higher_classes():
    """Displays the available higher-tier classes for each base class."""
    progression = {
        "warrior": ["paladin, "],
        "mage": ["necromancer"],
        "rogue": ["assassin"],
        "archer": [""],
    }

    print("\n=== Higher Tier Classes ===")
    for base_class, tiers in progression.items():
        print(f"\n{base_class.capitalize()}:")
        for tier in tiers:
            print(f"  - {tier}")


def beginning():
    """Displays the player's starting scenario."""
    print(f"\nYou have {health_potions} health potions and {gold} gold.")
    input("Press enter to begin your adventure!")
    print(f"\nYou arrive on a ship in the city of Evee.")


# Running the character creation process
if __name__ == "__main__":
    make_character()
    inv_rand()
    beginning()
