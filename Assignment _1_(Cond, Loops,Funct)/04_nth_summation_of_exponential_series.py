# 1^2 + 2^2 + 3^2 + 4^2 +.......+nth_number

nth_number = int(input("> "))
total = 0
i = 1
for j in range(1, nth_number + 1):
    total = j**2 + total
    ##total = (j+1)**2
print(total)
