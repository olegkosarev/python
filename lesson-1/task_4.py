n = str(input("Введите целое положительное число "))


l = len(n)

i = 1

n1 = int(n[0])

while(i<l):
	n2 = int(n[i])

	if n1<n2:
		n1=n2

	i +=1

print(n1)
