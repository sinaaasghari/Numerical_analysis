def trapezoidal_rule(x, f):
    n = len(x)
    h = x[1] - x[0]
    result = 0.5 * h * (f[0] + f[n-1])  

    for i in range(1, n - 1):
        result += 0.5 * h * 2 * f[i]  

    return result

# Example usage
x = [0, 0.2, 0.4, 0.8 , 1]  # x values
f = [1.2214,1.4818,1.8221,2.2255,2.7183]  # f(x) values
differentiation_result = trapezoidal_rule(x, f)

print("Numerical differentiation using the trapezoidal rule:", differentiation_result)
