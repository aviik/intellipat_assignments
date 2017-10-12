
#menu
def my_menu():
    print('  ' + '#'*31)
    print("  ##   1. Write your Name      ##")
    print("  ##   2. Say Hello Name       ##")
    print("  ##   3. Exit the programme   ##")
    print('  ' + '#'*31)
    my_choice()

def my_choice():
    while True:
        choices = input("What is you option : _ _")
        if choices == "1":
            names = input("Write your Name : ").upper()
        elif choices =="2":
            my_name = input("Write your Name : ").upper()
            print("Hello " + my_name)
        elif choices == "3":            #Exit the programme
            print("Exiting")
            break
        else:
            my_menu()
    print("bye!")

if __name__ == '__main__' :
    my_menu()
