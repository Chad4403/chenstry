import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 4))
plt.title("Sulfur Phase Changes with Structure Sketches", fontsize=16)

# Draw monoclinic layered zig-zags
def draw_zigzag(x_offset, y_offset, n=4):
    for i in range(n):
        xs = [x_offset, x_offset + 0.03, x_offset, x_offset - 0.0]
        ys = [y_offset + i*0.04, y_offset + 0.02 + i*0.04, y_offset + 0.04 + i*0.04, y_offset + 0.02 + i*0.04]
        ax.plot(xs, ys, linewidth=2)

draw_zigzag(0.08, 0.25)
ax.text(0.08, 0.1, "Monoclinic\n(S₈ rings stacked)", ha='center')

# Orthorhombic zigzag stacked flatter
def draw_orthorhombic(x_offset, y_offset, n=4):
    for i in range(n):
        xs = [x_offset, x_offset + 0.03, x_offset, x_offset - 0.03]
        ys = [y_offset + i*0.035]*4
        ax.plot(xs, ys, linewidth=2)

draw_orthorhombic(0.32, 0.25)
ax.text(0.32, 0.1, "Orthorhombic\n(stable solid)", ha='center')

# S8 ring (octagon-ish)
ring_x = [0.55, 0.57, 0.60, 0.58, 0.55, 0.52, 0.50, 0.52, 0.55]
ring_y = [0.30, 0.33, 0.30, 0.26, 0.24, 0.26, 0.30, 0.33, 0.30]
ax.plot(ring_x, ring_y, linewidth=2)
ax.text(0.55, 0.1, "Liquid sulfur\n(S₈ rings)", ha='center')

# Long polymer chain
poly_x = [0.78, 0.80, 0.83, 0.85, 0.84, 0.82, 0.81, 0.83, 0.86]
poly_y = [0.20, 0.25, 0.23, 0.27, 0.32, 0.34, 0.39, 0.42, 0.45]
ax.plot(poly_x, poly_y, linewidth=2)
ax.text(0.78, 0.1, "Hot polymer\n(long S chains)", ha='center')

# Amorphous sulfur scribble
amorph_x = [1.02, 1.04, 1.03, 1.05, 1.07, 1.06, 1.04, 1.03, 1.02]
amorph_y = [0.15, 0.18, 0.21, 0.26, 0.32, 0.36, 0.40, 0.45, 0.50]
ax.plot(amorph_x, amorph_y, linewidth=2)
ax.text(1.02, 0.07, "Amorphous\nrubbery sulfur", ha='center')

# arrows and labels
def arrow(x1, x2, y=0.42):
    ax.annotate("", xy=(x2, y), xytext=(x1, y), arrowprops=dict(arrowstyle="->", linewidth=2))
arrow(0.13, 0.27)
arrow(0.37, 0.50)
arrow(0.63, 0.75)
arrow(0.88, 1.00)

ax.text(0.50, 0.55, "Heat ↑ ring breaks → polymer chains", ha='center')
ax.text(0.50, -0.05, "Cooling → crystalline or amorphous", ha='center')

ax.axis('off')
plt.show()
