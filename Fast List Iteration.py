# Обычный способ

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)

# Списковое включение

even = [number for number in numbers if number % 2 == 0]
