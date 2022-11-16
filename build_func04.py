def main(n):
    """
    Given a argument called 'n' type of int , calculate the value of expression and return result:
    Args:
        n: int
    Returns:
        result : float
    """
    a = (2+n)/3
    b = pow(a, 2)
    return b
print(main(4))
