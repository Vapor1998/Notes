def getString(d):
    if d == 2:
        return 'abc'
    if d == 3:
        return 'def'
    if d == 4:
        return 'ghi'
    if d == 5:
        return 'jkl'
    if d == 6:
        return 'mno'
    if d == 7:
        return 'pqrs'
    if d == 8:
        return 'tuv'
    if d == 9:
        return 'wxyz'

    return ' '


def keypad(n):
    if n == 0:                  #1. Base case, if n becomes 0, it will create an output
                                # array and append an empty string to it

        output = []
        output.append('')
        return output

    smallerNumber = n // 10    #2. This will divide the input by 10, and gives integer part
    lastDigit = n % 10         #3. This will give us the last digit of n. i.e remainder part of n
    smallerOutput = keypad(smallerNumber)     #4. This will call recursion on the smallerNumber i.e on the 2. part
    options = getString(lastDigit)      #5. This will get the string from the getString()
    output = []                         #6. This will create an output array


    for s in smallerOutput:         #7. This will iterate over smallOutput which is obtained from keypad()
        for c in options:           # This will iterate over options which is obtained from getStrings()
            option = s + c          # This will add both the characters and
            output.append(option)   # this will append it to the output list

    return output

n = int(input())
ans = keypad(n)
print(ans)


# Dry Run

# Same as subsequences, 237 will calls on 23 according to 2., 23 calls on 2, 2 calls on 0.
# Now 0 will match the base case and it will return ['']
# Now actual calls looks like 237 -> 23 -> 2 -> 0.
# 0 returns [''] and moving to 7. smallerOutput is [''] and its last digit is also 0 so it is the output
# Now calls come back to 2, where it is the smallerOutput as well as the last number, it will add ['a', 'b', 'c']
# Now call comes back to 23, where 3 is the last no, it will append alphabets of 2 & 3 according to 7
# So call becomes ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
# Following the same cycle, this is the output of 23, so call goes to 237 where 7 is the last no
# So according to 7, it has to append 7 along with 23, so output becomes ['adq', 'adr', 'ads', 'aeq', 'aer', 'aes',
# 'afq', 'afr', 'afs', 'bdq', 'bdr', 'bds', 'beq', 'ber', 'bes', 'bfq',
# 'bfr', 'bfs', 'cdq', 'cdr', 'cds', 'ceq', 'cer', 'ces', 'cfq', 'cfr', 'cfs'].











# Base case: if 0, return -> ['']
# smallInput = input//10
# remaining digit = input % 10
# smallOutput = call recursion i.e. -> getComb(smallerInput)
# output =[]
# after creating new array, append smallOutput in it
