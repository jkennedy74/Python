# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Sweedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)
# The amount of candy the user will be allowed to choose

candyCart = []
answer ="Y"

while answer == "Y":

    yum = input("What candy do you want?")
    candyCart.append(candyList[int(yum)])  
    answer = input("Do you want more candy??  Y/N") 

print("Your cart contains " + str(candyCart))   


