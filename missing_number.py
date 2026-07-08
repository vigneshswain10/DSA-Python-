def missing_number(num):
    n=len(num)

    total_sum=n*(n+1)/2
    sum_num=sum(num)

    missing_element=total_sum-sum_num
    return missing_element

num=[0,1,2,3,5]
result=missing_number(num)
print(result)

    