quan = int(input('Введите количество чисел: '))
marker = 0
sum = 0
win1 = 0
win2 = 0
for num in range(quan):
  numb = int(input('Введите число: '))
  win1 = numb
  while numb != 0:
    sum += numb % 10
    numb //= 10
  if sum > marker:
    marker = sum
    win2 = win1
  win1 = 0
  sum = 0
print('Выведите на экран это число', win2,' и сумму его цифр', marker)