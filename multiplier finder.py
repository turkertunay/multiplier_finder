num = int(input("Enter a number: "))
i = 1
count = 0
while i <= num:
    q = num % i
    if q == 0:
        print(i, "is a quotient of", num)
        count += 1
    i += 1
print("this number has", count, "quotients.")
if count <= 2:
    print("this number is a prime number")
else:
    print("this number is not a prime number")