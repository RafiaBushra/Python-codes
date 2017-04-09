price = int(input("Purchase price: "))
if price < 0:
    print("Bad input!")
paid = int(input("Paid amount of money: "))
if paid < 0:
    print("Bad input!")
if price == paid:
    print("No change")
else:
    print("Offer change:")
    change = paid - price
    if change >= 10:
        print(change // 10," ten-euro notes")
        change %= 10
    if change >= 5:
        print(change // 5," five-euro notes")
        change %= 5
    if change >= 2:
        print(change // 2," two-euro coins")
        change %= 2
    if change == 1:
        print(change,"one-euro coins")