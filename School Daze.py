import re
file = open("lockers.txt", "r")
nums = file.read()
numsarr = re.split(" ", nums)
numsarr = list(map(int, numsarr))
amtoflockers = numsarr[0]
ogamtoflockers = numsarr[0]
amtofstudents = numsarr[1]
ogamtofstudents = numsarr[1]
lockerarr = []
while(amtoflockers != 0):
	lockerarr.append(0)
	amtoflockers -= 1
pointer = 0
whatRUdoingsteppointer = 1
while(amtofstudents != -1):
	while(True):
		try:
			if(lockerarr[pointer] == 0):
				lockerarr[pointer] = 1
			else:
				lockerarr[pointer] = 0
			pointer += whatRUdoingsteppointer
		except:
			break
	pointer = 0
	whatRUdoingsteppointer += 1
	amtofstudents -= 1
ans = lockerarr.count(1)
print(f"{ogamtoflockers} Lockers: {ogamtofstudents} Students; {ans} Open Lockers")