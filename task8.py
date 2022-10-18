money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
money = money_capital
while money > spend:
    money = money - spend + salary
    spend = spend + increase*spend
    month = month + 1
print(month)
