from decimal import Decimal, getcontext
from math import ceil, factorial

def pi(n):
    n += 2
    getcontext().prec = n
    num_iterations = ceil(n / 14)
    constant_term = 426880 * Decimal(10005).sqrt()
    exponential_term = 1
    num = 13591409
    partial_sum = Decimal(num)
                
    for i in range(1, num_iterations):
        num1 = factorial(6 * i) // (factorial(3 * i) * factorial(i) ** 3)
        num = num + 545140134
        exponential_term = exponential_term * -262537412640768000
        partial_sum += (num1 * num) / exponential_term
    return str(Decimal(constant_term / partial_sum))[:-1]
