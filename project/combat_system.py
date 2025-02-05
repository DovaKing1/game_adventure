import random

class Character:
    """Base class for both Player and Enemy."""
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        """Reduces health by the amount of damage taken, ensuring it doesn't go negative."""
        self.health = max(0, self.health - damage)

    def roll_attack(self):
        """Rolls a D20 plus attack bonus."""
        return random.randint(1, 20) + self.attack

    def roll_defense(self):
        """Rolls a D12 plus defense bonus."""
        return random.randint(1, 12) + self.defense

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"


class Player(Character):
    """Player-controlled character."""
    def __init__(self, name):
        super().__init__(name, health=100, attack=10, defense=5)


class Enemy(Character):
    """Enemy AI-controlled character."""
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)


def battle(player, enemy):
    """Handles turn-based combat between player and enemy."""
    print(f"\nA wild {enemy.name} appears!\n")
    
    turn = 1
    while player.is_alive() and enemy.is_alive():
        print(f"\n--- TURN {turn} ---")
        print(f"{player.name} Health: {player.health} | {enemy.name} Health: {enemy.health}\n")
        
        # Player's Turn
        print(f"{player.name}'s Turn:")
        action = input("Choose an action: [1] Attack, [2] Defend: ").strip()
        
        if action == "1":  # Attack
            player_attack = player.roll_attack()
            enemy_defense = enemy.roll_defense()
            
            print(f"{player.name} rolls an attack: {player_attack}")
            print(f"{enemy.name} rolls a defense: {enemy_defense}")
            
            if player_attack > enemy_defense:
                damage = player_attack - enemy_defense
                enemy.take_damage(damage)
                print(f"{player.name} hits {enemy.name} for {damage} damage!")
            else:
                print(f"{enemy.name} blocks the attack.")

        elif action == "2":  # Defend
            print(f"{player.name} is in a defensive stance.")
        
        else:
            print("Invalid action! You lose your turn.")

        if not enemy.is_alive():
            print(f"\n{player.name} has defeated {enemy.name}.")
            break

        # Enemy's Turn
        print(f"\n{enemy.name}'s Turn:")
        enemy_choice = random.choice(["attack", "defend"])
        
        if enemy_choice == "attack":
            enemy_attack = enemy.roll_attack()
            player_defense = player.roll_defense()
            
            print(f"{enemy.name} rolls an attack: {enemy_attack}")
            print(f"{player.name} rolls a defense: {player_defense}")
            
            if enemy_attack > player_defense:
                damage = enemy_attack - player_defense
                player.take_damage(damage)
                print(f"{enemy.name} hits {player.name} for {damage} damage!")
            elif player_defense > enemy_attack + 5:  # Counterattack chance
                counter_damage = random.randint(5, 15)
                enemy.take_damage(counter_damage)
                print(f"{player.name} counterattacks and deals {counter_damage} damage!")
            else:
                print(f"{player.name} blocks the attack.")

        elif enemy_choice == "defend":
            print(f"{enemy.name} is in a defensive stance.")

        if not player.is_alive():
            print("\nYou were defeated. Game Over.")
            break

        turn += 1


# Main function to initiate battle
def main():
    player1 = Player("Hero")
    enemy1 = Enemy("Goblin", 50, 8, 7)
    battle(player1, enemy1)


if __name__ == "__main__":
    main()
