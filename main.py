per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму вклада: ")) # Ввод суммы вклада

deposit = [round(money * rate / 100) for rate in per_cent.values()] # Подсчет средств

print("Накопленные средства в каждом из банков:", deposit) # Вывод результатов

max_deposit = max(deposit)
max_index = deposit.index(max_deposit) # Максимальное значение

print(f"Максимальная сумма, которую вы можете заработать — {max_deposit}")
