def subset(arr,k):
    n=len(arr)
    if n == 1:
        if arr[0]==k:
            output = [ [k] ]
            return output
        else:
            output = []
            return output

    output1 = subset(arr[:-1], k)
    output2 = subset(arr[:-1], k - arr[-1])

    for lst in output2:
        lst.append(arr[-1])

    if arr[-1] == k:
        output2.append([k])

    return output1 + output2

print(subset([2,3,4,3], 6))
