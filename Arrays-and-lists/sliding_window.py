
def sub_array_with_sum(array, target):
    summ = 0
    results = []
    window_start = 0
    for window_end in range(len(array)):
        #add the current number
        summ+=array[window_end]
        
        if summ >= target:
            while summ > target and window_start < window_end:
                summ -=array[window_start]
                window_start+=1
                
            #if we found our target 
            if summ == target:
                results.append(window_start+1)
                results.append(window_end+1)
                return results
    return [-1]

array = [2,5,4,6,3,7,8,5]
target = 18

result=sub_array_with_sum(array, target)
print(" ".join(map(str, result))) 