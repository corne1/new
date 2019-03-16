# main
print("Enter the AMOUNT of row: ")
n = int(input())
print("The row: ")

fib1 = 0
fib2 = 1

if n < 2:
    quit()

print(fib1, end=' ')
print(fib2, end=' ')

for item in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    if fib2 > 4000000:
        break
    else:
        print(fib2, end=' ')

print("\nEven elements of a row: ")
fib1 = 0
fib2 = 1
for item in range(n):
    fib1, fib2 = fib2, fib1 + fib2
    if fib2 > 4000000:
        break
    if fib2 % 2 == 0:
        print(fib2, end=' ')
