precios = {'sheep': 6769, 'cow': 3848, 'pig': 1296, 'goat': 678, 'chicken': 23} 


def print_animals(dinero, animal_name):
    number = int(dinero / precios[animal_name])
    if number > 1:
        if animal_name != "sheep":
            print(number, animal_name + "s")
        else:
            print(number, "sheep")
    else:
        print("1", animal_name)


coins = int(input())
if coins >= precios['sheep']:
    print_animals(coins, "sheep")
elif coins >= precios['cow']:
    print_animals(coins, "cow")
elif coins >= precios['pig']:
    print_animals(coins, "pig")
elif coins >= precios['goat']:
    print_animals(coins, "goat")
elif coins >= precios['chicken']:
    print_animals(coins, "chicken")
else:
    print("None")
