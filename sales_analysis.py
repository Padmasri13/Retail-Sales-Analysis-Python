
# RETAIL SALES DATA ANALYSIS
# Python Portfolio Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

# 1. CREATE SAMPLE DATASET
np.random.seed(42)

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor"]

prices = {
    "Laptop": 65000,
    "Mobile": 30000,
    "Headphones": 2500,
    "Keyboard": 1800,
    "Monitor": 12000
}

df = pd.DataFrame({
    "Order_ID": range(1001, 1301),
    "Date": pd.date_range("2025-01-01", periods=300, freq="D"),
    "Product": np.random.choice(products, 300),
    "Region": np.random.choice(
        ["North", "South", "East", "West"], 300
    ),
    "Quantity": np.random.randint(1, 5, 300)
})

df["Unit_Price"] = df["Product"].map(prices)
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# 2. DATA CLEANING
df.drop_duplicates(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])

print("\nDATASET OVERVIEW")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# 3. KEY PERFORMANCE INDICATORS
total_revenue = df["Revenue"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_revenue / total_orders

print("\nSALES SUMMARY")
print("Total Revenue: Rs.", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Total Units Sold:", total_quantity)
print("Average Order Value:", round(average_order_value, 2))

# 4. PRODUCT ANALYSIS
product_sales = df.groupby("Product")["Revenue"].sum().sort_values(
    ascending=False
)

print("\nPRODUCT SALES")
print(product_sales)

# 5. REGIONAL ANALYSIS
region_sales = df.groupby("Region")["Revenue"].sum().sort_values(
    ascending=False
)

print("\nREGIONAL SALES")
print(region_sales)

# 6. MONTHLY SALES ANALYSIS
df["Month"] = df["Date"].dt.month_name()

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()
)

print("\nMONTHLY SALES")
print(monthly_sales)

# 7. VISUALIZATION - PRODUCT SALES
sns.set_theme(style="whitegrid")

plt.figure(figsize=(9, 5))
product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("outputs/product_sales.png")


# 8. VISUALIZATION - REGIONAL SALES
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar", color="purple")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("outputs/regional_sales.png")


# 9. VISUALIZATION - MONTHLY SALES
plt.figure(figsize=(11, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")


# 10. BUSINESS INSIGHTS
print("\nBUSINESS INSIGHTS")

print("Best Selling Product:", product_sales.idxmax())
print("Top Performing Region:", region_sales.idxmax())
print("Highest Revenue Month:", monthly_sales.idxmax())

print("\nPROJECT COMPLETED SUCCESSFULLY!")

# 11. EXPORT DATA
df.to_csv("outputs/retail_sales_cleaned.csv", index=False)

print("Cleaned dataset exported successfully!")
plt.close("all")