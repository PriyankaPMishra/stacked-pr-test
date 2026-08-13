def add(a, b):
    """Return the sum of a and b."""
    return a + b

def sub(a, b):
    """Return the difference of a and b."""
    return add(a, -b)

if __name__ == "__main__":
    result_add = add(3, 5)
    print(f"SUM: {result_add}")
 
    result_sub = sub(10, 4)
    print(f"DIFFERENCE: {result_sub}")
