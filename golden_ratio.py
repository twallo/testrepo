from fractions import Fraction

def golden_ratio(n):
    one = Fraction(1, 1)
    sum = 0
    for _ in range(n):
        sum = Fraction(1, one + sum)
    sum = one + sum
    return sum
