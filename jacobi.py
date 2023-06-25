import numpy as np

def jacobi(A, b, max_iterations=100, tolerance=1e-6):
    n = len(A)
    x = np.zeros(n)  

    for iteration in range(max_iterations):
        x_new = np.zeros(n)  

        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]

            x_new[i] = (b[i] - s) / A[i][i]

        if np.linalg.norm(x_new - x) < tolerance:
            break

        x = x_new

    return x

# Example usage
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = np.array([1, 2, 3])

solution = jacobi(A, b)

print("Solution:", solution)
