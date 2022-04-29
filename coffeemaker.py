MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

while True:
    choice = input("What would you like (espresso/latte/cappuccino):")
    if choice in ["espresso", "latte", "cappuccino"]:
        for key in MENU[choice]["ingredients"]:
            if MENU[choice]["ingredients"][key] > resources[key]:
                print("Sorry, there is not enough", key, ".")
                break
            else:
                print("Please insert your coins.")
                quarters = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickels = int(input("How many nickels: "))
                pennies = int(input("How many pennies: "))
                total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
                if total < MENU[choice]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                    break
                elif total > MENU[choice]["cost"]:
                    change = round((total - MENU[choice]["cost"]), 2)
                    print("Here is your $" + str(change), "in change!")
                    print("Enjoy your", choice, "!")
                    resources[key] -= MENU[choice]["ingredients"][key]
                    money += MENU[choice]["cost"]
                    break
                else:
                    print("Enjoy your", choice, "!")
                    resources[key] -= MENU[choice]["ingredients"][key]
                    money += MENU[choice]["cost"]
                    break
    elif choice == "report":
        print("Water:", resources["water"])
        print("Milk:", resources["milk"])
        print("Coffee:", resources["coffee"])
        print("Money: $"+ str(money))
    elif choice == "off":
        break
    else:
        print("Invalid input! Please choose again.")
