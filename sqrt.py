import math

def sqrt(float_num, precision=0.0001):
    if float_num < 0:
        return None  # Return None for negative numbers to handle error.
    low, high = 0, float_num
    mid = (low + high) / 2

    while abs(mid * mid - float_num) > precision:
        if mid * mid < float_num:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2

    # Return the result rounded to the calculated number of decimal places
    decimal_places = abs(int(math.log10(precision)))
    return round(mid, decimal_places)

# Test the function
print(sqrt(10))
print(sqrt(10, 0.000001))
print(sqrt(5))
print(sqrt(6.7))