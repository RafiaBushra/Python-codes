# Rbbleh
# ID: 268449


def read_biometric_registry(filename):
    result = []
    handled_passports = []
    row = ""

    try:
        with open(filename, "r") as file_object:
            for row in file_object:
                row = row.rstrip()

                fields = row.split(";")

                if len(fields) != 8:
                    print("Error: there is a wrong number of fields in the "
                          "file:")
                    print("'", row, "'", sep="")
                    return None

                for ind in range(3, 8):
                    fields[ind] = float(fields[ind])
                    if not (0 <= fields[ind] <= 3.0):
                        print("Error: there is a erroneous value in the file:")
                        print("'", row, "'", sep="")
                        return None

                name = fields[0] + ", " + fields[1]
                passport = fields[2]
                biometric = []
                for value in fields[3:]:
                    biometric.append(value)

                if passport in handled_passports:
                    print("Error: passport number", passport, "found multiple "
                                                              "times.")
                    return None

                else:
                    handled_passports.append(passport)

                result.append({passport: {name: biometric}})

        return result

    except FileNotFoundError:
        print("Error: file", filename, "could not be opened.")

    except ValueError:
        print("Error: there's a non-numeric value on row:")
        print("'", row, "'", sep="")

    return None


def get_individual_fields(person):
    passport = ""
    name = ""
    for passport in person.keys():
        break
    for name in person[passport].keys():
        break
    biometric = person[passport][name]
    return passport, name, biometric


def execute_match(registry):
    match_flag = False
    repeat_flag = []
    found_flag = False
    for index1 in range(len(registry) - 1):
        passport1, name1, biometric1 = get_individual_fields(registry[index1])
        if passport1 in repeat_flag:
            break
        if found_flag:
            print()
        found_flag = False
        for index2 in range(index1 + 1, len(registry)):
            passport2, name2, biometric2 = get_individual_fields(registry[index2])
            difference = get_difference(biometric1, biometric2)
            if difference < 0.1:
                match_flag = True
                repeat_flag.append(passport2)
                if not found_flag:
                    print("Probably the same person:")
                    found_flag = True
                    print_suspects(passport1, name1, biometric1)
                print_suspects(passport2, name2, biometric2)

    if not match_flag:
        print("No matching persons were found.")
    return


def print_suspects(passport, name, biometric):
    print(name, ";", passport, ";", sep="", end="")
    for i in range(len(biometric)):
        if i == len(biometric) - 1:
            print(format(biometric[i], ".2f"))
        else:
            print(format(biometric[i], ".2f"), ";", sep="", end="")
    return


def get_difference(first_list, second_list):
    result = 0.0
    for index in range(len(first_list)):
        result += (first_list[index] - second_list[index])**2
    from math import sqrt
    result = sqrt(result)
    return result


def take_search_input(registry):
    values = 0
    try:
        values = input("enter 5 measurement points separated by semicolon: ")
        values = values.split(";")
        for index in range(len(values)):
            values[index] = float(values[index])
        if len(values) != 5:
            print("Error: wrong number of measurements. Try again.")
            return take_search_input(registry)
    except ValueError:
        if len(values) != 5:
            print("Error: wrong number of measurements. Try again.")
        else:
            print("Error: enter floats only. Try again.")
        return take_search_input(registry)
    return values


def execute_search(registry):
    found_flag = False
    search_values = take_search_input(registry)
    for person in registry:
        for passport in person.keys():
            break
        for name in person[passport].keys():
            break
        biometric = person[passport][name]
        euclidian_difference = get_difference(search_values, biometric)
        for index in range(len(biometric)):
            if search_values[index] == biometric[index] and euclidian_difference < 0.1:
                if not found_flag:
                    print("Suspects found:")
                    found_flag = True
                print_suspects(passport, name, biometric)
                break
            elif euclidian_difference < 0.1:
                if not found_flag:
                    print("Suspects found:")
                    found_flag = True
                print_suspects(passport, name, biometric)
                break
    if not found_flag:
        print("No suspects were found.")
    return


def command_line_user_interface(registry):
    while True:
        command = input("command [search/match/<enter>] ")
        if command == "":
            return
        elif command == "match":
            execute_match(registry)
        elif command == "search":
            execute_search(registry)
        else:
            print("Error: unknown command '", command,
                  "': try again.", sep="")


def main():
    registry_file = input("Enter the name of the registry file: ")

    biometric_registry = read_biometric_registry(registry_file)
    if biometric_registry is not None:
        command_line_user_interface(biometric_registry)


main()
