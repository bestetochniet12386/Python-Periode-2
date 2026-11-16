player_name = input("Wat is je naam? ")

player_gold = 100

inventory = []

print("Welkom in de winkel,", player_name)
print("Je begint met,", player_gold, "goud!")

items = ["Sword", "Shield", "Potion", "Bow"]

print("\nDit zijn de items die je kunt kopen:")

for item in items:
    print(item)


# Winkelmenu
while True:
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Sell Item")
    print("7. Exit shop")

    choice = input("\nWat wil je doen? ").strip()


    # Items kopen

    match choice:
        case "1":
            if player_gold >= 50:
                player_gold -= 50
                inventory.append("Sword")
                print("\nJe hebt een sword gekocht!")
                print("Je hebt nog", player_gold, "gold over.")
            else:
                print("\nJe hebt niet genoeg gold!")

        case "2":
            if player_gold >= 40:
                player_gold -= 40
                inventory.append("Shield")
                print("\nJe hebt een Shield gekocht!")
                print("Je hebt nog", player_gold, "gold over.")
            else:
                print("\nJe hebt niet genoeg gold!")

        case "3":
            if player_gold >= 20:
                player_gold -= 20
                inventory.append("Potion")
                print("\nJe hebt een potion gekocht!")
                print("Je hebt nog", player_gold, "gold over.")
            else:
                print("\nJe hebt niet genoeg gold!")

        case "4":
            if player_gold >= 60:
                player_gold -= 60
                inventory.append("Bow")
                print("\nJe hebt een Bow gekocht!")
                print("Je hebt nog", player_gold, "gold over.")
            else:
                print("\nJe hebt niet genoeg gold!")

        # Inventory bekijken

        case "5":
            print("\n=== Jouw Inventory ===")

            if len(inventory) == 0:
                print("Je inventory is leeg!")
            else:
                for item in inventory:
                    print("-", item)


        # Items verkopen

      
        case "6":
            print("\n=== Items verkopen ===")

            if len(inventory) == 0:
                print("Je inventory is leeg!")
            else:
                for item in inventory:
                    print("-", item)

                sell_item = input("Welk item wil je verkopen? ")

                if sell_item in inventory:
                    if sell_item == "Sword":
                        player_gold += 25
                    elif sell_item == "Shield":
                        player_gold += 20
                    elif sell_item == "Potion":
                        player_gold += 10
                    elif sell_item == "Bow":
                        player_gold += 30

                    inventory.remove(sell_item)

                    print("Je hebt", sell_item, "verkocht!")
                    print("Je hebt nu", player_gold, "gold.")

                else:
                    print("Je hebt dit item niet in je inventory!")

        # Winkel verlaten

        case "7":
            print("\nBedankt voor je bezoek aan de winkel,", player_name, "!")
            print("Je hebt nog", player_gold, "gold over.")
            print("Tot ziens!")
            break

        # Ongeligde keuze

        case _:
            print("\nOngeldige keuze! Kies een optie van 1 tot en met 7.")