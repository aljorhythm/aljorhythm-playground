
l = list(map(int, "123125423890467"))
a = l.copy()
a.sort()

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quicksort(a, s, e, depth=0):
    print("qs", s, e)
    if s >= e:
        return

    p = partition(a, s, e)
    
    print("\t" * depth, p, a)
    #$,"partitioned", a, s, e, p)
    # print("quicksort left", a, s, p-1)
    quicksort(a, s, p - 1, depth+1)
    # print("quicksort right", a, p+1, e)
    quicksort(a, p + 1, e,depth+1)
    # print("after", a)

quicksort(l, 0, len(l) - 1)
print(l == a)
print(l)