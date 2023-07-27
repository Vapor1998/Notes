def printSubsets(l, output):
    if len(l) == 0:
        print(output)
        return
    printSubsets(l[1:], output)
    newOutput  = output, l[0]
    printSubsets(l[1:], newOutput)

n = int(input())
l = [int(ele) for ele in input().split()]
output = ''
printSubsets(l)





#input =
#3
#15 20 12

#output =
#[] (this just represents an empty array, don't worry about the square brackets)
#12
#20
#20 12
#15
#15 12
#15 20
#15 20 12