def NabeJayie(function, a, b, tolerance):

    if function(a) * function(b) >= 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")
    
    while (b - a) >= tolerance:
        c = (a * function(b) - b * function(a)) / (function(b) - function(a))

        if function(c) == 0.0:
            return c
        elif function(c) * function(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

def f(x):
    return x**2 + x - 4


root = NabeJayie(f, 1, 3, 0.0001)
print("Approximate root:", root)