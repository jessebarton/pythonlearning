
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    # colWidths = [0] * len(tableData)
    for data in tableData:
        for d in data:
            print(d.rjust(10))

if __name__ == "__main__":
    printTable(tableData)