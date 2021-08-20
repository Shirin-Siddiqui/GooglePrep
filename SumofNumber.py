def sum(n):
    assert n>=0 and int(n) == n, "Please enter a positive number greater than 0"
    if n <= 9:
        return n
    else:
        return int(n%10) + sum(int(n/10))

print(sum(-123))