import random

hidden_value = random.randint(1,10)
print("Dhammunte guess cheyra shikavattu guess cheste icchesta laptopuuuuu!")
user_input = 0
while True:
	user_input=int(input("Guess cheyra shikavattu :"))
	if(user_input == hidden_value):
		print("\nParledhu dha ra shikavattu dammundi niku")
		break
	elif user_input > hidden_value:
		print("\nRey shikavtttu pedda number guess chesav raaa")
		print("Ega savak hint estunna patu. ",user_input-hidden_value," difference undi chuskooooo")
	elif user_input < hiden_value:
		print("\nReyyyy esari chinna number guess chesav raa shikavattu")
		print("Ega savak hint estunna patu. ",abs(user_input-hidden_value)," difference undi chuskooooo")
	else:
		print("inkosari chance istunna guess cheyra shikavattu")

	
	
	