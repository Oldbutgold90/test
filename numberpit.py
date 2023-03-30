number = int(input('Введите число для ямы: '))
print()
q = number - 1
while q >= 0:
  for i in range(-number, number + 1):
    if abs(i) > q:
      print(abs(i), end = '')
    elif i == 0:
      print('.', end = '')
    else:
      print('.', end = '')
  q -= 1
  print()