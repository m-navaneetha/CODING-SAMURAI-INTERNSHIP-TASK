import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("sales_data.csv")  

# Step 2: Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Create Month-Year column
df['Month'] = df['Date'].dt.to_period('M')

# Step 4: Calculate monthly sales totals
monthly_sales = df.groupby('Month')['Quantity'].sum().reset_index()

# Identify best and worst months
best_month = monthly_sales.loc[monthly_sales['Quantity'].idxmax()]
worst_month = monthly_sales.loc[monthly_sales['Quantity'].idxmin()]

print(f"Best Month: {best_month['Month']} with {best_month['Quantity']} sales")
print(f"Worst Month: {worst_month['Month']} with {worst_month['Quantity']} sales")

# Step 5: Plot monthly sales trend with highlights
plt.figure(figsize=(12,6))
plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Quantity'], marker='o', color='green', label='Monthly Sales')
plt.scatter(best_month['Month'].strftime('%Y-%m'), best_month['Quantity'], color='gold', s=150, label='Best Month', edgecolors='black', zorder=5)
plt.scatter(worst_month['Month'].strftime('%Y-%m'), worst_month['Quantity'], color='red', s=150, label='Worst Month', edgecolors='black', zorder=5)
plt.title('Monthly Sales Trends (2025)')
plt.xlabel('Month')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Step 6: Analyze sales by region
region_sales = df.groupby('Region')['Quantity'].sum().reset_index()

# Plot regional sales
plt.figure(figsize=(8,5))
bars = plt.bar(region_sales['Region'], region_sales['Quantity'], color='skyblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Quantity Sold')

# Highlight the region with max sales
max_region = region_sales.loc[region_sales['Quantity'].idxmax()]
for bar in bars:
    if bar.get_height() == max_region['Quantity']:
        bar.set_color('gold')
plt.tight_layout()
plt.show()
