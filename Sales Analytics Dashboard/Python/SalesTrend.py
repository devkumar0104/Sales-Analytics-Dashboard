import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/mysql_superstore.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["sales"]
      .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("../screenshots/monthly_sales_trend.png")
plt.show()

print("Monthly trend chart created!")