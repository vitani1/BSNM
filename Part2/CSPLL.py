import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 1. Define the Runge function family
def f(x, c):
    return 1 / (c * x**2 + 1)

# 2. Setup the interpolation nodes
x_nodes = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
c_values = [1, 4, 25]

# Setup high-resolution x array for true function plotting
x_plot = np.linspace(-1.0, 1.0, 400)

plt.figure(figsize=(10, 6))

print("=== SHIFTED FORM CUBIC SPLINE EQUATIONS ===\n")

for c in c_values:
    y_nodes = f(x_nodes, c)
    
    # Compute the natural cubic spline
    # 'natural' sets the second derivatives at boundaries to 0
    cs = CubicSpline(x_nodes, y_nodes, bc_type='natural')
    
    print(f"--- Case c = {c} ---")
    # cs.c holds coefficients in the order: [d, c, b, a] for each interval
    # Equation for interval i: d_i*(x - x_i)^3 + c_i*(x - x_i)^2 + b_i*(x - x_i) + a_i
    for i in range(len(x_nodes) - 1):
        d = cs.c[0, i]
        c_coeff = cs.c[1, i]
        b = cs.c[2, i]
        a = cs.c[3, i]
        
        # Format the signs cleanly for printing
        sign = "+" if x_nodes[i] <= 0 else "-"
        x_term = f"(x {sign} {abs(x_nodes[i])})" if x_nodes[i] != 0 else "x"
        
        print(f"  Interval [{x_nodes[i]}, {x_nodes[i+1]}]:")
        print(f"    S_{i}(x) = {a:.4f} + {b:+.4f}*{x_term} + {c_coeff:+.4f}*{x_term}^2 + {d:+.4f}*{x_term}^3")
    print()

    # 3. Add curves to the plot
    plt.plot(x_plot, f(x_plot, c), linestyle='--', alpha=0.4, label=f'True Function (c={c})')
    plt.plot(x_plot, cs(x_plot), linestyle='-', linewidth=2, label=f'Spline Fit (c={c})')
    plt.scatter(x_nodes, y_nodes, s=40, zorder=5)

# 4. Final plot configurations
plt.title("Natural Cubic Spline Interpolation of $1/(cx^2+1)$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
#plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.show()
