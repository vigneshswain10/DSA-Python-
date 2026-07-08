def majority_element(elements):
    majority=0
    vote=0
    for i in range(0,len(elements)):
        if vote==0:
            majority=elements[i]
            vote+=1
        elif majority==elements[i]:
            vote+=1
        else:
            vote-=1
    return majority

elements=[2,1,1,2,1,2,2,2]
results=majority_element(elements)
print(results)