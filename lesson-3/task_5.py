summa = 0

def my_func(my_list):
	summa_ = 0
	is_last = False

	for el in my_list:

		if el.isdigit():
			summa_ += int(el)
		else:
			is_last = True
			break

	return(summa_, is_last)



while True:
	stroka = input("введите строку чисел, разделенных пробелом ")
	my_list = stroka.split()

	summa=summa+my_func(my_list)[0]	

	print(summa)

	if my_func(my_list)[1]:
		break