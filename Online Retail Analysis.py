
#Step 1: Importing the necessary libraries and reading the Excel file
import pandas as pd
df = pd.read_excel(r"C:\Users\ferna\PROJECTS\Online Retail Analysis\Online Retail.xlsx", sheet_name="Online Retail")

print(df.head())
print(df.shape)
print(df.columns)

# %%
#Step2: Data Cleaning

df.dropna(subset=["CustomerID", "InvoiceNo", "Description"], inplace=True)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df = df[df["Quantity"] > 0]  

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# %%
# Step3: Exploratory Data Analysis (EDA)
top_products = df.groupby("Description")["TotalPrice"].sum().sort_values(ascending=False).head(10)
print(top_products)

# %%
revenue_by_country = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False)
print(revenue_by_country.head(10))

# %%
import matplotlib.pyplot as plt

df.set_index("InvoiceDate")["TotalPrice"].resample("W").sum().plot(figsize=(12, 4))
plt.title("Weekly Sales Over Time")
plt.ylabel("Revenue")
plt.xlabel("Date")
plt.show()

# %%
top_customers = df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False).head(10)
print(top_customers)

# %%
returns = df[df["Quantity"] < 0]
print(returns.head())


