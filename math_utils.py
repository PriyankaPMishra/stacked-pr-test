def add(a, b, c=0):
    """Return the sum of a, b, and c."""
    #add func modified
    #add third arg
    print(f"Adding {a}, {b}, and {c}")
    return a + b + c

if __name__ == "__main__":
    result = add(3, 5)
    print(f"SUM: {result}")