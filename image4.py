import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 4))
plt.title("Sulfur Phase Transitions and Structural Forms", fontsize=16, pad=20)

# --- Helper drawing functions ---
def draw_zigzag(x, y, layers=4, spacing=0.04, width=0.03, label=None):
    """Draw zigzag pattern for crystalline sulfur structures."""
    for i in range(layers):
        xs = [x - width, x, x + width, x]
        ys = [y + i * spacing, y + spacing/2 + i * spacing,
              y + i * spacing, y - spacing/2 + i * spacing]
        ax.plot(xs, ys, color='darkgoldenrod', linewidth=2)
    if label:
        ax.text(x, y - 0.08, label, ha='center', va='top', fontsize=11)

def draw_ring(x, y, r=0.04, n=8, label=None):
    """Draw S8 ring-like polygon."""
    angles = np.linspace(0, 2 * np.pi, n+1)
    ax.plot(x + r * np.cos(angles), y + r * np.sin(angles),
            color='goldenrod', linewidth=2)
    if label:
        ax.text(x, y - 0.08, label, ha='center', va='top', fontsize=11)

def draw_chain(x, y, segments=8, label=None):
    """Draw polymer chain (wavy line)."""
    xs = np.linspace(x, x + 0.15, segments)
    ys = y + 0.03 * np.sin(10 * xs)
    ax.plot(xs, ys, color='goldenrod', linewidth=2)
    if label:
        ax.text(x + 0.07, y - 0.08, label, ha='center', va='top', fontsize=11)

def draw_scribble(x, y, label=None):
    """Draw amorphous sulfur (irregular curve)."""
    np.random.seed(2)
    xs = x + 0.1 * np.random.rand(12)
    ys = y + np.cumsum(np.random.randn(12)) * 0.005 + 0.02
    ax.plot(xs, ys, color='goldenrod', linewidth=2)
    if label:
        ax.text(x + 0.05, y - 0.08, label, ha='center', va='top', fontsize=11)

# --- Draw structures in order ---
draw_zigzag(0.1, 0.25, label="Monoclinic\n(S₈ stacked)")
draw_zigzag(0.35, 0.25, layers=3, spacing=0.03, label="Orthorhombic\n(stable solid)")
draw_ring(0.55, 0.28, label="Liquid sulfur\n(S₈ rings)")
draw_chain(0.78, 0.25, label="Hot polymer\n(long S chains)")
draw_scribble(1.02, 0.25, label="Amorphous\nrubbery sulfur")

# --- Arrows and text flow ---
def arrow(x1, x2, y=0.42):
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="->", color='black', linewidth=2))

arrow(0.17, 0.30)
arrow(0.42, 0.50)
arrow(0.63, 0.75)
arrow(0.90, 1.00)

# Transition text
ax.text(0.55, 0.55, "Heating ↑  →  Rings open → Long chains", ha='center', fontsize=12)
ax.text(0.55, 0.02, "Cooling ↓  →  Crystalline (monoclinic/orthorhombic) or amorphous",
        ha='center', fontsize=12)

# Aesthetic tweaks
ax.axis('off')
ax.set_xlim(0, 1.15)
ax.set_ylim(-0.1, 0.6)

plt.tight_layout()
plt.show()
