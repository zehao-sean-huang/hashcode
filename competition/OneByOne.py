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
 limit = 1   # the minimum number of score we are satisfied to get each time
 current = 0   # current picture we are processing
 result = []   # the final result

 print("second phase started")
 
 def findNext():
  nonlocal current, result
  currentElement = li[current]

  for i in range(current, len(li)):
   if calScore(currentElement, li[i]) >= limit:
   
    if current > i:
     pass
    else:
     i -= 1
    
    result.append(li.pop(current))
    current = i

    return

  result.append(li.pop(current))

  
  for i in range(len(li)):
   if random.randint(0, 10) > 3:
    current = i
    return
  current = 0
  return

 while(len(li) > 0):
  findNext()
  
 print("second phase ended ...")



 return result