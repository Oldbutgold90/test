print('Задача 6. Спецшифр')
text = input('Введите строку ')
scount1 = 0
scount2 = 0
for symbol in text:
 if symbol == 's':
   scount1 += 1
 else:
   scount1 = 0
 if scount1 > scount2 :
  scount2 = scount1
print(' Самая длинна последовательность: ',scount2)