#Write a Python program to sum all the items in a list (of integers)
# i tried to make this interactive, but not being able to implement my ideas fully

items = []

#context menu
def banner():
    my_string = "Program to add to add all iems in a list: "
    print(my_string)
    print('-'*(len(my_string) - 1))
    print('')
    my_choice = input("continue Y/N ? >").lower().strip()
    while True:
        if my_choice == "y":
            help_menu()
        else:
            break



def help_menu():
        print("""
                Type 'M' for menu,
                Type 'Q' to stop adding items
                Type 'A' to continue adding next item
                Type 'D' remove last item of list

                """)
        my_menu()

#menu
def my_menu():
        user_input = input('==>')
        if user_input == "m" or user_input == "M":
            help_menu()
        elif user_input == "Q" or user_input == "q":
            list_add()
        elif user_input == "A" or user_input == "a":
            list_append()
        elif user_input == "D" or user_input == "d":
            list_pop()
        else:
            print("NOT A VALID INPUT!")

#adding items to the list
def list_append():
    my_number = int(input('Give me a number ==>'))
    items.append(my_number)
    print("                 {} items in list".format(len(items)))
    print("Type 'A' to continue adding next item or 'Q' see the total or 'D' remove last item")
    my_menu()


def list_pop():
    items.pop()
    return items

#the adding engine
def list_add():
    total = 0
    while True:
        for item in items:
            total = total + item
        print("The total is {}".format(total))
        break

if __name__ == '__main__':
    banner()
