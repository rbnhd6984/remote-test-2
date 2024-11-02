first_wagon_num = int(input("Введите номер вагона Вити: "))
current_wagon_num = int(input("Введите номер вагона, который написан на вагоне: "))
if first_wagon_num == current_wagon_num:
    print("Без доп информации, решение невозможно")
else:
    print(first_wagon_num + current_wagon_num - 1)
