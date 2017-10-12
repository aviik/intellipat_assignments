## 0^2 + ( 0^2 + 1^2 ) + (0^2 + 1^2 + 1^2) +(0^2 + 1^2 + 1^2 + 2^2)+ .......nth number


print("Give the nth number: ")
nth_number = int(input("> "))

i = 0
j = 0
sum = 0
while i <= nth_number:
    total = 0
    for j in range(0,i):
        total = total + j**2
    sum = sum + total
    i = i + 1
print(sum)
