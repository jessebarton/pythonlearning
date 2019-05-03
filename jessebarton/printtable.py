
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    for k in range(len(table[0])):
        for v in range(len(table)):
            print(table[v][k].rjust(10), end = ' ')
        print()


if __name__ == "__main__":
    printTable(tableData)