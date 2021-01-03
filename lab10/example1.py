def basic_multiplication(n,total = 0):
    if n == 1:
        return print(total + 3)
    else:
        return basic_multiplication(n - 1,total + 3)
(basic_multiplication(30))