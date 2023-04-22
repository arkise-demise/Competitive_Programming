def pivot_place(list1,first,last):
      pivot=list1[first]
      left=first+1
      right=last
      while True:
            while left<=right and list1[left]<=pivot:
                  left+=1
            while left<=right and list1[right]>=pivot:
                  right-=1
            if right<left:
                  break
            else:
                  list1[left],list1[right]=list1[right],list1[left]
      list1[first],list1[right]=list1[right],list1[first]
      return right
def Quicksort(list1,first,last):
      if first<last:
            p=pivot_place(list1,first,last)
            Quicksort(list1,first,p-1)
            Quicksort(list1,p+1,last)
list1=[56,26,93,17,31,44]
n=len(list1)
Quicksort(list1,0,n-1)
print(list1)