## Write a function which squares a number and then use it to write a function
## which takes three integers and returns the sum of their squares.
def squarer(foo):
    squared = foo**2
    return squared

while num <= 3:
    try:
        my_num = int(input('==> '))


    except ValueError:
        print("Hey Thats not a number")


