tickets = int(input("При покупке больше трёх билетов действует скидка 10%\n"
                   "Введите количество билетов:"))
age = list(map(int, input("Укажите возраст посетителей через пробел: ").split()))
while tickets != len(age):
    age = list(map(int, input("Количество не совпадает.\n"
                              "Укажите возраст посетителей через пробел: ").split()))
price = []
for i in age:
    if i in range(0, 18):
        price.append(0)
    elif i in range(18, 25):
        price.append(990)
    else:
        price.append(1390)
if tickets > 3:
    print("Суммас учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "руб.")
else:
    print("Сумма: ", sum(price), "руб.")
