#5.Write a Python program to convert a list of characters into a string.

# enter some characters
my_char = []
while True:
    foo = input("==>")
    if foo == 'done':
        break

    my_char.append(foo)

def string_maker(my_char):
    my_string = ''.join(my_char)
    print(my_string)



string_maker(my_char)
