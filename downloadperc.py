print('Задача 3. Аналог Steam')
size = int(input('Укажите размер файла для скачивания: '))
ispeed = int(input('Какова скорость вашего соединения? '))
speed = ispeed
count = 0
while True:
  count +=1
  if speed < size:
    print('Прошло ', count, 'сек. Скачано ',speed, ' из ', size, ' Мб (', round(speed / (size / 100)), '%)')
    speed += ispeed
  elif speed >= size:
    print('Прошло ', count, 'сек. Скачано ',size, ' из ', size, ' Мб (100%)')
    break