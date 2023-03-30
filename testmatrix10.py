num = 0
for row in range(6):
  num = row
  for col in range(6):
    print(num + col, end = ' ')
    num += 1
  print()