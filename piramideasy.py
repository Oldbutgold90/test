print('Задача 6. Пирамидка')
height = int(input('Введите высоту пирамидки- '))
side = 1
brush = '#'
for n in range(height - 1):
  side +=2
for row in range(height):
  for col in range(side):
    if col != side // 2:
      print(' ', end = '')
    else:
      print(brush, end = '')
      side -= 2
  brush += '##'
  print()
