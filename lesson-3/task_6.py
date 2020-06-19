def int_func(word):
	return(word.capitalize())


sentence = input("введите строку из латинских букв ").split()

new_sentence = ""

for el in sentence:
	el = int_func(el)
	new_sentence +=el+" "


print(new_sentence)