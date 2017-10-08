my_list = [1,2,3,4,5,6,20]

for item in my_list:
    if my_list[0] < item:
        my_list[0] = item

#    i = i + 1
print(my_list[0])
