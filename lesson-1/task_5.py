revenue = int(input("Введите выручку "))
cost = int(input("Введите издержки "))

profit = revenue-cost

print("Финансовый результат "+str(profit))

if profit > 0:
	rentabel = profit/revenue
	print("Рентабельность "+str(rentabel))


employees = int((input("Введите количество сотрудников ")))

print("прибыль фирмы в расчете на одного сотрудника "+str(profit/employees))
