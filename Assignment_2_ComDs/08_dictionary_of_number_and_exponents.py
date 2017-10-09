## Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
## Sample Dictionary ( n = 5) :
## Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

my_dict = {}
n = int(input("Enter the vavue of n: "))
my_list = range(1,n+1)
counts = 0
for item in my_list:
    if item not in my_dict:
        my_dict[item] = item**2
           
print(my_dict)
