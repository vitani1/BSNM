import numpy as np
import matplotlib.pyplot as plt

# 1. Define the original cubic function
def original_f(x):
    return x**3 - 2*x**2 + 6*x - 1

# 2. Define the Lagrange polynomial derived from your points
def lagrange_P(x):
    return (-37/7500)*x**4 + (247/250)*x**3 - (431/300)*x**2 + (73/10)*x - 1

# 3. Your specific initial data points
x_points = np.array([-10, -5, 0, 5, 10])
y_points = np.array([-1255, -200, -1, 120, 867])

# 4. Generate smooth x-values for continuous plotting
x_plot = np.linspace(-12, 12, 500)

# 5. Create the plot
plt.figure(figsize=(10, 6))

# Plot lines
plt.plot(x_plot, original_f(x_plot), label="Original Function: $f(x) = x^3-2x^2+6x-1$", color="blue", alpha=0.7)
plt.plot(x_plot, lagrange_P(x_plot), label="Lagrange Polynomial: $P(x)$", color="crimson", linestyle="--", lw=2)

# Plot the specific points
plt.scatter(x_points, y_points, color="black", zorder=5, label="Given Data Points")

# Annotate each coordinate point on the chart
for (x, y) in zip(x_points, y_points):
    plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Formatting chart layout
plt.title("Lagrange Interpolating Polynomial vs. Original Cubic Function", fontsize=14, fontweight='bold')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")

# Show the chart
plt.show()
