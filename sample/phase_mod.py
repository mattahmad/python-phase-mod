# PM Modulation Python Script
import numpy as np
import matplotlib.pyplot as plt
# Define the modulation index (m) and the frequency of the carrier signal (fc)
m = 0.25
fc = 30
# Generate time values for the input signal
t = np.linspace(0, 1, 1000)
# Generate the input signal using a sinusoidal wave
input_signal = np.sin(2 * np.pi * 5 * t)
input_signal = input_signal.astype(int)
# Generate the carrier signal using a sinusoidal wave
carrier_signal = np.sin(2 * np.pi * fc * t)
# Calculate the phase change as per positive and negative cycles of the input signal
for val in input_signal:
  if input_signal[val] >= 0:
    phase = m * np.sin(2 * np.pi * 5 * t)
  else:
    phase = -m * np.sin(2 * np.pi * 5 * t)
# Generate PM Modulated Signal
pm_modulated_signal = np.sin(2 * np.pi * fc * t + phase)
plt.subplot(3,1,1)
plt.plot(t, input_signal)
plt.title("Analog Message signal")
plt.subplot(3,1,2)
plt.plot(t, carrier_signal)
plt.title("RF carrier signal")
plt.subplot(3,1,3)
plt.plot(t, pm_modulated_signal)
plt.title("Phase Modulated Signal")
plt.tight_layout()
plt.show()