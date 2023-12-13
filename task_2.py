salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

capital_ = 0
for _ in range(months):
    capital_ += spend - salary
    spend *= 1 + increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital_, 2))
