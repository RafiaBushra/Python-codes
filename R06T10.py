def add_spaces_to_line(row, line_segment, index, line_length):
    num_of_spaces = line_length - len(row)
    row = ""
    while num_of_spaces != 0:
        row += line_segment[index] + " "
        num_of_spaces -= 1
        index += 1
    row += line_segment[index:]
    #return True


def main():
    paragraph = ""
    print("Enter text rows. Quit by entering an empty row.")
    while True:
        sentence = input()
        if sentence == "":
            break
        paragraph += sentence

    line_length = int(input("Enter the number of characters per line: "))
    line = paragraph.split()
    row = ""
    index = 0
    start_index = 0
    line_completed = False
    for i in range(len(line) - 1):
        line[i] += " "
    while len(row) < line_length:
        if len(row + line[index]) <= line_length:
            row += line[index]
            index += 1
        elif len(row + line[index]) - 1 == line_length:
            line[index] = line[index].rstrip()
            #index += 1
        else:
            add_spaces_to_line(row, line[start_index:index], index - len(row), line_length)
            row = ""
            start_index = index
        if len(row) == line_length:
            start_index = index
            row = ""
        print(row)


main()





# def solution1():
    # line = ""
    # index = 0
    # while len(line) < line_length:
    #     if paragraph[index] != " ":
    #         line += paragraph[index]
    #         if len(line) == line_length and paragraph[index + 1] != " ":
    #             for back_index in range(index, line_length - index, -1):
    #                 if paragraph[back_index] != " ":
    #                     line.strip(paragraph[back_index])
    #                 else:
    #                     break
    #     else:
    #         line += paragraph[index] + " "
    #     index += 1
    #     if len(line) == line_length:
    #         print(line)
    #         line = ""