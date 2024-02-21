#!/user/bin/env python3
# elso program
a = input ("Adj meg egy fajl nevet: ")
try:
	for line in open(a):
		print(line, end="")
except IOError:
	print("I/O hiba!")
	exit()
except:
	print("Valamilyen hiba")
	exit()
