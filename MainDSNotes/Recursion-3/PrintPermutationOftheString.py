from itertools import permutations
def permutationsString(str):
    permList = permutations(str)

    for p in list(permList):
        print(''.join(p))
    return p

str = str(input())
permutationsString(str)


#input = abc
# output = abc
# acb
# bac
# bca
# cab
# cba