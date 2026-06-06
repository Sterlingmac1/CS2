def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial (n-1)

def summation(n):
    if n == 1:
        return 1
    else:
        return n + summation(n-1)
    
def exponential(base, power):
    if power == 0:
        return 1
    return base * exponential(base, power-1)

def fibanacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

def sum_digits(n):
    n = str(n)

    if n == '':
       return 0
    return int(n[0]) + sum_digits(n[1:])

def reverse_digits(n):
    n = str(n)

    if n == '':
       return n
    return int(n[-1] + str(reverse_digits(n[:-1])))

print(reverse_digits(15732))

def product_digits(f):
    f = str(f)
    
    if f == '':
       return 0
    return int(f[0]) * product_digits(f[1:])
    
def number_product(f, n):
    if n == 0:
        return 0
    return f * exponential(f, n-1)

def sum_of_numbers_range(f,n):
    if f == n:
        return f 
    return f + sum_of_numbers_range(n, f-1)


