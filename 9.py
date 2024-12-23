import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Ініціалізація даних
x_range = 180
r_max = 200

# Змінна для напрямку A
a_direction = 1
A_value = 0

# Масив для збереження значень L
L_values = []

# Функція, яка імітує прийом даних через серійний порт
def receive_data():
    global A_value, a_direction

    # Генерація A з циклічним збільшенням і зменшенням
    if A_value >= 180:
        a_direction = -1
    elif A_value <= 0:
        a_direction = 1

    A_value += a_direction
    L = random.randint(0, 200)  # Значення L від 0 до 200
    return A_value, L

# Функція для оновлення графіка
def update(frame):
    global L_values

    # Отримання даних
    A, L = receive_data()

    # Очищення графіка
    ax.clear()

    # Налаштування осей
    ax.set_xlim(-r_max, r_max)
    ax.set_ylim(0, r_max)

    # Побудова півкола
    theta = np.linspace(0, np.pi, 500)
    x_circle = r_max * np.cos(theta)
    y_circle = r_max * np.sin(theta)
    ax.plot(x_circle, y_circle, color='black', alpha=0.5)

    # Додавання лінії для A
    angle_rad = np.deg2rad(A)
    x_A = r_max * np.cos(angle_rad)
    y_A = r_max * np.sin(angle_rad)
    ax.plot([0, x_A], [0, y_A], color='red', linestyle='--', label=f'A: {A}')

    # Додавання нових ліній L, якщо L <= 150
    if L <= 150: # Додає лінії при змінному значенні
        adjusted_length = 180 - L
        L_values.append((A, adjusted_length))
        print(L)

    # Відображення ліній L та фільтрація за значенням A
    filtered_L_values = []
    for angle, length in L_values:
        if 0 < A < 180:  # Лінії зникають, коли A досягає 0 або 180
            angle_rad = np.deg2rad(angle)
            x_L_start = r_max * np.cos(angle_rad)
            y_L_start = r_max * np.sin(angle_rad)
            x_L_end = (r_max - (180 - length)) * np.cos(angle_rad)
            y_L_end = (r_max - (180 - length)) * np.sin(angle_rad)
            ax.plot([x_L_start, x_L_end], [y_L_start, y_L_end], color='blue', alpha=0.7)
            filtered_L_values.append((angle, length))

    L_values = filtered_L_values

    # Легенда
    ax.legend()

# Ініціалізація графіка
fig, ax = plt.subplots(figsize=(8, 6))
ani = animation.FuncAnimation(fig, update, interval=100)

# Показ графіка
plt.show()
