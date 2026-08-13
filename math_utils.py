def add(a, b, c=0):
    """Return the sum of a, b, and c."""
    #add func modified
    #add third arg
    print(f"Adding {a}, {b}, and {c}")
    return a + b + c

def sub(a, b):
    """Return the difference of a and b."""
    return a - b

if __name__ == "__main__":
    result_add = add(3, 5)
    print(f"SUM: {result}")
 
    result_sub = sub(10, 4)
    print(f"DIFFERENCE: {result_sub}")
