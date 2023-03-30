width = int(input('Введите ширину рамки- '))
height = int(input('Введите высоту рамки- '))
for row in range(height + 1):
  for col in range(width + 1):
    if (row == 0 or row == height) and not (col == 0 or col == width):
      print('_', end = ' ')
    elif (col == 0 or col == width) and not row == 0:
      print('|', end = ' ')
    else:
      print(' ', end = ' ')
  print() 