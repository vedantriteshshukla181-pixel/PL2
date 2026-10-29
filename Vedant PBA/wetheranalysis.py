import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

print("Average Temperature:", df["Temperature"].mean())
print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())

day = df.loc[df["Temperature"].idxmax(), "Day"]
print("Hottest Day:", day)

plt.plot(df["Day"], df["Temperature"], marker='o')
plt.title("Daily Temperature Changes")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()

plt.hist(df["Temperature"], bins=5, edgecolor='black')
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["Humidity"], df["Temperature"])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.show()