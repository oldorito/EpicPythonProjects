import resources

machine_turned_on = True
profit = 0

def report():
    return resources.machine_resources


def resource_check(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources.machine_resources[item]:
            print(f"Not enough {item}.")
            return False
    return True


def make_drink(drink, drink_ingredients):
    for item in drink_ingredients:
        resources.machine_resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink}. Enjoy!")


def transaction(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change, ${change}.")
        profit += drink_cost
        return True
    else:
        print("Not enough money. Money refunded.")
        return False


def coin_processing():
    print("Insert coins.")
    total = int(input("quarters: ")) * 0.25
    total += int(input("dimes: ")) * 0.1
    total += int(input("nickles: ")) * 0.05
    total += int(input("pennies: ")) * 0.01
    return total


while machine_turned_on:
    print("This is Ola's EPIC and TASTY coffee machine!\nIf your coffee tastes like gatorade, well... I don't care.")
    chosen_drink = input("Choose your coffee: espresso/latte/cappuccino\n").lower()
    if chosen_drink == "report":
        print(report())
    elif chosen_drink == "off":
        machine_turned_on = False
    else:
        drink = resources.MENU[chosen_drink]
        if resource_check(drink["ingredients"]):
            payment = coin_processing()
            if transaction(payment, drink["cost"]):
                make_drink(chosen_drink, drink["ingredients"])
