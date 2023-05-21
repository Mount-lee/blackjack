koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
import random
random.shuffle(koloda)

print("Го в блэкджэк?")
count = 0


while True:
	choise = input("Будете брать карту? y/n\n")
	if choise == 'y':
		kol = koloda.pop()
		print("Вам попалась карта достоинством %d" %kol)
		count+=kol
		if count > 21:
			print("Извините, но вы проиграли")
			break
		elif count == 21:
			print("Поздравляем, вы набрали 21 очко!")
			break
		else:
			print("У вас %d очков." %count)
	elif choise == 'n':
		print("У вас %d очков и вы решили закончить игру." %count)
		break
print("До новых встреч!")

