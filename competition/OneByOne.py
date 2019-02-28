import random

# Calculate the Score betwee two consecutive slides


def calScore(a, b):
	x, y, z = 0, 0, 0
	for item in a[1]:
		if item not in b[1]:
			y += 1
		else:
			x += 1
	for item in b[1]:
		if item not in a[1]:
			z += 1
	return min(x, y, z)

# Input: a list of labels
# Output: a list of labels after rearrangement


def oneByOne(li):
	limit = 1			# the minimum number of score we are satisfied to get each time
	current = 0 		# current picture we are processing
	chosen = []			# Whether each slides has been picked to result, 1 - not picked 0- picked
	result = []			# the final result

	for i in range(len(li)):
		chosen.append(1)
	print("second phase started")
	
	def findNext():
		nonlocal current, result, chosen
		length = len(chosen)
		currentElement = li[current]
		for i in range(current, length):
			if chosen[i] and calScore(currentElement, li[i]) >= limit:
				chosen[current] = 0
				current = i
				result.append(li[current])
				return
		chosen[current] = 0
		result.append(currentElement)
		for i in range(length):
			if chosen[i] and random.randint(0, 10) > 5:
				current = i
				return
		for i in range(length):
			if chosen[i]:
				current = i
				return

	if(len(li) > 5000):
		result1 = oneByOne(li[:len(li)//2])
		result2 = oneByOne(li[len(li)//2:])
		result = result1 + result2

	else:
		while(sum(chosen) > 0):
			findNext()
			if sum(chosen) % 1000 == 0:
				print(sum(chosen), " photos left for processing.")
		
	print("second phase ended ...")



	return result
