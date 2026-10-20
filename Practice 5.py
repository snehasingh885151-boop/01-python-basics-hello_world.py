# 3) Write a program to print numbers from
# 1 to 50 using a while loop

num = 1

while num <= 50:
    if num % 2 == 0:
        print(num)
    num = num + 1


# 4) Write a program that prints the sum of first
# n natural numbers.
# For example, if n = 5, then output should be
# 1 + 2 + 3 + 4 + 5 = 15.

# Hint: Keep a running total inside the loop.

n = int(input("Enter a number:"))
sum = 0

while n >= 1:
    sum = sum + n
    n = n - 1

print("sum =", sum)
print("n =", n)