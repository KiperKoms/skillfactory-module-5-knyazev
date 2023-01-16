#Приветствие и выбор начала игры.
def intro():
    print("-" * 60)
    print('| Приветсвую Вас в игре "Крестики-нолики" для двух игроков |')
    print("-" * 60)
    start = 0
    while start != "Q" and start != "S":
        start = input('Для старта введите "S", для выхода из игры - "Q"')
    if start == "S":
        return True

#Выбор начать новую игру или закончить
def next_game():
    finish = 0
    while finish != "Q" and finish != "C":
        finish = input('Для новой игры введите "С", для выхода из игры - "Q"')
        if finish == "C":
            return True

#Отрисовка поля.
def draw_field(field):
   print("-" * 13)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
   print("-" * 13)

#Выбор игроком существующей клетки
def step_person(field, person):
    print(f"Ход {person}")
    while True:
        step = input('Введите номер незанятой клетки')
        if not step.isdigit():
            print('Вы ввели не число')
            continue
        step = int(step)
        if step < 1 or step > 9:
            print('Нет такой позиции, число вне диапазона')
            continue
        if str(field[step - 1]) in "X0":
            print('Клетка занята')
            continue
        else:
            break
    return step

#Условия окнчания игры (выйгрыш или ничья)
def end_game(count, field, person):
    vin_positions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for position in vin_positions:
        if field[position[0]] == field[position[1]] == field[position[2]]:
            print(f'Выйграл {person}')
            return True
    if count == 9:
        print('Ничья')
        return True

#Заполение поля
field = list(range(1, 10))

# Победные комбинации
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

#Основная программа
if intro():
    count = 0
    while True:
        draw_field(field)
        if count % 2 == 0:
            person = "X"
        else:
            person = "0"
        step = step_person(field, person)
        count += 1
        field[step - 1] = person
        if end_game(count, field, person):   #Если игра завершилась (победа или ничья)
            draw_field(field)                #Отрисовка конечного варианта ходов
            if next_game():                  #Предоставление выбора закончить игру или начать заново
                field = list(range(1, 10))
                count = 0
                continue
            else:
                print("До новых встреч!")
                break
else:
    print("До новых встреч!")
