def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fib_sequence = [0,1]
        a,b = 0,1
        for _ in range(2,n):
            next_fib = a + b
            fib_sequence.append(next_fib)
            a,b = b, next_fib
        return fib_sequence

n = 11
fib_sequence = fibonacci(n)
print("Fibo sequence for: " + str(n) + " -> " + str(fib_sequence))