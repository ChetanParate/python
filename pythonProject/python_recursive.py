def factorial_interative(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3......1
    """
    fact = 1
    for i in range (n):
        fact = fact * (i+1)
    return fact

def factorial_recursive(n):
    """
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return n* factorial_recursive(n-1)

num = int(input("Enter the number :"))
print("Factorial Using Iterative Method", factorial_interative(num))
print("Factorial Using Iterative Method", factorial_recursive(num))