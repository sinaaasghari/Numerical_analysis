def euler_method(f, x0, y0, h, n):

    x = [x0]  # List to store x-values
    y = [y0]  # List to store y-values

    for i in range(n):
        x.append(x[i] + h) 
        y.append(y[i] + h * f(x[i], y[i]))

    return x, y


def f(x, y):
    return x + y  # Example differential equation: dy/dx = x + y


x0 = 0 
y0 = 1 
h = 0.1 
n = 10 

x_values, y_values = euler_method(f, x0, y0, h, n)

for i in range(n+1):
    print("x = {:.1f}, y = {:.6f}".format(x_values[i], y_values[i]))
