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

def calculate_average(numbers):
    if len(numbers):
        return None
    else:
        total = sum(numbers) 
        return total / len (numbers)
input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in input_numbers.split()]
average = calculate_average(numbers)
if average is None:
    print("No numbers provided.")
else:
    print("The average of the numbers is: (average)")
above_average = []
below_average = []
for num in numbers:
    if num > average:
        above_average.append(num)
    elif num < average:
        below_average.append(num)
print("Numbers above the average:", above_average)
print("Numbers below the average:", below_average)

student_scores = []
while True:
     score_input = input("Enter the student's score (or type 'done' to finish): ")
     if score_input.lower() == 'done':
            break
     score = float(score_input)
     student_scores.append(score)
     if not student_scores:
        print("No scores entered.")

print("\nGrades for each student:")
for i, score in enumerate(student_scores, start=1):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
         grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
print(f"Student {i}: Score = {score}, Grade = {grade}")
