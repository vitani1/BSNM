import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 1. Define the Runge function family
def f(x, c):
    return 1 / (c * x**2 + 1)

# 2. Setup the interpolation nodes
x_nodes = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
c_values =[1, 4, 25]

# High-resolution x array to evaluate the error continuously
x_plot = np.linspace(-1.0, 1.0, 1000)

plt.figure(figsize=(10, 6))

for c in c_values:
    y_nodes = f(x_nodes, c)
    
    # Compute the natural cubic spline
    cs = CubicSpline(x_nodes, y_nodes, bc_type='natural')
    
    # Calculate absolute error at each point
    y_true = f(x_plot, c)
    y_spline = cs(x_plot)
    abs_error = np.abs(y_true - y_spline)
    
    # Report the maximum error for context
    print(f"Max absolute error for c = {c:2d}: {np.max(abs_error):.5f}")
    
    # Plot absolute error curve
    plt.plot(x_plot, abs_error, linewidth=2, label=f'Error (c={c})')

# 3. Mark the interpolation nodes (where error is mathematically zero)
plt.axhline(0, color='black', linestyle='-', alpha=0.3)
for node in x_nodes:
    plt.axvline(node, color='gray', linestyle=':', alpha=0.5)

# 4. Final plot configurations
plt.title("Absolute Error of Natural Cubic Spline $|f(x) - S(x)|$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("Absolute Error", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.show()
