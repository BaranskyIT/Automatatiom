def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False

sel_year = input("Введите год: ")

sel_year = int(sel_year)

true_false = is_year_leap(sel_year)

print("Год", sel_year, ":", true_false)