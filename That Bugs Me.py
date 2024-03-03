file = open("onebits.txt", "r")
numbers = file.read()
numbers = list(numbers)
while("\n" in numbers):
	numbers.remove("\n")
while(" " in numbers):
	numbers.remove(" ")
numbers = list(map(int, numbers))
size = int(numbers[0])
numbers.pop(0)
fieldarr = []
placeholderarr = []
sizecounter = 0
placeholderstr = ""
while(True):
	while(sizecounter < size):
		try:
			placeholderstr += str(numbers[0])
			numbers.pop(0)
			sizecounter += 1
		except:
			break
	placeholderarr.append(placeholderstr)
	placeholderarr[0] = list(placeholderarr[0])
	fieldarr.append(placeholderarr)
	placeholderarr = []
	placeholderstr = ""
	try:
		numbers[0]
	except:
		break
	sizecounter = 0
print(fieldarr)