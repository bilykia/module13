
per_cent ={'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

Money= int(input("Print money:"))
deposit=[]
deposit.append(int(Money/100*per_cent ['ТКБ']))
deposit.append(int(Money/100*per_cent ['СКБ']))
deposit.append(int(Money/100*per_cent ['ВТБ']))
deposit.append(int(Money/100*per_cent ['СБЕР']))

print(deposit)
print(max(deposit))
