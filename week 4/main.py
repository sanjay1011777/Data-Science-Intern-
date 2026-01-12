import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# 1. Load Dataset (Error Handling)
# -----------------------------
DATA_PATH = "data/weatherHistory.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("weatherHistory.csv not found in data/ folder")

df = pd.read_csv(DATA_PATH)
print("Dataset loaded successfully")

# -----------------------------
# 2. Data Cleaning
# -----------------------------
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df.columns = df.columns.str.lower().str.replace(" ", "_")

df.dropna(inplace=True)

df['month'] = df['formatted_date'].dt.month
df['year'] = df['formatted_date'].dt.year

# -----------------------------
# 3. Basic Analysis
# -----------------------------
avg_temp = df['temperature_(c)'].mean()
max_temp = df['temperature_(c)'].max()
min_temp = df['temperature_(c)'].min()

print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Max Temperature: {max_temp:.2f} °C")
print(f"Min Temperature: {min_temp:.2f} °C")

# -----------------------------
# 4. Monthly Average Temperature
# -----------------------------
monthly_avg_temp = df.groupby('month')['temperature_(c)'].mean()

# -----------------------------
# 5. Visualization 1: Line Chart
# -----------------------------
plt.figure()
monthly_avg_temp.plot(marker='o')
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("visualizations/monthly_avg_temperature.png")
plt.show()

# -----------------------------
# 6. Visualization 2: Histogram
# -----------------------------
plt.figure()
plt.hist(df['humidity'], bins=20)
plt.title("Humidity Distribution")
plt.xlabel("Humidity")
plt.ylabel("Frequency")
plt.savefig("visualizations/humidity_distribution.png")
plt.show()

# -----------------------------
# 7. Validation
# -----------------------------
assert df.isnull().sum().sum() == 0
assert 'temperature_(c)' in df.columns

print("Analysis completed successfully")
