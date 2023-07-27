def minList(l):
    if len(l) == 1:
        return l[0]

    minSmallArray = minList(l[1:])
    overallMin = min(minSmallArray, l[0])
    return overallMin




import sys
def printMin(l, minSoFar = 1000000):
    if len(l) == 0:
        print(minSoFar)
        return
    newMin = min(minSoFar, l[0])
    printMin(l[1:], newMin)

l = [1, 2, 3]
printMin(l)

# Dry run
# Concept here is to use the large number and create a variable, initialize it with largest number and then
# compare it with every element, and update it with the smallest one
# Starting with dry run, it first checks if length of list is 0 or not,
# it is not so it gives min between minSoFar and l[0]
# So min is 1, so it updates newMin variable to 1.
# Then it calls recursion to l[1:] part of list which is [2, 3].
# Now it checks if the len is 0 or not, it is not so it checks min between minSoFar and l[0]
# which is between 1 & 2 and we passed newMin as arg in place of minSoFar during recursion, so statement becomes
# newMin = min(1, 2) where minSoFar is 1 and l[0] is 2.
# So newMin becomes 1 and then it calls recursion to l[1:] part of list
# So list becomes [3] now it checks base case, len is not 0,
# so it calculates newMin where minSoFar is 1 and l[0] is 3
# So newMin becomes 1 again, now again it calls recursion to l[1:]
# part of list where list becomes []
# Again it goes to base case where it checks if len is 0 or not, so len is 0
# and then it prints minSoFar which is 1 and it returns from there

#This is also a concept
