#Count Digits
n = int(input("Enter a Number: "))
if n == 0:
    counter = 1
else:
    counter = 0
    while n > 0:
        n = n // 10
        counter += 1
print("No Of Digits", counter)
