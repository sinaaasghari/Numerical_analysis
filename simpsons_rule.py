def simpsons_rule(x, f):
    n = len(x) - 1
    h = (x[-1] - x[0]) / n
    
    sum_odd = 0
    sum_even = 0
    
    for i in range(1, n, 2):
        sum_odd += f[i]
    
    for i in range(2, n, 2):
        sum_even += f[i]
    
    integral = h / 3 * (f[0] + 4 * sum_odd + 2 * sum_even + f[n])
    
    return integral

x = [0, 0.5, 1.0, 1.5, 2.0]
f = [0, 0.19, 0.26, 0.29, 0.31]

result = simpsons_rule(x, f)
print(result)
