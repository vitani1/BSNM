import numpy as np
import matplotlib.pyplot as plt

# 1. Define functions
def original_f(x):
    return x**3 - 2*x**2 + 6*x - 1

def lagrange_P(x):
    return (-37/7500)*x**4 + (247/250)*x**3 - (431/300)*x**2 + (73/10)*x - 1

# 2. Points of evaluation and their exact absolute errors
x_points = np.array([-10, -5, 0, 5, 10])
error_at_points = np.abs(original_f(x_points) - lagrange_P(x_points))

# 3. Continuous domain for smooth error curve
x_plot = np.linspace(-12, 12, 500)
absolute_error = np.abs(original_f(x_plot) - lagrange_P(x_plot))

# 4. Generate the error plot
plt.figure(figsize=(10, 5))
plt.plot(x_plot, absolute_error, color="purple", lw=2, label="Absolute Error: $|f(x) - P(x)|$")
plt.scatter(x_points, error_at_points, color="black", zorder=5)

# Label error points explicitly
for x, err in zip(x_points, error_at_points):
    plt.annotate(f"Error: {err:.1f}", (x, err), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Formatting layout
plt.title("Absolute Error Graph Between $f(x)$ and Lagrange $P(x)$", fontsize=14, fontweight='bold')
plt.xlabel("X Axis")
plt.ylabel("Absolute Error Magnitude")
plt.xlim(-12, 12)
plt.ylim(0, max(absolute_error) + 5)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right")

plt.show()
