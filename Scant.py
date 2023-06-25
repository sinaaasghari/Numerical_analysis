def secant_method(f, x0, x1, tol=1e-6, max_iter=100):

    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1) < tol:
            return x1
        
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        if abs(x2 - x1) < tol:
            return x2
        
        x0 = x1
        x1 = x2
    
    raise ValueError("Secant method did not hamgera.")

# Example usage:
def equation(x):
    return x**3 - 2*x - 5

solution = secant_method(equation, 2.0, 3.0)
print("Approximate solution:", solution)
print("Error:", equation(solution))
