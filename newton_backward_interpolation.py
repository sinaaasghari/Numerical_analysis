def newton_backward_interpolation(x, y, x_target):
    n = len(x) - 1
    h = x[1] - x[0]
    
    # Calculating the backward difference table
    backward_diff_table = [[0 for _ in range(n+1)] for _ in range(n+1)]
    backward_diff_table[0] = y
    
    for j in range(1, n+1):
        for i in range(n, j-1, -1):
            backward_diff_table[j][i] = backward_diff_table[j-1][i] - backward_diff_table[j-1][i-1]
    
    # Calculating the interpolation
    result = y[-1]
    u = (x_target - x[-1]) / h
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i
        result += (backward_diff_table[i][n] * u**i) / factorial
        u *= (u + i)
    
    return result

# Example usage
x = [1, 1.3, 1.6, 1.9, 2.2]
y = [0.7651977, 0.6200860, 0.4554022,0.2818186, 0.1103623]
x_target = 2

interpolated_value = newton_backward_interpolation(x, y, x_target)
print("Interpolated value at x = {}: {}".format(x_target, interpolated_value))
