def fact(n):
    if n == 0:
        return 1
    output = fact(n-1)
    return n * output


# Above example is where we return the output  after calculating the result
# In the above program, we passed 3 which accoding to base case is not 9, so it will execute the next
# line where it will calls recursion, and it again return 2 which is not 0, so it will pass recursion again
# This time, it becomes 1, so it will call recursion again in next line , this time n becomes 0, so it will return 1.
# Now, as it returns back to 1, it multiplies with 1, and becomes 1, and in the next case, it multiplies with 2, and
# then with 3, so the output becomes 6.

# Now instead of returning, we have to print the output instead of returning it.
# So far in the previous prob, we are passing the answer till the base case and it is returning the answer.
# Now, we have to pass the answer to the base case and print it from the base case.
# Below is the code of it.

def printFact(n, ans):
    if n == 0:
        print(ans)
        return
    ans = ans * n
    printFact(n-1, ans)

printFact(5, 1)

# Dry run of printFact()
# First, the argument passed is 5, 1. It will check whether n is 0 or not, it is not so it will multiply n
# with ans which is  5 * 1.
# So ans becomes 5, and it calls recursion to n-1, where n becomes 4, it will go to the base case where it
# will check if n ==0 or not, it is not so it will multiply n with ans where ans becomes 4 * 5 = 20,
# So ans becomes 20 and recursion is called where n becomes 3, now, it goes to base case which
# checks whether n is 0 or not,
# it is not so it multiplies n with ans where it becomes n * ans which is 3 * 20 which is 60.
# So ans becomes 60 and it calls recursion to 2, following the same procedure, it checks the base case where it fails
# and then it multiplies ans with n where it becomes 2 * 60 which is 120.
# Now it calls recursion where n becomes 1.
# It checks the base case where it checks whether n is 0 or not, it is not so it multiplies n with ans which is
# n * ans which becomes 1 * 120 which is 120
# Now ans in the argument is 120. It again calls recursion where n becomes 0.
# Now it checks base case and this time n is 0, so it executes the base case where
# it print the ans which is 120 and returns.
# This function is concept

