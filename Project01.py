#Introduction to Programming
#Project01
#Student Name: Rafia Bushra
#Student ID: 268449

def main():
    prev_result = 0.0
    result = 0.0
    count = int(input("Enter the number of the measurements:"))
    flag = 0
    if count <= 0:
        print("Error: the number must be expressed as a positive integer.")
    else:
        for i in range(1,count+1):
            next_result = float(input("Enter the measurement result "+str(i)
                                      + ": "))
            if next_result > 8 or next_result < 6:
                print("The conditions are not suitable for zebra fishes.")
                flag = 1
                break
            elif i > 1 and abs(next_result - prev_result) > 1.0:
                print("The conditions are not suitable for zebra fishes.")
                flag = 1
                break
            else:
                result += next_result
                prev_result = next_result
        if flag == 0:
            print("Conditions are suitable for zebra fishes. The average pH is"
                  " ", format(result/count, '.2f'), ".", sep="")

main()
