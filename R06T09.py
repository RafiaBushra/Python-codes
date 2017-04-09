def longest_substring_in_order(string):
    list_of_strings = []
    index = 0
    i = 0
    if len(string) < 2:
        return string
    while True:
        count = 0
        for second_index in range(index, len(string)-1):
            if string[second_index] > string[second_index+1]:
                break
            else:
                count += 1
                if second_index == len(string) - 2:
                    break
        if count > 0:
            list_of_strings.append(string[index:index+count+1])
            i += 1
        index = second_index + 1
        if second_index == len(string) - 2:
            break
    if len(list_of_strings) == 0:
        return string[0]
    if len(list_of_strings) == 1:
        return list_of_strings[0]
    list_of_strings.sort(key=len)
    if len(list_of_strings[0]) == len(list_of_strings[len(list_of_strings) - 1]):
        return list_of_strings[0]
    return list_of_strings[len(list_of_strings) - 1]
print(longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm"))
