def main():
    list = [630,1015,1415,1620,1720,2000]
    time = int(input("Enter the time (as an integer): "))
    i = 0
    count = 0
    print("The next buses leave:")
    while count != 3:
        if i >= len(list) and count < 3:
            print(list[i- len(list)])
            count += 1
            i += 1
            continue
        if time <= list[i]:
            print(list[i])
            count += 1
        i += 1
main()
