import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтегралу
n_points = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(0, max(y), n_points)

# Обчислення кількості точок під кривою
points_under_curve = y_random < f(x_random)
area = (b - a) * max(y) * np.mean(points_under_curve)

print(f"Інтеграл методом Монте-Карло: {area}")

# Перевірка з використанням quad
result, error = spi.quad(f, a, b)
print(f"Інтеграл за допомогою quad: {result}")

# Порівняння
print(f"Похибка методу Монте-Карло: {abs(area - result)}")
