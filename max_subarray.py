def max_subarray(arr):
    max_sum=0
    
    for i in range(0,len(arr)):
        current_sum=0
        for j in range (i,len(arr)):
            current_sum+=arr[j]
            max_sum=max(max_sum,current_sum)
        return max_sum

arr=[1,2,3,4,-2]
result=max_subarray(arr)
print(result)

#O(n^2)