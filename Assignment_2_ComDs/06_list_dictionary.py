## Suppose you have the list:
## ['dog', 'pencil', 'fence', 'dog', 'apple', 'dog', 'dog', 'dog', 'pear', 'pencil', 'pear', 'pear']
## Using a dictionary, compute the numbers of times each word occurs.
my_list = ['dog', 'pencil', 'fence', 'dog', 'apple', 'dog', 'dog', 'dog', 'pear', 'pencil', 'pear', 'pear']

my_dict = {}
for item in my_list:
    if item not in my_dict:
        my_dict[item] = my_list.count(item)
print(my_dict)
