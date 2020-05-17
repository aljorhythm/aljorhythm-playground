# Number of Students Doing Homework at a Given Time
# Given two integer arrays startTime and endTime and given an integer queryTime.

# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.



a = list("asd")
b = list("zxc")
print(list(zip(a, b)))

print(list(filter()))

queryTime = 4
startTime = [1,2,3]
endTime = [3,2,7]

l = len(filter(lambda se: queryTime >= se[0] & queryTime <= se[1], zip(startTime,endTime)))
print(l)