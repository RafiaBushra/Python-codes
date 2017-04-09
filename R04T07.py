#Introduction to Programming
#Car.py
#Student Name: Rafia Bushra
#Student ID: 268449


def menu():
    tank_size  = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size
    gas_consumption = read_number("How many liters of gas does the car " + \
                                 "consume per hundred kilometers? ")
    x = 0.0
    y = 0.0

    MENU_TEXT = "1) Fill 2) Drive 3) Quit \n-> "

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input(MENU_TEXT)

        if choice == "1":
           to_fill = read_number("How many liters of gas to fill up? ")
           gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
           new_x = read_number("x: ")
           new_y = read_number("y: ")
           gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
           break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    if to_fill >= tank_size or float(gas + to_fill) >= tank_size:
        return tank_size
    else:
        return float(gas + to_fill)


def drive(x, y, new_x, new_y, gas, gas_consumption):
    if new_x == x and new_y == y:
        return gas, x, y
    max_distance = gas / (gas_consumption/100)
    gas_consumed = path_length(x, y, new_x, new_y)*(gas_consumption/100)
    if gas > 0:
        return return_value(x, y, new_x, new_y, gas, gas_consumption,
                            gas_consumed, max_distance)
    else:
        return 0.0, x, y


def path_length(x, y, new_x, new_y):
    return float(((new_x - x)**2 + (new_y - y)**2)**.5)


def return_value(x, y, new_x, new_y, gas, gas_consumption, gas_consumed, max_distance):
    if gas_consumed <= gas_consumption and gas_consumed <= gas:
        return float(gas - gas_consumed), new_x, new_y
    elif gas_consumed <= gas:
        return float(gas - gas_consumed), new_x, new_y
    else:
        return 0.0, x + float((max_distance * (new_x - x)) /
                        path_length(x, y,new_x,new_y)),\
               y + float((max_distance * (new_y - y)) / path_length(x, y,
                                                          new_x, new_y))


def read_number(prompt, error_message="Incorrect input!"):
    try:
        return float(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()

main()
