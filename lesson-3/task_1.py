def division(a, b):
	if b==0:
		return ("делить на 0 нельзя")
	else:
		return (str(a/b))



a = int(input("введите делимое "))
b = int(input("введите делитель "))


print(division(a, b))