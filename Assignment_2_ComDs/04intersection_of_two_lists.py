# Write a Python function that takes two lists and returns True if they have at least one common member.


# my_fruits = ["apple", "banana", "strawberry", "orange", "pomegranate", "grapes", "mangoes"]
# my_berries = ["blueberry", "gooseberry", "raspberry","strawberry"]

my_list = []
my_lists = []

def my_menu():
	while len(my_list) < 10:
		foo = input("What to add to first list :")
		if foo.lower().strip() == 'done':
			break
		my_list.append(foo)
	my_lists_menu()	


def my_lists_menu():
	while len(my_lists) < 10:
		foo = input("What to add to second list :")
		if foo.lower().strip() == 'done':
			break
		my_lists.append(foo)
	my_iterator(my_list, my_lists)
	
		

def my_iterator(my_list, my_lists):
	for items in my_list:
		if items in my_lists:
			return True

if __name__ == '__main__':
	my_menu()
