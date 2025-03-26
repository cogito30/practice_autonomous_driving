# Data Loading and Analysis
import pandas as pd

data = {"시간": ["10:00", "10:05", "10:10"], "속도(km/h)": [40, 42, 38]}
df = pd.DataFrame(data)
print(df)

# Visualization
import matplotlib.pyplot as plt

time = ["10:00", "10:05", "10:10"]
speed = [40, 42, 38]

plt.plot(time, speed, marker='o', linestyle='-', color='b', label="Speed")
plt.xlabel("Time")
plt.ylabel("Speed (km/h)")
plt.title("Vehicle Speed Over Time")
plt.legend()
plt.grid()
plt.show()

