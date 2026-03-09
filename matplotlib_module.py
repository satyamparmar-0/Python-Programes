import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for saving plots to files
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# 1. Line Plot - Sales Trend Analysis
# -------------------------------

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1200, 1500, 1800, 1600, 2000, 2200,
         2100, 2400, 2300, 2600, 2800, 3000]

plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', color='blue', linewidth=2, label='Monthly Sales')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (in units)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('line_plot.png')
plt.close()
print("Line plot saved as 'line_plot.png'")

# -------------------------------
# 2. Bar Chart - Product Category Comparison
# -------------------------------

categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
revenue = [45000, 28000, 15000, 32000, 9000]

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, revenue, color=['steelblue', 'tomato', 'green', 'orange', 'purple'])
plt.title('Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Revenue (in $)')
for bar, val in zip(bars, revenue):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 500,
             f'${val:,}', ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.close()
print("Bar chart saved as 'bar_chart.png'")

# -------------------------------
# 3. Histogram - Age Distribution
# -------------------------------

np.random.seed(42)
ages = np.random.normal(loc=35, scale=10, size=200).astype(int)
ages = np.clip(ages, 18, 65)  # clip ages between 18 and 65

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=15, color='teal', edgecolor='black')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histogram.png')
plt.close()
print("Histogram saved as 'histogram.png'")

# -------------------------------
# 4. Scatter Plot - Advertising Spend vs Sales
# -------------------------------

np.random.seed(7)
ad_spend = np.random.randint(500, 5000, size=50)
sales_scatter = ad_spend * 0.8 + np.random.randint(-500, 500, size=50)

plt.figure(figsize=(8, 5))
plt.scatter(ad_spend, sales_scatter, color='darkorange', alpha=0.7, edgecolors='black')
plt.title('Advertising Spend vs Sales')
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.close()
print("Scatter plot saved as 'scatter_plot.png'")

# -------------------------------
# 5. Pie Chart - Market Share
# -------------------------------

companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Others']
market_share = [35, 25, 20, 12, 8]
explode = (0.05,) * len(companies)

plt.figure(figsize=(7, 7))
plt.pie(market_share, labels=companies, autopct='%1.1f%%',
        explode=explode, startangle=140,
        colors=['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2'])
plt.title('Market Share Distribution')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.close()
print("Pie chart saved as 'pie_chart.png'")

# -------------------------------
# 6. Subplots - Combined Dashboard
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Data Analysis Dashboard', fontsize=16, fontweight='bold')

# Subplot 1: Line plot
axes[0, 0].plot(months, sales, marker='o', color='blue', linewidth=2)
axes[0, 0].set_title('Monthly Sales Trend')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Sales (units)')
axes[0, 0].grid(True)

# Subplot 2: Bar chart
axes[0, 1].bar(categories, revenue, color=['steelblue', 'tomato', 'green', 'orange', 'purple'])
axes[0, 1].set_title('Revenue by Category')
axes[0, 1].set_xlabel('Category')
axes[0, 1].set_ylabel('Revenue ($)')
axes[0, 1].tick_params(axis='x', rotation=15)

# Subplot 3: Histogram
axes[1, 0].hist(ages, bins=15, color='teal', edgecolor='black')
axes[1, 0].set_title('Age Distribution')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Frequency')

# Subplot 4: Scatter plot
axes[1, 1].scatter(ad_spend, sales_scatter, color='darkorange', alpha=0.7, edgecolors='black')
axes[1, 1].set_title('Ad Spend vs Sales')
axes[1, 1].set_xlabel('Ad Spend ($)')
axes[1, 1].set_ylabel('Sales ($)')
axes[1, 1].grid(True)

plt.tight_layout()
plt.savefig('dashboard.png')
plt.close()
print("Dashboard saved as 'dashboard.png'")
