def count_abbas(string):
    ABBA = "abba"
    count = 0
    for index in range(len(string)-3):
        if string[index:index+4] == ABBA:
            count += 1
    return count