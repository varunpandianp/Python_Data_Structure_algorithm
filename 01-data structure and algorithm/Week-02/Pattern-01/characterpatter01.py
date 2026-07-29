# print kth alphabet
k = int(input())
# 'A' + k - 1
x = ord('A')
asciiTarget = x + k - 1
targetChar = chr(asciiTarget)
print(targetChar)