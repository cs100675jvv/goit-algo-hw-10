import pulp

# Створення моделі оптимізації
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішення
x_lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість лимонаду
x_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Цільова функція
model += x_lemonade + x_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * x_lemonade + 1 * x_juice <= 100, "Water_Constraint"  # Обмеження на воду
model += 1 * x_lemonade <= 50, "Sugar_Constraint"  # Обмеження на цукор
model += 1 * x_lemonade <= 30, "Lemon_Juice_Constraint"  # Обмеження на лимонний сік
model += 2 * x_juice <= 40, "Fruit_Puree_Constraint"  # Обмеження на фруктове пюре

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Статус оптимізації: {pulp.LpStatus[model.status]}")
print(f"Оптимальна кількість лимонаду: {x_lemonade.varValue}")
print(f"Оптимальна кількість фруктового соку: {x_juice.varValue}")
print(f"Максимальна кількість напоїв: {pulp.value(model.objective)}")
