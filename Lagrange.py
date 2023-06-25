def lagrange_interpolation(x_values, y_values, x):

    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

x_values = [-1, 0 , 1]
y_values = [1, 1 , 3]
#The output polynomial answer is equal to x^2 + x + 1
# Estimate the value at x = 3
x = 2
estimated_value = lagrange_interpolation(x_values, y_values, x)

print(f"The estimated value at x = {x} is {estimated_value}")