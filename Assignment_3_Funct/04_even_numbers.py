## Write a Python program to print the even numbers from a given list.

my_numbers = []
def my_menu():
    print( """
       Enter Numbers below and type any character when finished populating list..
""")


def number_lister():
    while True:
        try:
            num = int(input("==>"))
            if num % 2 == 0:
                my_numbers.append(str(num))
            else:
                continue
        except ValueError:
            if len(my_numbers)<1:
                print("No even numbers given")
                my_menu()
            elif len(my_numbers) == 1:
                print("{} is even".format(my_numbers))
                break
            else:
                print("The even numbers are: {}".format(",".join(my_numbers)))
                break



if __name__ == '__main__':
    my_menu()
    number_lister()
