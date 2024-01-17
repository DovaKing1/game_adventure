import random

class Player:
    def __init__(self, name, health=100, attack=10, defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self):
        return random.randint(1, self.attack)

    def defend(self):
        return random.randint(1, self.defense)

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_player(self):
        return random.randint(1, self.attack)
    
    def defend(self):
        return random.randint(1, self.defense)

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"


def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print("What will you do?")
        print("1. Attack")
        print("2. Defend")
        choice = input("Enter your choice (1 for Attack, 2 for Defend): ")

        if choice == '1':
            player_attack = player.attack_enemy()
            enemy_defense = enemy.defend()
            if player_attack > enemy_defense:
                damage_dealt = player_attack - enemy_defense
                enemy.take_damage(damage_dealt)
                print(f"You attack the {enemy.name} and deal {damage_dealt} damage!")
            else:
                print(f"The {enemy.name} defends against your attack!")

            enemy_attack = enemy.attack_player()
            player_defense = player.defend()
            if enemy_attack > player_defense:
                damage_taken = enemy_attack - player_defense
                player.take_damage(damage_taken)
                print(f"The {enemy.name} attacks you and deals {damage_taken} damage!")
            else:
                print(f"You defend against the {enemy.name}'s attack!")

        elif choice == '2':
            enemy_attack = enemy.attack_player()
            player_defense = player.defend()
            if enemy_attack > player_defense:
                damage_taken = enemy_attack - player_defense
                player.take_damage(damage_taken)
                print(f"The {enemy.name} attacks you and deals {damage_taken} damage!")
            else:
                print(f"You defend successfully against the {enemy.name}'s attack!")

        else:
            print("Invalid choice. Please enter a valid option.")

        print(f"Your health: {player.health}, {enemy.name}'s health: {enemy.health}")
        print()

    if player.is_alive():
        print(f"Congratulations! You defeated the {enemy.name}.")
    else:
        print("Game Over. You were defeated.")

def main():
    player1 = Player("Hero")
    enemy1 = Enemy("Goblin", 50, 8, 7)

if __name__ == "__main__":
    main()
