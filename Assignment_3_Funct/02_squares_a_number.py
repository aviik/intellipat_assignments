## Write a function which squares a number and then use it to write a function
## which takes three integers and returns the sum of their squares.



##function to square numbers input
def squarer(foo):
    squared = foo**2
    return squared


items = []

## interactive input and populating the list of three numbers
def sqare_inputter():
    count = 1
    tots = 0
    while count<=3:
        try:
            my_input = int(input("Enter Number {}: ".format(count)))
            items.append(squarer(my_input))

        except ValueError:
            print("Hey thats not a number!")
            continue
        count +=1

    for item in items:
        tots = tots + item
    print("Sum of their squares is: {} ".format(tots))


sqare_inputter()
#print(items)
