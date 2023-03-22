print('Задача 4. Театр')
line = int(input('Введите кол-во рядов: '))
seat = int(input('Введите кол-во сидений в ряду: '))
space = int(input('Введите кол-во метров между рядами: '))
print('\nСцена\n')
for n in range(line):
 maket = '=' * seat
 maket = maket + ' ' + '*' * space + ' ' + maket
 print(maket)