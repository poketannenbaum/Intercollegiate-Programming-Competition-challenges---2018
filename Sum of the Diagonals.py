import re
import numpy as np
file = open("sumofdiagonals.txt", "r")
numbers = file.read()
numbers = re.split(" ", numbers)
size = int(numbers[0])
numbers.pop(0)
counter = 0
pointer = 0
numbarray = []
while (True):
	placeholder = ""
	counter = 0
	while(counter < size):
		try:
			placeholder += numbers[0]
			counter += 1
			if (counter != size):
				placeholder += " "
			numbers.pop(0)
		except:
			break
	numbarray.append(placeholder)
	try:
		numbers[0]
	except:
		break
counter = 0
answer = 0
while (counter < size):
		workingarrnum = re.split(" ", numbarray[counter])
		workingarrnum = list(map(int, workingarrnum))
		answer = answer + workingarrnum[counter]
		counter += 1
revcounter = 0
counter -= 1
while (counter > -1):
		workingarrnum = re.split(" ", numbarray[counter])
		workingarrnum = list(map(int, workingarrnum))
		answer = answer + workingarrnum[revcounter]
		counter -= 1
		revcounter += 1

print(f"Sum of diagonals is {answer}")