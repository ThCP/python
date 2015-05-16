# exercise 01
# Write a program  which detects whether a number is primes

input_value = raw_input("Insert a number > ")
n = long (input_value)
n_prime = 0

print "The number is %d" % n

for i in range (2, n/2):
    if n%i == 0:
        n_prime = 1
        break

if n_prime == 0:
    print "the number is prime"
else:
    print "the number is not prime as it can be divided by %d" %i
    
    