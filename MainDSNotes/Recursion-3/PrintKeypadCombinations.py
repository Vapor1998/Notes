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
        return 'mnop'
    if d == 7:
        return 'qrs'
    if d == 8:
        return 'tuv'
    if d == 9:
        return 'wxyz'

    return ' '

def keypad(n, outputSoFar):

    if n == 0:
        print(outputSoFar)
        return
    smallNo = n // 10
    lastDigit = n % 10

    string = getString(lastDigit)

    for c in string:
        newOutput = c + outputSoFar
        keypad(smallNo, newOutput)


n = int(input())
keypad(n, '')

# Dry Run