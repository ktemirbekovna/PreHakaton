# Задание №1:

# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, то получим 3, 5, 6 и 9. 
# Сумма этих чисел равна 23 (3+5+6+9) = 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
a = 0
for i in range(0, 1000):
 if(i % 3 == 0 or i % 5 == 0):
  print(i)
  a = a + i
  print(a)