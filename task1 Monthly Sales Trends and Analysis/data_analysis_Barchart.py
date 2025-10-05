import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Calculate sales by region
region_sales = df.groupby('Region')['Quantity'].sum().reset_index()

# Plot bar chart
plt.figure(figsize=(8,5))
bars = plt.bar(region_sales['Region'], region_sales['Quantity'], color='skyblue')

# Highlight the region with the highest sales
max_region = region_sales.loc[region_sales['Quantity'].idxmax()]
for bar in bars:
    if bar.get_height() == max_region['Quantity']:
        bar.set_color('gold')

# Add labels and title
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Quantity Sold')
plt.tight_layout()
plt.show()
