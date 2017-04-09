# Introduction to Programming
# Project02: Coffee gallup
# Student Name: Rafia Bushra
# Student ID: 268449


def non_coffee_drinkers(intake_list):
    count = 0
    for index in range(len(intake_list) - 1, -1, -1):
        if intake_list[index] == 0:
            count += 1
            intake_list.remove(0)
    return count


def make_bar_diagram(intake_list):
    HIGHEST_VALUE = intake_list[len(intake_list) - 1]
    LOWEST_VALUE = intake_list[0]
    for index in range(LOWEST_VALUE, HIGHEST_VALUE + 1):
        print(format(index, '2d'), end=" ")
        for i in range(len(intake_list)):
            if intake_list[i] == index:
                print("#", end="")
        print()


def most_common_response(intake_list):
    maximum = 0
    i = len(intake_list) - 1
    prev_count = 0
    HIGHEST_VALUE = intake_list[len(intake_list) - 1]
    LOWEST_VALUE = intake_list[0]
    for value in range(HIGHEST_VALUE, LOWEST_VALUE - 1, -1):
        count = 0
        while i >= 0 and intake_list[i] == value:
            count += 1          # Checking how many repetitions there are of
            i -= 1              # each response.
        if count >= prev_count:
            maximum = value     # Storing the response value in case this is
            prev_count = count  # the most common response.
    return maximum


def responses_differing_by_1_from_most_common(intake_list):
    LOWER_LIMIT = most_common_response(intake_list) - 1
    UPPER_LIMIT = most_common_response(intake_list) + 1
    count = 0
    for index in range(len(intake_list)):
        if LOWER_LIMIT <= intake_list[index] <= UPPER_LIMIT:
            count += 1
    return make_percentage(count, len(intake_list))


def make_percentage(numerator, denominator):
    return float((numerator / denominator) * 100)


def drinks_more_than_4_cups(intake_list):
    RECOMMENDED_AMOUNT = 4
    count = 0
    for i in range(len(intake_list)):
        if intake_list[i] > RECOMMENDED_AMOUNT:
            count += 1
    return make_percentage(count, len(intake_list))


def drinks_5_to_8_cups(intake_list):
    LOWER_LIMIT = 5
    UPPER_LIMIT = 8
    count = 0
    for index in range(len(intake_list)):
        if LOWER_LIMIT <= intake_list[index] <= UPPER_LIMIT:
            count += 1
    return count


def drinks_over_8_cups(intake_list):
    LOWER_LIMIT = 8
    count = 0
    for index in range(len(intake_list)):
        if LOWER_LIMIT < intake_list[index]:
            count += 1
    return count


def print_responses_over_8(intake_list):
    LOWER_LIMIT = 8
    for index in range(len(intake_list)):
        if LOWER_LIMIT < intake_list[index]:
            print(intake_list[index])


def main():
    print("Enter one response per line. End by entering an empty row.")
    intake_list = []
    abusers_exist = False
    double_abuse = False
    while True:
        list_input = input()
        if list_input != "":
            intake_list.append(int(list_input))
        else:
            break
    no_coffee = non_coffee_drinkers(intake_list)
    if no_coffee > 0:
        print("Removed", no_coffee, "non-coffee-drinkers responses\n")

    if len(intake_list) > 0:
        print("Information related to coffee drinkers:")
        copied_list = sorted(intake_list)
        make_bar_diagram(copied_list)

        print()
        # Since the list is now sorted, the greatest response is at the end
        print("The greatest response:"
              , copied_list[len(copied_list) - 1]
              , "cups of coffee per day")
        print("The most common response:"
              , most_common_response(copied_list)
              , "cups of coffee per day")
        print(format(responses_differing_by_1_from_most_common(copied_list)
                     , '.1f')
              , "% of the respondents drink "
              , most_common_response(copied_list) - 1
              , "-", most_common_response(copied_list) + 1
              , " cups of coffee per day", sep="")
        # Checking if there are any responses over 4 cups every day
        for response in copied_list:
            if response > 4:
                abusers_exist = True
                if response > 8:
                    double_abuse = True
                    break
        if abusers_exist:
            print()

            print("Information related to coffee abusers:")
            print(format(drinks_more_than_4_cups(copied_list), '.1f')
                  , "% of the respondents drink more than 4 cups of coffee per day"
                  , sep="")
            print(drinks_5_to_8_cups(copied_list)
                  , "respondents drink a little too much coffee (5-8 cups per day)")
            print(drinks_over_8_cups(copied_list)
                  , "respondents drink over double the recommendation")
            if double_abuse:
                print("The responses over 8 cups of coffee per day:")
                # Here I call the function with the original, unsorted list.
                print_responses_over_8(intake_list)
main()
