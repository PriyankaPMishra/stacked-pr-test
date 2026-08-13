def add(a, b, c=0):
    """Return the sum of a, b, and c."""
    #add func modified
    #add third arg
    print(f"Adding {a}, {b}, and {c}")
    return a + b + c

def sub(a, b):
    """Return the difference of a and b."""
    return add(a, -b)

def mul(a, b):
    """Return the product of a and b."""
    return a * b

if __name__ == "__main__":
    result_add = add(3, 5)
    print(f"SUM: {result_add}")
 
    result_sub = sub(10, 4)
    print(f"DIFFERENCE: {result_sub}")

    result_mul = mul(6, 7)
    print(f"PRODUCT: {result_mul}")
