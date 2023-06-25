def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(A)
    x = x0.copy()
    iter_count = 0
    error = tol + 1
    
    while error > tol and iter_count < max_iter:
        x_new = x.copy()
        for i in range(n):
            sum_1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum_2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_1 - sum_2) / A[i][i]
        
        error = max(abs(x_new[i] - x[i]) for i in range(n))
        x = x_new
        iter_count += 1
    
    if iter_count == max_iter:
        print("Maximum iterations reached without convergence.")
    
    return x

# Example system of equations:
# x + 2y + z = 8
# 3x + y - z = 2
# 2x + 3y + z = 11

A = [[1, 2, 1],
     [3, 1, -1],
     [2, 3, 1]]
b = [8, 2, 11]
x0 = [0, 0, 0]

solution = gauss_seidel(A, b, x0, tol=1e-8, max_iter=100)
print("Solution:", solution)
