# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Sweedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)
# The amount of candy the user will be allowed to choose
allowance = 5
candyCart = []

for selection in range(allowance):
    yum = input("What candy do you want?")
    candyCart.append(candyList[int(yum)])   
    print("Your cart contains " + str(candyCart))   


