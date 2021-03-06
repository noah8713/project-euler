""" Euler archive problem 1:
    If we list all the natural numbers below 10 that are multiples of 3 or
    5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
"""
def find_multiples_of_3_and_5():
    sum=reduce(lambda x, y: x+y,filter(lambda x: (x %5 ==0 or x %3 ==0), list(range(1000))))
    return sum


print find_multiples_of_3_and_5()

