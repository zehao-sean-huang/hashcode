import random
 
# Calculate the Score betwee two consecutive slides

def calScore(a, b):
	x, y, z = 0
	for item in a:
		if item not in b:
			y += 1
		else:
			x += 1
	for item in b:
		if item not in a:
			z ++
	return min(x, y, z)

# Input: a list of labels
# Output: a list of labels after rearrangement

def oneByOne(li):
	limit = 1			# the minimum number of score we are satisfied to get each time
	current = 0 		# current picture we are processing
	chosen = []			# Whether each slides has been picked to result, 1 - not picked 0- picked
	result = []			# the final result

	for i in range(len(li)):
		chosen.append(1);

	def findNext():
		nonlocal current, result, chosen
		for i in range(current, len(li)):
			if chosen[i] and calScore(li[current], li[i]) >= limit:
				chosen[current] = 0
				current = i
				result.append(li[current])
				return 
		chosen[current] = 0
		result.append(li[current])
		for i in range(len(chosen)):
			if chosen[i] and random.randint(0,10) > 5:
				current = i
				return
		for i in range(len(chosen)):
			if chosen[i]:
				current = i
				return

	while(sum(chosen) > 0):
		findNext()

	return result
