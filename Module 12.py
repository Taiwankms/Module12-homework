per_cent = {'ТКБ': 5.6,
            'СКБ': 5.9,
            'ВТБ': 4.28,
            'СБЕР': 4.0}
money = input("Введите сумму")
deposit = [per_cent['ТКБ']*float(money)//100,
           per_cent['СКБ']*float(money)//100,
           per_cent['ВТБ']*float(money)//100,
           per_cent['СБЕР']*float(money)//100]
print('Сумма:')
print(money)
print('Депозит:')
print(deposit)
print('Максимальная сумма, которую вы можете заработать:')
print(max(deposit))
#print(per_cent.keys())

