import numpy as np
import pandas as pd
#Parameters
A = 10
# degrees
T = 2.0
# seconds
phi = 0
t = np.arange(0, 2.0, 0.05) # time steps
# Angle values using cosine formula
theta Anp.cos (2 np.pi t / T + phi)
df = pd.DataFrame(('time': t, 'angle': theta))
df.to_csv("/home/username/foldername/pendulum_data.csv", index=False)
