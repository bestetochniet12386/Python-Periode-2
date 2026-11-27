# Fantasy Item Shop 2.0

# Functie om de difficulty te kiezen

def choose_difficulty():
    print("\n=== Choose Difficulty ===")
    print("1. Easy (150 gold)")
    print("2. Normal (100 gold)")
    print("3. Hard (50 gold)")

    while True:
        choice = input("Kies je moeilijkheidsgraad: ").strip()

        if choice == "1":
            return 150
        elif choice == "2":
            return 100
        elif choice == "3":
            return 50
        else:
            print("Ongeldige keuze! Kies 1, 2 of 3.")

# Functie voor het winkelmenu
def show_menu():
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Sell Item")
    print("7. Exit shop")
    print("8. Work (+20 gold)")


# Functie om de inventory te bekijken
def show_inventory(inventory):
    print("\n=== Jouw Inventory ===")

    if len(inventory) == 0:
        print("Je inventory is leeg!")
    else:
        for item in inventory:
            print("-", item)

# Functie om te controleren of de speler genoeg gold heeft
def can_buy(gold, price):
    if gold >= price:
        return True
    else:
        return False


# Functie om een item te kopen
def buy_item(gold, inventory, item_name, price):
    if can_buy(gold, price):
        gold -= price
        inventory.append(item_name)

        print("\nJe hebt een", item_name, "gekocht!")
        print("Je hebt nog", gold, "gold over.")
    else:
        print("\nJe hebt niet genoeg gold!")

    return gold

# Bonus 1
def sell_item(gold, inventory):
    print("\n=== Items verkopen ===")

    if len(inventory) == 0:
        print("Je inventory is leeg!")
    else:
        show_inventory(inventory)

        item_to_sell = input("Welk item wil je verkopen? ").strip()

        if item_to_sell in inventory:
            if item_to_sell == "Sword":
                gold += 25
            elif item_to_sell == "Shield":
                gold += 20
            elif item_to_sell == "Potion":
                gold += 10
            elif item_to_sell == "Bow":
                gold += 30

            inventory.remove(item_to_sell)

            print("Je hebt", item_to_sell, "verkocht!")
            print("Je hebt nu", gold, "gold.")
        else:
            print("Je hebt dit item niet in je inventory!")

    return gold

# Bonus 2
def work(gold):
    gold += 20

    print("\nJe hebt gewerkt en 20 gold verdiend!")
    print("Je hebt nu", gold, "gold.")

    return gold

# Gegevens
player_name = input("Wat is je naam? ")
player_gold = choose_difficulty()

inventory = []

print("\nWelkom in de winkel,", player_name)
print("Je begint met,", player_gold, "goud!")

items = ["Sword", "Shield", "Potion", "Bow"]

print("\nDit zijn de items die je kunt kopen:")

for item in items:
    print(item)

# Winkelmenu
while True:
    show_menu()

    choice = input("\nWat wil je doen? ").strip()

    match choice:

        case "1":
            player_gold = buy_item(
                player_gold, inventory, "Sword", 50
            )

        case "2":
            player_gold = buy_item(
                player_gold, inventory, "Shield", 40
            )

        case "3":
            player_gold = buy_item(
                player_gold, inventory, "Potion", 20
            )

        case "4":
            player_gold = buy_item(
                player_gold, inventory, "Bow", 60
            )

            # Inventory bekijken
        case "5":
            show_inventory(inventory)

            # Items verkopen
        case "6":
            player_gold = sell_item(player_gold, inventory)

            # Winkel verlaten
        case "7":
            print(
                "\nBedankt voor je bezoek aan de winkel,",
                player_name, "!"
            )
            print("Je hebt nog", player_gold, "gold over.")
            print("Tot ziens!")
            break

        # Gold verdienen
        case "8":
            player_gold = work(player_gold)

        # Ongeldige keuze
        case _:
            print(
                "\nOngeldige keuze! Kies een optie van 1 tot en met 8."
            )