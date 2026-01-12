import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales_df = pd.read_csv("sales_data.csv")
customers_df = pd.read_csv("customer_churn.csv")

sales_df.head(), customers_df.head()

sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])
sales_df.dropna(inplace=True)
customers_df.dropna(inplace=True)

sales_df['revenue'] = sales_df['price'] * sales_df['quantity']
sales_df['month'] = sales_df['order_date'].dt.month

merged_df = pd.merge(
    sales_df,
    customers_df,
    on="customer_id",
    how="inner"
)

merged_df.head()

# Top customers
top_customers = merged_df.groupby('customer_name')['revenue'].sum().sort_values(ascending=False)
top_customers.head()

# Monthly sales
monthly_sales = merged_df.groupby('month')['revenue'].sum()
monthly_sales

high_value_orders = merged_df[
    (merged_df['revenue'] > 500) &
    (merged_df['region'] == 'South')
]

merged_df['customer_name'] = merged_df['customer_name'].str.title()

pivot_table = pd.pivot_table(
    merged_df,
    values='revenue',
    index='region',
    columns='category',
    aggfunc='sum'
)

pivot_table

# Line chart
monthly_sales.plot(kind='line', marker='o', title="Monthly Sales Trend")
plt.show()

# Bar chart
merged_df.groupby('region')['revenue'].sum().plot(kind='bar', title="Revenue by Region")
plt.show()

# Pie chart
merged_df.groupby('category')['revenue'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.show()

# Heatmap
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="coolwarm")
plt.title("Revenue Heatmap")
plt.show()

assert merged_df.isnull().sum().sum() == 0
assert merged_df['revenue'].sum() > 0
