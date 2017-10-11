## Try reimplementing the factorial function using an iterator.
## Which do you think is better? Which do you think is easier to understand?


def facto(num):
    fact = 1

    for i in range(1, num+1):
        fact = fact * i

    print(fact)


facto(5)