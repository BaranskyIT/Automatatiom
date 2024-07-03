def month_to_season(month):
    return ['Зима', 'Весна', 'Лето', 'Осень'][(month%12)//3]

x = int(input("Введите порядковый номер месяца: "))
print(month_to_season(x))