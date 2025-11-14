import matplotlib.pyplot as plt

# X = heat input, Y = temperature
x = [0, 1, 2, 3, 4, 5]
y = [ -10, 0, 0, 20, 40, 60]  # melting plateau between x=1 and x=2

plt.figure(figsize=(7,5))

# Plot
plt.plot(x, y, linewidth=3)

# Style (textbook colors)
plt.style.use("default")
plt.rcParams["font.family"] = "serif"

# Labels & title
plt.title("Heating Curve of a Solid", fontsize=14)
plt.xlabel("Heat Added →", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)

# Phase labels
plt.text(0.3, -8, "Solid", fontsize=12)
plt.text(1.2, 2, "Melting\n(Solid → Liquid)", fontsize=12)
plt.text(3.1, 25, "Liquid", fontsize=12)

# Dotted phase change guides
plt.axvline(1, linestyle="--", linewidth=1)
plt.axvline(2, linestyle="--", linewidth=1)

# Arrows for heat of fusion
plt.annotate("Heat of Fusion",
             xy=(1.5, 0), xytext=(1.5, -15),
             arrowprops=dict(arrowstyle="->", linewidth=1),
             fontsize=11)

# Grid (light textbook style)
plt.grid(alpha=0.2)

plt.tight_layout()
plt.show()
