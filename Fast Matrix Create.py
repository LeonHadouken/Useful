# Обычный способ создания матрицы

map = []
for row in range(rows):
    map.append([0] * columns)

# Быстрый способ

map = [([0] * columns) for row in range(rows)]
