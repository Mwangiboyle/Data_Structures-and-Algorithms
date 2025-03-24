'''The task of creating a prefix sum list in Python involves iterating over a sequence of numbers and calculating the cumulative sum at each index. 
For example, with a list of numbers a = [3, 4, 1, 7, 9, 1], the task is to compute the cumulative sum at each index,
resulting in a prefix sum list like [3, 7, 8, 15, 24, 25].
'''
array = [3,5,6,3,2,7,12]

new_array = []

sum = 0
for num in array:
    sum+=num
    new_array.append(sum)
print(new_array)