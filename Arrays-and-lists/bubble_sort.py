
arr= [7,3,12,5,78,67,15,6]

n = len(arr)

for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
        swapped=True
    if not swapped:
        break
print(arr)