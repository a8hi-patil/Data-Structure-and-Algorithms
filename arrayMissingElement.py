def misEle(arr):
    flag = True
    if(len(arr) == 0):
        return "Array is empty"
    elif (len(arr)):
        start = arr[0]
        for i in range(1,len(arr)):
            if((start+1) == arr[i]):
                start = arr[i]
            else:
                flag = False
                return start +1
                
    if(flag):
        return "Nothing is missing"

    
    
ls = [1,2,3,4,6]
ms = [1,2,3,4,5]
ks = []
print(misEle(ls))
print(misEle(ms))
print(misEle(ks))
