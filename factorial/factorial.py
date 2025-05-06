def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f'El resultado de factorial 5 es: ' + str(factorial(5)))