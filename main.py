def binary_search (arr: list, target: float) -> int:
   min = 0
   max = len(arr) - 1
   done = False
   while not done:
       i = int((min+max)/2)+1
       if arr[i] == target:
           return i
       elif arr[i] > target:
           max = i
       else:
           min = i
       if max == min and arr[min] != target:
           done = True
   return -1

def linear_search (arr: list, target: float) -> int:
    for i in len (arr):
        if arr[i] == target:
            return i
    return -1 

def merge_sort (arr: list) -> list:
    sorted = True
    for i in range (1, len(arr)):
        if arr[i] < arr[i-1]:
            sorted = False
    mid = int(len(arr)/2)
    if sorted:
        return arr
    else:
        a, b = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        c = []
        while a or b:
            if a and b:
                if a[0] < b[0]:
                    c.append(a.pop(0))
                else:
                    c.append(b.pop(0))
            elif a:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
        return c
