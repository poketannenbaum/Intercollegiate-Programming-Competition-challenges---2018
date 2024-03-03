file = open("digitproductsequence.txt", "r")
numbers = file.read()
startnum = numbers
numbers = list(numbers)
numbers = list(map(int, numbers))
originalnumbers = []
iteratednum = 1
iterationcounter = 0
currentnum = " "
ogcurrentnum = 1
counter = 0
ognumbers = []
originalnumbers.append(ogcurrentnum)
ognumbers.append(1)
while (True):
	ogiratednum = 1
	iteratednum = 1
	if (currentnum == " "):
		currentnum = int(startnum)
	iterationcounter += 1
	for num in numbers:
		if (num == 0):
			continue
		else:
			iteratednum *= num
	while (int(ogcurrentnum) <= int(currentnum)):
		ogiratednum = 1
		for num in ognumbers:
			if (num == 0):
				continue
			else:
				ogiratednum *= num
		ognumbers = ogcurrentnum + ogiratednum
		ogcurrentnum = ognumbers
		ognumbers = str(ognumbers)
		ognumbers = list(ognumbers)
		ognumbers = list(map(int, ognumbers))
		originalnumbers.append(ogcurrentnum)
	if (currentnum in originalnumbers):
			break
	numbers = currentnum + iteratednum
	currentnum = numbers
	numbers = str(numbers)
	numbers = list(numbers)
	numbers = list(map(int, numbers))
print(f"{startnum} converged at {currentnum} requiring {iterationcounter - 1} iteration(s)")