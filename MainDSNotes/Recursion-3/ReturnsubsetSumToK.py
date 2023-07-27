def subSumToK(l, k):
    if len(l) == 1:
        if l[0] == k:
            output = [[k]]
        else:
            output = []
            return
    output1 = subSumToK(l[:-1],k)
    output2 = subSumToK(l[:-1], k - l[-1])
    for lst in output2:
        lst.append(l[-1])
    if l[-1] == k:
        output2.append([k])
    return output1 + output2

n = int(input())
l = [int(ele) for ele in input().split()]
k = int(input())
ans = subSumToK(l, k)
print(ans)


#input =
#9
#5 12 3 17 1 18 15 3 17
#6

#output
#3 3
#5 1