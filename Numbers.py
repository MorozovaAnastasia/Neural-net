import random
 
# Обучающая выборка
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
 
# Список всех цифр
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
 
# Тестовая выборка
num92 = list('011101111001111')
num93 = list('110101111001111')
num94 = list('110101111001110')
num95 = list('111101111001110')
num96 = list('111111111001111')
 
# Создание весов сети
weights = []
for i in range(15):
    weights.append(0)
 
# Порог функции активации
bias = 7
 
# Является ли данное число 9
def proceed(number):
    # Рассчитываем взвешенную сумму
    net = 0
    for i in range(15):
        net += int(number[i])*weights[i]
 
    # Превышен ли порог? (Да - сеть думает, что это 9. Нет - сеть думает, что это другая цифра)
    return net >= bias
 
# Уменьшение значений весов, если сеть ошиблась и выдала 1
def decrease(number):
    for i in range(15):
        # Возбужденный ли вход
        if int(number[i]) == 1:
            # Уменьшаем связанный с ним вес на единицу
            weights[i] -= 1
 
# Увеличение значений весов, если сеть ошиблась и выдала 0
def increase(number):
    for i in range(15):
        # Возбужденный ли вход
        if int(number[i]) == 1:
            # Увеличиваем связанный с ним вес на единицу
            weights[i] += 1
 
# Тренировка сети
for i in range(100000):
    # Генерируем случайное число от 0 до 9
    option = random.randint(0, 9)
 
    # Если получилось не 9
    if option != 9:
        # Если сеть выдала True, то уменьшаем вес
        if proceed(nums[option]):
            decrease(nums[option])
    # Если получилось число 9
    else:
        # Если сеть выдала False, то увеличиваем вес
        if not proceed(num9):
            increase(num9)
 
# Вывод значений весов
print(weights)
 
# Пройдемся по обучающей выборке
print("0 это 9? ", proceed(num0))
print("1 это 9? ", proceed(num1))
print("2 это 9? ", proceed(num2))
print("3 это 9? ", proceed(num3))
print("4 это 9? ", proceed(num4))
print("6 это 9? ", proceed(num6))
print("7 это 9? ", proceed(num7))
print("8 это 9? ", proceed(num8))
print("9 это 9? ", proceed(num9), '\n')
 
# А теперь по тестовой выборке
print("это 9? ", proceed(num9))
print("это 9? ", proceed(num92))
print("это 9? ", proceed(num93))
print("это 9? ", proceed(num94))
print("это 9? ", proceed(num95))
print("это 9? ", proceed(num96))