file = open("onebits.txt", "r")
numbers = file.read()
ognumber = int(numbers)
numbers = int(numbers)
numbers = bin(numbers)
numbers = str(numbers)
numbers = list(numbers)
ans = numbers.count("1")
othernumberscount = 0
runningnums = ognumber - 1
ogrunningnums = ognumber - 1
counter = 1
while(runningnums != -1):
	runningnums = int(runningnums)
	runningnums = bin(runningnums)
	runningnums = str(runningnums)
	runningnums = list(runningnums)
	compareans = runningnums.count("1")
	if(compareans == ans):
		othernumberscount += 1 
	counter += 1
	runningnums = ognumber - counter
print(f"{ognumber} in binary has {ans} 1-bits. There are {othernumberscount} other numbers with {ans} 1-bits between 0 and {ognumber}")