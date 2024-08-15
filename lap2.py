def factorial(n):
    if n ==1 or n ==0:
        return 1
    else:
        return n * factorial(n-1)
def prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
num = int(input("Enter a positive number: "))
if prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
print(f"The factorial of {num} is: {factorial(num)}")