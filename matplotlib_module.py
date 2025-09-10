import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# 1. Basic Line Plots
# -------------------------------

# Simple line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Multiple lines on one plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='red', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='blue', linewidth=2)
plt.title('Sine and Cosine Functions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# -------------------------------
# 2. Bar Charts
# -------------------------------

# Simple bar chart
categories = ['Python', 'Java', 'JavaScript', 'C++', 'Go']
values = [85, 70, 75, 60, 55]

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
plt.title('Programming Languages Popularity')
plt.xlabel('Languages')
plt.ylabel('Popularity Score')
plt.ylim(0, 100)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}', ha='center', va='bottom')

plt.show()

# Horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
plt.title('Programming Languages Popularity (Horizontal)')
plt.xlabel('Popularity Score')
plt.ylabel('Languages')
plt.xlim(0, 100)
plt.show()

# -------------------------------
# 3. Scatter Plots
# -------------------------------

# Basic scatter plot
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6, c='purple', s=50)
plt.title('Scatter Plot Example')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True, alpha=0.3)
plt.show()

# Colored scatter plot
# Different groups with different colors
group1_x = np.random.normal(2, 1, 50)
group1_y = np.random.normal(3, 1, 50)
group2_x = np.random.normal(6, 1, 50)
group2_y = np.random.normal(7, 1, 50)

plt.figure(figsize=(8, 6))
plt.scatter(group1_x, group1_y, c='red', alpha=0.6, label='Group 1', s=60)
plt.scatter(group2_x, group2_y, c='blue', alpha=0.6, label='Group 2', s=60)
plt.title('Scatter Plot with Groups')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# -------------------------------
# 4. Histograms
# -------------------------------

# Simple histogram
np.random.seed(42)
data = np.random.normal(100, 15, 1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()

# Multiple histograms
data1 = np.random.normal(100, 15, 1000)
data2 = np.random.normal(120, 10, 1000)

plt.figure(figsize=(10, 6))
plt.hist(data1, bins=30, alpha=0.5, label='Dataset 1', color='red')
plt.hist(data2, bins=30, alpha=0.5, label='Dataset 2', color='blue')
plt.title('Overlapping Histograms')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# -------------------------------
# 5. Pie Charts
# -------------------------------

# Simple pie chart
sizes = [30, 25, 20, 15, 10]
labels = ['Python', 'Java', 'JavaScript', 'C++', 'Others']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
explode = (0.1, 0, 0, 0, 0)  # explode the first slice

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('Programming Languages Market Share')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

# -------------------------------
# 6. Subplots - Multiple Plots
# -------------------------------

# Create a 2x2 subplot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: Line plot
x = np.linspace(0, 2*np.pi, 100)
ax1.plot(x, np.sin(x), 'r-', linewidth=2)
ax1.set_title('Sine Wave')
ax1.set_xlabel('X')
ax1.set_ylabel('sin(x)')
ax1.grid(True)

# Subplot 2: Bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
ax2.bar(categories, values, color='green', alpha=0.7)
ax2.set_title('Bar Chart')
ax2.set_ylabel('Values')

# Subplot 3: Scatter plot
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
ax3.scatter(x_scatter, y_scatter, c='purple', alpha=0.6)
ax3.set_title('Scatter Plot')
ax3.set_xlabel('X values')
ax3.set_ylabel('Y values')

# Subplot 4: Histogram
data_hist = np.random.normal(0, 1, 1000)
ax4.hist(data_hist, bins=20, color='orange', alpha=0.7)
ax4.set_title('Histogram')
ax4.set_xlabel('Values')
ax4.set_ylabel('Frequency')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()

# -------------------------------
# 7. Advanced Plot Customization
# -------------------------------

# Customized plot with annotations
x = np.linspace(0, 10, 100)
y = np.exp(-x/3) * np.cos(2*x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='Damped Oscillation')

# Add annotations
plt.annotate('Peak', xy=(1.57, 0.35), xytext=(3, 0.5),
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
            fontsize=12, color='red')

plt.annotate('Zero Crossing', xy=(4.71, 0), xytext=(6, 0.2),
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
            fontsize=12, color='green')

plt.title('Damped Oscillation with Annotations', fontsize=16, fontweight='bold')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
plt.show()

# -------------------------------
# 8. Box Plot
# -------------------------------

# Create box plot data
np.random.seed(42)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(110, 5, 200)

data_to_plot = [data1, data2, data3]

plt.figure(figsize=(8, 6))
box_plot = plt.boxplot(data_to_plot, tick_labels=['Group A', 'Group B', 'Group C'],
                       patch_artist=True)

# Customize box colors
colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Box Plot Comparison')
plt.ylabel('Values')
plt.grid(True, alpha=0.3)
plt.show()

# -------------------------------
# 9. Area Plot (Fill Between)
# -------------------------------

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, 'r-', linewidth=2, label='sin(x)')
plt.plot(x, y2, 'b-', linewidth=2, label='cos(x)')
plt.fill_between(x, y1, y2, where=(y1 >= y2), alpha=0.3, color='red', label='sin(x) ≥ cos(x)')
plt.fill_between(x, y1, y2, where=(y1 < y2), alpha=0.3, color='blue', label='sin(x) < cos(x)')

plt.title('Area Plot - Fill Between Curves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# -------------------------------
# 10. 3D Plot (Surface)
# -------------------------------

from mpl_toolkits.mplot3d import Axes3D

# Create 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Make data
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax.set_title('3D Surface Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

print("All matplotlib examples have been displayed!")
print("This module demonstrates:")
print("1. Basic line plots with customization")
print("2. Bar charts (vertical and horizontal)")
print("3. Scatter plots with grouping")
print("4. Histograms (single and overlapping)")
print("5. Pie charts with exploding slices")
print("6. Subplots for multiple visualizations")
print("7. Advanced customization with annotations")
print("8. Box plots for statistical analysis")
print("9. Area plots with fill between")
print("10. 3D surface plots")