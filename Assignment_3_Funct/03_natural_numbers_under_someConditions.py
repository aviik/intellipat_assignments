## Write a function which prints the natural numbers less than  nn
## which are divisible by 3, divisible by 5 but not divisible by 10

def divisible():
    print("Enter the range of natural numbers to be analyzed.")
    while True:
        try:
            print("Enter the lowest number in the range")
            num_lower = int(input('==>'))
            if num_lower < 0 :
                print("Natural numbers are greater than zero")
            print("Enter the highest number in the range")
            num_upper = int(input('==>'))
            if num_upper < 0 :
                print("Natural numbers are greater than zero")
            else:
                break
        except ValueError:
            print("Please input whole numbers only")
            continue

        continue

    for i in range(num_lower,num_upper,1):
        if i % 3 == 0 and i % 5 == 0 and i % 10 != 0:
            print(i)

if __name__ == '__main__':
    divisible()
