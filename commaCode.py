myList = [] 

while True:
    print('Enter an item to be added to the list: ' + str(len(myList) +1) + ' (Or enter nothing to stop.):')
    item = input()
    if item == '':
        break
    myList = myList +[item] #concatenate list
print('Items in the list are:')
for Items in myList:
        print(*myList, sep = ", ") 