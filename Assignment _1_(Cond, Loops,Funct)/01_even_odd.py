#Write a while loop wher you take the integer input from command prompt,
#and if the number n is odd print "Number is odd" else print "Number is even".

while True:
    try:
        n = int(input("Give me a number: "))
        if n % 2 == 0 and n != 0:
            print ("The number is even")
        elif n % 2 != 0 and n != 0:
            print ("The number is odd")
        elif n == 0:
            print ("I dont know if {} is even or odd".format(n))
        else:
            break
    except ValueError:
        print("Only Natural Numbers Please!")
        continue



## I have a problem in getting out of the loop with an user input like "done"
