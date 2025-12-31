import pandas as pd

# 1️⃣ Load the dataset
df = pd.read_csv("sales_data.csv")

# 2️⃣ Display first few rows
print("🔹 First 5 rows of dataset:")
print(df.head())

# 3️⃣ Basic information
print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Shape of dataset (rows, columns):")
print(df.shape)

# 4️⃣ Handle missing values
df.fillna(0, inplace=True)

# 5️⃣ Basic statistics
total_revenue = df["Total_Sales"].sum()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()
average_sale = df["Total_Sales"].mean()

# 6️⃣ Best-selling product (by revenue)
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# 7️⃣ Best-selling region
best_region = df.groupby("Region")["Total_Sales"].sum().idxmax()

# 8️⃣ Final Report
print("\n📊 SALES ANALYSIS REPORT")
print("-" * 30)
print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Average Sale       : ₹{average_sale:,.2f}")
print(f"Highest Sale       : ₹{highest_sale:,.2f}")
print(f"Lowest Sale        : ₹{lowest_sale:,.2f}")
print(f"Best Product       : {best_product}")
print(f"Top Performing Region : {best_region}")
