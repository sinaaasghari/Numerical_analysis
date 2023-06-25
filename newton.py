def newton_method(f, f_prime, x0, tolerance=1e-6, max_iterations=100):
    """
    Newton's method for finding the root of an equation in one variable.
    
    Parameters:
        f (function): The function for which we want to find the root.
        f_prime (function): The derivative of the function f.
        x0 (float): The initial guess for the root.
        tolerance (float): The desired accuracy of the root (default: 1e-6).
        max_iterations (int): The maximum number of iterations (default: 100).
    
    Returns:
        float: The approximate root of the equation.
    """
    x = x0
    for _ in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            return x
        fpx = f_prime(x)
        if fpx == 0:
            break
        x = x - fx / fpx
    raise ValueError("The method did not converge to a root.")

# Example usage:
def f(x):
    return x**2 - 4

def f_prime(x):
    return 2*x

root = newton_method(f, f_prime, x0=1)
print("Approximate root:", root)
