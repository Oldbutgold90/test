height = int(input('Введите высоту пирамидки- '))
side = 1
brush = 1
for row in range(1, height + 1):
  print('\t' * (height - row), end = '')
  for col in range(row):
    print(brush, end = '')
    print('\t' * 2, end = '')
    brush += 2
  print()