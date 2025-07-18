from scipy.optimize import curve_fit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/filepath/pendulum_data.csv")
# Define the model function
def model(t, A, T, phi):
return A* np.cos (2 np.pit/T+ phi)
# Fit curve
params, = curve_fit (model, df['time'], df['angle'], p*theta = [1theta, 2, theta] )
A_fit, T_fit, phi_fit params
print(f"Fitted Period: {T_fit:.2f} s")
#Plot fit
t_fit = np.linspace(0, 2, 500)
plt.plot(df['time'], df['angle'], 'bo', label='Data')
plt.plot(t_fit, angle_fit, 'r', label='Fit')
plt.legend()
plt.show()
