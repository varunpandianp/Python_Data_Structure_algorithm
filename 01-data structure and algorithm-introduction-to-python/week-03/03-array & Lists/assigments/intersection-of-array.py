def commonElements(arr1, arr2):
    result = []

    for i in range(len(arr1)):

        for j in range(len(arr2)):

            if arr1[i] == arr2[j]:
                result.append(arr1[i])

    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

result = commonElements(arr1, arr2)

print(result)