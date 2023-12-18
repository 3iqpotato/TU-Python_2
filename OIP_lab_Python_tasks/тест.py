import numpy as np
import matplotlib.pyplot as plt

# Параметри на синусоидалния сигнал
A = 1  # Амплитуда
f = 1  # Честота в Hz
phi = 0  # Начална фаза

# Генериране на времевата ос
t = np.linspace(0, 2, 1000)  # време от 0 до 2 секунди

# Генериране на синусоидалния сигнал
x = A * np.sin(2 * np.pi * f * t + phi)

# Начертаване на сигнала
plt.plot(t, x)
plt.title('Синусоидален сигнал')
plt.xlabel('Време (секунди)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

