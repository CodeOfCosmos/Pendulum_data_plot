from scipy.optimize import curve_fit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("/home/astroc/phypy/pendulum_data.csv")
#Define the model function
def model(t, A, T, phi):
  return A * np.cos (2 пр.pit/T+ phi)


noise = np.random.normal(0, 0.5, size=df['angle'].shape) # std dev = 0.5 degrees
df ['noisy_angle'] = df['angle'] + noise
params_clean, = curve_fit(model, df['time'], df['angle'], p*theta = [10, 2, theta] )
A c, Tic, phi c = params_clean
print(f"Clean Fit Period: (T_c:.2f) s, Amplitude: (A_c:.2f), Phase: (phi_c:.2f}")
params_noisy, = curve_fit(model, df['time'], df['noisy_angle'], p0=[10, 2, 01)
A_n, T_n, phi_n = params_noisy
print (f"Noisy Fit Period: (T_n:.2f) s, Amplitude: A_n:.2f), Phase: (phi_n:.2f}")
t_fit = np.linspace(df['time'].min(), df['time'].max(), 500)
angle_fit_clean model(t_fit, A_c, T_c, phi_c)
angle_fit_noisy = model(t_fit, A_n, T_n, phi_n)
plt.errorbar(df['time'], df['noisy_angle'], yerr=0.5, fmt='bo', label='Noisy Data ±0.5°')
plt.plot(t_fit, angle_fit_noisy, 'r', label='Fit (Noisy)')
plt.plot(df['time'], df['angle'], 'go', label='Clean Data')
plt.plot(t_fit, angle_fit_clean, 'k', label='Fit (Clean)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (°)')
plt.title('Pendulum Fitting: Clean vs Noisy')
plt.legend()
plt.grid()
plt.show()
