# Task 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(7))
print(is_prime(1))
print(is_prime(13))

# Task 2

def digit_sum(k):
    s = 0
    for digit in str(k):
        s += int(digit)
    return s

print(digit_sum(24))
print(digit_sum(502))
print(digit_sum(12345))

# Task 3

def powers_of_two(N):
    k = 1
    result = []
    while 2**k <= N:   
        result.append(2**k)
        k += 1
    return result

print(powers_of_two(10))  
print(powers_of_two(1))   
print(powers_of_two(20))  
