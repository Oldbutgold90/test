def summa_n(number):
    summa = 0
    if number < 0:
        print('negative')
    else:
        for n in range(1, number + 1):
            summa += n
    return summa
number = int(input('Введите число: '))

print('Сумма от 1 до ', number, '=', summa_n(number))
print('Сумма от 1 до ', summa_n(number), '=', summa_n(summa_n(number)))




