
def power(n,e):
    if e == 1:
        return n
    else:
        return n * power(n,e-1)

print(power(2,4))