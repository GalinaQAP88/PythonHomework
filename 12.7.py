percent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=input("Введите сумму депозита:")
money=int(money)
allrates=list(percent.values())
deposit=[int(value * money) for value in allrates]
print(deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
