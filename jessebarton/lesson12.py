print('Enter a number between 1 - 10')
userEntered = input()

def collatz(number):
        newNumber = number % 2
        # If even, print number // 2 and return this value.
        if newNumber == 0:
                evalNum = newNumber // 2
                print(str(evalNum))
        # If number is odd print 3 * number + 1
        else:
                evalNum = newNumber * 3 + 1
                print(str(evalNum))

collatz(int(userEntered))