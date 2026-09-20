def pairSum(arr, n, X):

    count = 0

    for i in range(n):

        for j in range(i + 1, n):

            if arr[i] + arr[j] == X:
                count += 1

    return count


arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]

n = len(arr)

X = 7

result = pairSum(arr, n, X)

print(result)