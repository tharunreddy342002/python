n = int(input("Enter a number:"))
result = 1
while n > 0 :
    result *= n
    n = n - 1
print("Factorial : ",result)