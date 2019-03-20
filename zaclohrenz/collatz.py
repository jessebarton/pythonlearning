def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    elif number % 2 == 1:
        return(3 * number + 1)

print('Give me a number, son.')

while True:
     try: 
         number = int(input())
         while number != 1:
             collatzoutput = collatz(number)
             print(collatzoutput)
             number = collatz(collatzoutput)
         print(1)
         break
     except:
         print('I said a NUMBER.')