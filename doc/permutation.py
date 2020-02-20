def perm(arr, i):
    if i == len(arr):
        print(arr)
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            perm(arr, i+1)
            arr[i], arr[j] = arr[j], arr[i] # swap back

perm([1, 2, 3], 0)