## 1^2 + ( 1^2 + 2^2 ) + (1^2 + 2^2 + 3^2) + .......+nth_number
print("Give the nth number: ")
nth_number = int(input("> "))

i = 1
j = 1
sum = 0
while i <= nth_number:
    total = 0
    for j in range(0,i+1):
        total = total + j**2
    sum = sum + total
    i = i + 1
print(sum)
