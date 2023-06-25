import numpy as np

def runge_kutta4(f, t0, y0, h, num_steps):
    t = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)
    t[0] = t0
    y[0] = y0

    for i in range(num_steps):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h/2, y[i] + k2/2)
        k4 = h * f(t[i] + h, y[i] + k3)
        t[i+1] = t[i] + h
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return t, y

# Example usage
def f(t, y):
    return t * y  # Example : dy/dt = t * y

t0 = 0.0  
y0 = 1.0  
h = 0.1  
num_steps = 10  

t, y = runge_kutta4(f, t0, y0, h, num_steps)


for i in range(num_steps + 1):
    print(f"t = {t[i]:.2f}, y = {y[i]:.6f}")
