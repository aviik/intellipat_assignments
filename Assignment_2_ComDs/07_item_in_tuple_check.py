## Write a Python program to check whether an element exists within a tuple


print("Guess whats in my tuple")
print("Here is a hint : its a fruit basket")
test_element = input("check if this element is in the tuple :")
my_tuple = ("apple", "bananas", "orange", "mango", "pomegranate")
for item in my_tuple:
    if item == test_element:
        print("Yay! You Got it!")
        break
    elif item != test_element:
        print(" Tough luck ")
        break
