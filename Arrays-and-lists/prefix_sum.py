array = [3,5,6,3,2,7,12]

new_array = []

sum = 0
for num in array:
    sum+=num
    new_array.append(sum)
print(new_array)