import pandas as pd
import matplotlib.pyplot as plt
#Read the CSV file
df= pd.read_csv("/filepath/pendulum_data.csv")
#Plot
еггог = 0.5 # you can change this based on your assumption
plt.errorbar(df['time'], df['angle'], yerr error, fmt='bo', label='Measured with Eггог')
plt.plot(df['time'], df['angle'], 'bo-')
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.title("Pendulum Oscillation")
plt.grid(True)
plt.legend()
plt.show()
