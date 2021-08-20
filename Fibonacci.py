n = 6

def fibonacci(n):
    if n in [1,0]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))