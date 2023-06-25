def bisection_method(function, a, b, tolerance):
    if function(a) * function(b) >= 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    midpoint = (a + b) / 2
    iteration = 0

    while abs(function(midpoint)) > tolerance:
        if function(a) * function(midpoint) < 0:
            b = midpoint  # The root is in the left half of the interval
        else:
            a = midpoint  # The root is in the right half of the interval

        midpoint = (a + b) / 2
        iteration += 1

    return midpoint, iteration

# Define the function
def equation(x):
    return x ** 3 - 2 * x - 5

# Define the interval [a, b]
a = 2
b = 3

# Set the desired tolerance
tolerance = 0.0001

root, iterations = bisection_method(equation, a, b, tolerance)

print("Root:", root)
print("Iterations:", iterations)
