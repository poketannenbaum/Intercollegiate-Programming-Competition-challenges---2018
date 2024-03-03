import re
import math
file = open("closepoints.txt", "r")
numbers = file.read()
numbersarr = re.split(" ", numbers)
answersarr = []
answersarr2 = []
answersarr3 = []
distarr = []
counter = len(numbersarr)
counter2 = 0
while (True):
	try:
		answersarr.append(numbersarr[counter2] + " " + numbersarr[counter2 + 1])
	except:
		break
	counter2 += 2
for ans in answersarr:
	ansint = re.split(" ", ans)
	ansint = list(map(int, ansint))
	for ans2 in answersarr:
		ans2int = re.split(" ", ans2)
		ans2int = list(map(int, ans2int))
		if (ans == ans2):
			continue
		else:
			thex = (ans2int[0] - ansint [0])
			they = (ans2int[1] - ansint [1])
			thex = thex * thex
			they = they * they
			numtosquare = thex + they
			distance = math.sqrt(numtosquare)
			distarr.append(distance)
			answersarr3.append (ans)
			answersarr3.append (ans2)
			answersarr3.append (distance)
			distance = str(distance)
			answersarr2.append(ans + " " + ans2 + " " + distance)
distarr.sort()
pointer = answersarr3.index(distarr[0])
point1 = " "
point2 = " "
point1 = answersarr3[pointer - 2]
point2 = answersarr3[pointer - 1]
distance = str(answersarr3[pointer])
point1 = re.split (" ", point1)
point2 = re.split (" ", point2)
print(f"Closest 2 points are ({point1[0]}, {point1[1]}) and ({point2[0]}, {point2[1]}).")
print(f"The distance is {distance}")