total = 0  # set start price

number = int(input("How many items you want to count?: "))

while number < 0:  # error checking
    print("Invalid number of items, Please try again")
    number = int(input("How many items you want to count?:  "))

for i in range(number):  # loops for discounting
    price = float(input("Please enter the Price of each item: "))
    total = total + price

if total > 100:
    total *= 0.9  # 10% discount

print("Total price for these", number, "items is $", total)
