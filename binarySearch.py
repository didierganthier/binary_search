def binarySearch(sortedList, target):
 left = 0
 right = len(sortedList) - 1
 while (left <= right):
  mid = (left + right)/2
  if (sortedList(mid) == target):
   return mid
  elif(sortedList(mid) < target):
   left = mid + 1
  else:
   right = mid - 1

# If target is not in the list, return -1
 return -1

binarySearch([1,3,9,22],22)
# return 3