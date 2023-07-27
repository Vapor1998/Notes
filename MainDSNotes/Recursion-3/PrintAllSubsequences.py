def printSubs(s, output):
    if len(s) == 0:         #1. Base case, it checks if len(s) is 0 or not,
                            # If yes, then it prints output.
        print(output)
        return
    printSubs(s[1:], output)        #2. This will call recursion on s[1:] part of the string and in
                                    # parameter, it does not include s[0] part of string.

    newOutput = output + s[0]       # This part will add s[0] part of string to the output
    printSubs(s[1:], newOutput)     #3. This part will calls recursion on s[1:] part of the string
                                    # with s[0] part of the string included.

s = str(input())
printSubs(s, '')





# Dry Run
# First, we pass input string 'abc', where it checks the base case, if it is 0,
# it is not so it moves to 2. where it calls recursion on the s[1:] part of the string
# where it does not include s[0] part of the string
# Then string becomes 'bc',''.

# Then it again checks the base case, len is not 0, so it again goes to 2, where it calls
# recursion on s[1:] part of string where string becomes 'c',''.

# Then again it calls on base case where it checks len which is not 0, so
# it calls recursion again where it calls recursion on s[1:] part of string
# then string becomes '','' which is empty, so it goes to base case, where it checks if len is 0
# or not, it is 0, so it prints the output which is ''.
# Until now, the calls looks like 'abc'->'bc'->'c'->''.

# So after printing, call goes back to 'c', where it calls recursion  3.,( because 2. base case is
# completed), where it calls
# recursion on s[1:] part of string, so string becomes, '', now it returns output as s[0] + string
# where s[0] is c so, '' +'c' becomes c, and after checking base case, len is 0 after recursion,
# so it print output which is 'c'.

# Now, call goes back to 'bc' where it checks the base case which is not 0, so it
# calls on 3. where it calls recursion on s[1:] part of string, so string becomes, 'c','b' as it includes s[0].
# Now, it goes back and check the base case which is not 0, so it moves to the next line which calls 2.
# which calls recursion on s[1:] part of string in which string becomes '','b' as in 2.,
# it does not include s[0] part of the string, Now it goes back to the base case, where it checks the
# len which is 0, so it prints the output which is 'b'.(For note string representation '','' denotes
# s, output where s is string part of recursion and output denotes output part, which both updates after recursion)
# So the base case matches and it prints the output which is 'b'.

# Now it returns back to 'c','b', where it calls 3. in which s[0] is 'c'.Now, it calls
# recursion on s[1:] part of string where it becomes '','b'. After calling recursion, newOutput becomes 'bc'
# checks the base case if len is 0 or not, it is so it prints the output 'bc'.

# After then, it returns back to 'bc', it returns back to 'abc'.
# And then when 3. recursion is completed, it calls on 2. where it calls on s[1:], where string becomes 'bc' and output
# becomes 'a' where it includes s[0] part of string.
# Rest part is as same as the left subtree of recursion given below.





























# Recursion Tree
#                                               abc
#                                /                              \
#                               /                                \
#                              /                                  \
#                            bc, ''                                  bc, a
#                          /       \                               /        \
#                         /         \                             /          \
#                        /           \                           /            \
#                      c, ''         c,'b'                      c,'a'           c,'ab'
#                      /    \         /   \                     /   \              /    \
#                     /      \       /     \                   /     \            /      \
#                    /        \     /       \                 /       \          /        \
#                    '',''  '','c' '','b'   '',bc            '','a'   '','ac'   '','ab'   '','abc'
#
#
#
#
#
#
#
#
#