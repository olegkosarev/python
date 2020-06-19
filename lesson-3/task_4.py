def my_func(x, y):
	
	x1=x
	i = 1
	while i<abs(y):
		x1=x1*x
		i +=1

	return(1/x1)


print(my_func(7,-3))