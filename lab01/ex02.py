# exercise 2
# write a program which, given n, computes the Fibonacci series of order n

n = int (raw_input("insert n: "))

a1 = 0
a2 = 1

for i in range (0, n):
    temp = a1
    a1 = a2
    a2 = temp+a2
    print a1
    