import pandas as pd

customers = pd.read_csv(r"C:\Users\divya\Downloads\156c0733-d225-4b76-a984-3ed5e19eb16d_83d04ac6-cb74-4a96-a06a-e0d5442aa126_customers.csv")

orders = pd.read_csv(r"C:\Users\divya\Downloads\419f8355-6271-44cc-a20b-fea8bd241428_83d04ac6-cb74-4a96-a06a-e0d5442aa126_orders.csv") 

transactions = pd.read_csv(r"C:\Users\divya\Downloads\422ceab9-b775-4f4a-8a04-066006bf204b_83d04ac6-cb74-4a96-a06a-e0d5442aa126_transactions.csv")

print(customers.head(2))
print(orders.head(2))
print(transactions.head(2))

print(customers.columns)