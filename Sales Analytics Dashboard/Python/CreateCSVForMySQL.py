import pandas as pd

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

df.columns = [
    'row_id',
    'order_id',
    'order_date',
    'ship_date',
    'ship_mode',
    'customer_id',
    'customer_name',
    'segment',
    'country',
    'city',
    'state',
    'postal_code',
    'region',
    'product_id',
    'category',
    'sub_category',
    'product_name',
    'sales',
    'quantity',
    'discount',
    'profit'
]

df.to_csv("../data/mysql_superstore.csv", index=False)

print("Done!")