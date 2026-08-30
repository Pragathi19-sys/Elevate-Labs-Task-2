import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Basic Cleaning
df.drop_duplicates(inplace=True)
print(df.info())
print(df.isnull().sum())

# 1. Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum)
plt.title('Total Sales by Region')
plt.savefig('sales_by_region.png')
plt.show()

# 2. Profit by Category
plt.figure(figsize=(8,5))
sns.barplot(x='Category', y='Profit', data=df, estimator=sum)
plt.title('Total Profit by Category')
plt.savefig('profit_by_category.png')
plt.show()

# 3. Monthly Sales Trend
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot()
plt.title('Monthly Sales Trend')
plt.savefig('monthly_trend.png')
plt.show()

print("Visualizations Created Successfully!")
