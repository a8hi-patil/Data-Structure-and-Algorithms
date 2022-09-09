def removeDuplicate(arr):
    if(not len(arr)):
        return "Array is empty"
    return list(set(arr))
    

ls= [1,2,3,3,5,6,3,7,8,9,9]
ks=[]

print(removeDuplicate(ls))
print(removeDuplicate(ks))
