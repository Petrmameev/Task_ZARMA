import pandas as pd

products_df = pd.read_csv("products.csv")
sales_df = pd.read_json("sales.json")

merge_df = pd.merge(products_df, sales_df, on='product_id', how='left')

print(merge_df)