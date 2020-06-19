def my_func(a, b, c):
	rank_list =sorted([a, b, c], reverse = True)
	return (rank_list[0]+rank_list[1])


print(my_func(100,5,6))