def shop():
    print("Hello, Welcome to this shop.\nWe sell only the highest of tier items.")

    items = {
        "[1] Sword": 50,
        "[2] Shield": 30,
        "[3] Potion": 10,
        "[4] Helmet": 20
    }

    print("\nHere are the items we have for sale:")
    for num, item, price in items.items():
        print(f"{num}{item}: ${price}")

    balance = 100  # Starting balance
    print(f"\nYou have ${balance}.")

    while True:
        choice = input("\nWhat would you like to buy? (type 'exit' to leave): ").lower()
        if choice == "exit":
            print("Thank you for visiting the shop!")
            break
        elif choice in items:
            if balance >= items[choice]:
                balance -= items[choice]
                print(f"You bought a {choice} for ${items[choice]}.")
                print(f"Remaining balance: ${balance}")
            else:
                print("You don't have enough money for that item.")
        else:
            print("Sorry, we don't have that item.")
