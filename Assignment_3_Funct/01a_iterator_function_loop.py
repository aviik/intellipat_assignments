## Try reimplementing the factorial function using while loop/iterator.
## Which do you think is better? Which do you think is easier to understand?

def facto():
    fact = 1
    num = int(input("Enter Number: "))
    for i in range(1, num+1):
        fact = fact * i

    print("Factorial by iteration of {} is {}.".format(num , factorial))






def simple_factoriser():
    num = int(input("Enter Number: "))
    counter = 1
    fact = 1

    while counter <= num:
        fact = counter * fact
        counter = counter + 1 
    print("Factorial by iteration of {} is {}.".format(num , factorial))





# mixed itertor in while loop
##factorial = 1
##foo = int(input("Enter Number: "))

def factoriser(factorial = 1):
    while True:
        try:
            foo = int(input("Enter Number: "))
            if foo < 0:
                print("Hello! Enter a Positive Number Man......")
                continue
            elif foo == 0:
                print("Zero")
                break
            else:
                for i in range(1, foo+1):
                    factorial *= i
                print("Factorial of {} is {}.".format(foo , factorial))
                break
        except ValueError:
            print("Hey this is not allowed.")
            continue


if __name__ == '__main__':
#   factoriser()
#   simple_factoriser()
   facto()         
