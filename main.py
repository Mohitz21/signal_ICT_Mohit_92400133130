import numpy as np
from signal_ICT_Mohit_92400133130 import unitary_signals, trigonometric_signals, operations

# Task 1: Discrete signals
n = np.arange(-5, 15)

step = unitary_signals.unit_step(n)
impulse = unitary_signals.unit_impulse(n)
ramp = unitary_signals.ramp_signal(n)

# Task 2: Trigonometric signals
t = np.linspace(0, 1, 500)  # time vector
sine = trigonometric_signals.sine_wave(2, 5, 0, t)
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
exponential_signal = trigonometric_signals.exponential_signal(2, 5,t)

# Task 3: Operations
# Example 1: Time shift sine wave by +5
shifted_sine = operations.time_shift(sine, 5)
scale_sine = operations.time_scale(sine, 5)


# Example 2: Add unit step and ramp
added = operations.signal_addition(step, ramp)

# Example 3: Multiply sine and cosine wave
multiplied = operations.signal_multiplication(sine , cosine)