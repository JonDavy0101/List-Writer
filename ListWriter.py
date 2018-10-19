"""
List Writer v0.1
by: Jonathan Chapman
date: October 18, 2018
"""

optionsArray = ["1. Add item", "2. Delete item", "3. Save and close"]
listArray = []
enterListName = ""
optionsList = ""

def listName():
    global enterListName
    enterListName = input("\nEnter the name of your list: ")
def addItem():
    while True:
        print("\n-------------------------\n-------------------------\n\n" + enterListName, "\n")
        x = 1
        for y in listArray:
            print(x, ". ", y, sep = '')
            x += 1
        enterItem = input("\nEnter item or just hit ENTER: ")
        if enterItem == '':
            break
        listArray.append(enterItem)
def removeItem():
    while True:
        print("\n-------------------------\n-------------------------\n" + enterListName, "\n")
        x = 1
        for y in listArray:
            print(x, ". ", y, sep = '')
            x += 1
        try:
            enterItem = input("\nEnter number of item you want to delete or just hit ENTER: ")
            if enterItem == '':
                break
            else:
                enterItem = int(enterItem)
                enterItem = enterItem - 1
                if enterItem > len(listArray):
                    print("\nSorry, this number does not correspond with the items on your list.")
                    pass
                else:
                    del listArray[enterItem]
        except:
            if enterItem == '':
                break
            else:
                print("\nSorry, this is not a number.")
def saveList():
    with open("List.txt", "w") as results:
        results.write(enterListName + "\n\n")
        for y in listArray:
            results.write("__ " + y + "\n")
    print("\nYour list has been saved in a text file called \"List\" in the")
    print("same location as this program. Enjoy!\n")


# Main code
listName()
while True:
    print("\n-------------------------\n-------------------------\n\n" + enterListName, "\n")
    x = 1
    for y in listArray:
        print("__ ", y, sep='')
    print("\n-------------------------\n")
    for z in optionsArray:
        print(z)
        x += 1
    try:
        optionsList = int(input("\nEnter number of action you want to take: "))
        if optionsList == 1:
            addItem()
        elif optionsList == 2:
            removeItem()
        elif optionsList == 3:
            saveList()
            print("")
            break
        elif optionsList > 3:
            print("\nSorry, this number does not correspond with the options list.")
    except:
        print("\nSorry, this is not a number.\n")
        pass