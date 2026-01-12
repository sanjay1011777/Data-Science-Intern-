import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. LOAD DATA
# ==============================
customers_df = pd.read_csv(r"c:\Users\sanja\Downloads\customer_churn.csv")
sales_df = pd.read_csv(r"c:\Users\sanja\Downloads\sales_data.csv")

print("Files loaded successfully")

# ==============================
# 2. CLEAN COLUMN NAMES
# ==============================
customers_df.columns = customers_df.columns.str.strip()
sales_df.columns = sales_df.columns.str.strip()

# Rename for consistency
sales_df.rename(columns={"Customer_ID": "CustomerID"}, inplace=True)

# ==============================
# 3. FIX CUSTOMER ID FORMAT (CRITICAL FIX)
# ==============================
# Convert CUST001 -> C00001
sales_df["CustomerID"] = (
    sales_df["CustomerID"]
    .str.replace("CUST", "", regex=False)
    .astype(int)
    .astype(str)
    .str.zfill(5)
)

sales_df["CustomerID"] = "C" + sales_df["CustomerID"]

# ==============================
# 4. DATE HANDLING
# ==============================
sales_df["Date"] = pd.to_datetime(sales_df["Date"], errors="coerce")
sales_df.dropna(subset=["Date"], inplace=True)

sales_df["Month"] = sales_df["Date"].dt.month

# ==============================
# 5. MERGE DATASETS
# ==============================
merged_df = pd.merge(
    sales_df,
    customers_df,
    on="CustomerID",
    how="inner"
)

print("Rows after merge:", len(merged_df))

# ==============================
# 6. BASIC METRICS
# ==============================
total_revenue = merged_df["Total_Sales"].sum()
total_customers = merged_df["CustomerID"].nunique()
avg_order_value = merged_df["Total_Sales"].mean()

print("Total Revenue:", total_revenue)
print("Total Customers:", total_customers)
print("Average Order Value:", avg_order_value)

# ==============================
# 7. AGGREGATIONS
# ==============================
monthly_sales = merged_df.groupby("Month")["Total_Sales"].sum()
region_sales = merged_df.groupby("Region")["Total_Sales"].sum()

# ==============================
# 8. PIVOT TABLE
# ==============================
pivot_table = pd.pivot_table(
    merged_df,
    values="Total_Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)
# ------------------------------ 
# TOP CUSTOMERS BY TOTAL SALES 
# ------------------------------ 
 
top_n = 10 # change this if you want more 
 
top_customers = ( 
    merged_df 
    .groupby("CustomerID")["Total_Sales"] 
    .sum() 
    .sort_values(ascending=False) 
    .head(top_n) 
) 
 
print(f"\nTop {top_n} Customers by Total Sales:\n") 
print(top_customers)
# ==============================
# 9. VISUALIZATIONS
# ==============================
plt.figure()
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

plt.figure()
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.show()

plt.figure()
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="coolwarm")
plt.title("Sales Heatmap")
plt.show()

print("Analysis completed successfully ✅")
