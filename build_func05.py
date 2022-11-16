def main(n,x):
    """
    Given a argument called 'n' and 'x' type of int , calculate the value of expression and return result:
    Args:
        n: int
        x: int
    Returns:
        result : int
    """
    a = pow(x, n)
    b = pow(n, x)
    c = a+b
    return c
print(main(3,6))
