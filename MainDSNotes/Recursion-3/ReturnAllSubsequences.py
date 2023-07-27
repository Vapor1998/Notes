from sys import setrecursionlimit
setrecursionlimit(11000)
def subS(s):
    n = len(s)
    if n == 0:              #1. base case where we check if string is empty or not,
                            # if yes, then we create output list where we append empty char
                            # and return output array
        output = []
        output.append('')
        return output
    smallerString = s[1:]           #2. Here we slice list
    smallerOutput = subS(smallerString)         #3. Here we find the subsequences of s[1:] using recursion (Induction Hypothesis)

    output = []                                 #4. Here, we create new output list
    for sub in smallerOutput:                   #5. Here we traverse smallerOutput and we append that output to the
        output.append(sub)                      # output list

    for sub in smallerOutput:                   #6. In this part we traverse to the smallerOutput and
        subs = s[0] + sub                       # store that to the same output list with s[0] appending to it
        output.append(subs)

    return output

print(subS('abc'))


# Dry Run of the Code

# Initially we pass the string 'abc'
# So it checks the base case if the len is 0 or not, if not then it moves to 2.
# In 2., we slice the list to s[1:], in which string becomes 'bc' and in 3, we calls to recursion which checks if the
# string is empty or not, string is not empty so we move to 2. which slice the list, in which list becomes 'c',
# then we calls to recursion, in which calls goes to 1. which checks base case, still string len is not 0, so we move to 2.
# Uptil now, the call has become like the following sequence ->: 'abc'->'bc'->'c'
# which slices the string, so string becomes empty i.e. ''.
# Now, we go to 3. where we calls recursion in which it goes to base case, this time, len is 0 so, call
# becomes 'abc'->'bc'->'c'->'' and base case executes.
# As per recursion, empty string is waiting for the smallerOutput of 'c','c' is waiting for 'bc', 'bc is
# waiting for 'abc'.
# Base case creates output list where it appends empty list and returns output.
# Now smallerOutput has recieved a list with empty string.
# Now in this, we go to 4. and create a new list and then we move to 5. where we traverse smallerOutput.
# Now for loop will append the sub of the smallerOutput to the output(4.) list.So there is nothing there in smallerOutput
# so it will move to 6. where the for loop will append content of smallerOutput with the s[0] which after recursion is 'c'.
# So the output list will become ['', 'c']. This is the output of 'c'.
# Now, 'bc' is going to receive output as ['','c'], copy them again, and then, appends zeroth character of the string.
# So, zeroth character here becomes b, which is appended according to 5. and then according to 6., it will append
# s[0] which is b and smallOutput which is 'c', which becomes 'bc'.
# So answer of 'bc' becomes ['', 'c', 'b', 'bc'].
# Now for abc, it copies answer of 'bc', and then appends zeroth character of
# the string which is 'a', So according to 6.
# output becomes ['', 'c', 'b, 'bc', a, 'ac', 'ab', 'abc']

# We can try for string 'abcd'


