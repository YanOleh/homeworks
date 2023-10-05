import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

operator = random.choice(['+', '-', '*', '/'])

answer = input(f'Write the correct answer: {num1} {operator} {num2} = ')

if operator == '+':
    expected_answer = num1 + num2
elif operator == '-':
    expected_answer = num1 - num2
elif operator == '*':
    expected_answer = num1 * num2
elif operator == '/':
    expected_answer = num1 / num2

if int(answer) == expected_answer:
    print("Great, correct!")
else:
    print(f"Wrong... The correct answer is {expected_answer}")
