quan = int(input('Введите количество чисел: '))
simple = 0
for num in range(quan):
  numb = int(input('Введите число: '))
  marker = True
  for sim in range(2, numb):
   if numb % sim == 0:
     marker = False
   if marker == False:
     break
  if marker == True:
    simple += 1
print('Количество простых чисел в последовательности: ', simple)