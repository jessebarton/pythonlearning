myList = [] 

while True:
    print('Enter an item to be added to the list: ' + str(len(myList) +1) + ' (Or enter nothing to stop.):')
    item = input() #add input items to the list
    if item == '':
        break
    myList = myList +[item] #concatenate list
print('Items in the list are:')
print(*myList, sep = ", ") 