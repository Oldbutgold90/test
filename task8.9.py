print('Задача 9. Коровы')
milkaday = 0
milkstall = 2
stall = input('Введите данные заполнения 10 стойл с коровами символами a и b: ')
for cow in stall:
  if cow == 'b':
    milkaday += milkstall
  milkstall += 2
print('Со всех стойл выйдет ',milkaday,'л молока в день')