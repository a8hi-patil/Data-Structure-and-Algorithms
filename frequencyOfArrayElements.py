# Find the frequency of elements in an Array?
# Sample input =[1,3,3,4,2,3,6,6,1,0,9]
# Output=> 1= 2times;
# 	      3= 3times;
#                 4= 1 times;
#                 2= 1times;
#                 6 = 2times;
#                 0= 1times;
#                 9= 1times;


def counter(arr):
    arr.sort()
    counter = 1
    for i in range(0,len(arr)):
        if(i==len(arr)-1):
            print(f"{arr[i]} : {counter} times" )
            break
        if arr[i] == arr[i+1]:
            counter = counter +1
        else:
            print(f"{arr[i]} : {counter} times" )
            counter = 1
    
ls = [1,3,3,4,2,3,6,6,1,0,9]

counter(ls)
