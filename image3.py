import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrow

# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# --- Temperature vs Time curve ---
time = [0, 2, 4, 6, 8, 10, 12]
temp = [115, 115, 117, 117, 120, 125, 125]
ax.plot(time, temp, color='blue', lw=2, label='Temperature (°C)')

# --- α-Sulfur S8 rings (yellow circles) ---
for x in [1, 1.5, 2]:
    circle = Circle((x, 115), 0.2, color='gold', zorder=5)
    ax.add_patch(circle)
ax.text(2, 114.2, 'α-Sulfur (S8 rings)', fontsize=10, ha='center')

# --- β-Sulfur orthorhombic (orange rectangles) ---
for x in [5, 5.5, 6]:
    rect = Rectangle((x, 117), 0.4, 0.8, color='orange', zorder=5)
    ax.add_patch(rect)
ax.text(5.5, 116.2, 'β-Sulfur (orthorhombic)', fontsize=10, ha='center')

# --- Liquid sulfur (red polygon) ---
polygon = Polygon([[10, 125], [10.5, 126], [11, 125]], color='red', zorder=5)
ax.add_patch(polygon)
ax.text(10.5, 124.2, 'Liquid Sulfur', fontsize=10, ha='center')

# --- Arrows showing transitions ---
arrow1 = FancyArrow(2.2, 115, 2.2, 117-115, width=0.05, color='black', length_includes_head=True)
ax.add_patch(arrow1)
arrow2 = FancyArrow(6.5, 117, 3.5, 125-117, width=0.05, color='black', length_includes_head=True)
ax.add_patch(arrow2)

# --- Labels and axes ---
ax.set_xlabel('Time (min)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Sulfur Solid Phase Change')
ax.set_xlim(0,12)
ax.set_ylim(110,130)
ax.legend()

plt.show()
