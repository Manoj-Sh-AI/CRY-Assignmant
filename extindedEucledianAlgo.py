def gcdExtended(a, b, x, y):
    # Base Case
    if a == 0:
        x = 0
        y = 1
        return b

    gcd = gcdExtended(b % a, a, x, y)

    x, y = y - (b // a) * x, x

    return gcd

x = 0
y = 0
a = 35
b = 15
g = gcdExtended(a, b, x, y)
print(f"gcd({a}, {b}) = {g}")