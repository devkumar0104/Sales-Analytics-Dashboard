import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/mysql_superstore.csv")

# Sales by Category
category_sales = df.groupby("category")["sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../screenshots/sales_by_category.png")
plt.close()

# Sales by Region
region_sales = df.groupby("region")["sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../screenshots/sales_by_region.png")
plt.close()

# Profit by Region
region_profit = df.groupby("region")["profit"].sum()

plt.figure(figsize=(8,5))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("../screenshots/profit_by_region.png")
plt.close()

print("Charts created successfully!")