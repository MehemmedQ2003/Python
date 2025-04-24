# 1) Write Python code to compute the factorial of a number recursively. 

# number = int(input("Enter a number: "))
# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(number))




# 2) Write a Python script to display all prime numbers between 10 and 50.

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# for i in range(10, 51):
#     if is_prime(i):
#         print(i)