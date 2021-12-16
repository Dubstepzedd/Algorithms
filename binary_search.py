import random

#-- Binary Search --#

def binary_search_bool(lst : list, target : int,pred = lambda t,c : t > c) -> bool:    
    #Base cases
    #Is it empty? 
    if not lst:
        return False
    
    mid = len(lst) // 2

    current = lst[mid]
    
    #Are we on the correct element?
    if(current == target):
        return True
    
    #Is the target larger than our current element?    [ ... c ... t]
    if(pred(target,current)):
        new_lst = lst[mid+1:]
  
        return binary_search_bool(new_lst,target,pred)

    #Is the target smaller than our current element?    [t ... c ... ]
    else:
        new_lst = lst[:mid]
        
        return binary_search_bool(new_lst,target,pred)

    
def binary_search_index(lst : list, start : int, end : int,target : int,pred = lambda t,c : t > c) -> int:    
    #--Base cases--#

    #If start is bigger than end we return None as nothing was found
    if(start > end):
        return None

    mid = start + (end-start) // 2

    current = lst[mid]
    
    #Are we on the correct element?
    if(current == target):
        return mid
    
    #Is the target larger than our current element?    [ ... c ... t]
    if(pred(target,current)):

        return binary_search_index(lst,mid+1,end,target,pred)

    #Is the target smaller than our current element?    [t ... c ... ]
    else:   
       
        return binary_search_index(lst,start,mid-1,target,pred)


#Code
target = 99
lst =  [_ for _ in range(0,100)]
lst.sort()
#Add print
i = binary_search_index(lst,0,len(lst),target)
print("Index: ",i )
if(i is not None):  
    print(lst[i])
