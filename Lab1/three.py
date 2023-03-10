def maxlist():
    lst=[]
    n=int(input("enter number of elements in the list: "))
    for i in range(0,n):
        ele=int(input("Enter elements of the list: "))
        lst.append(ele)
        
    maxoflist=max(lst)    
    print("max of the list is: ", maxoflist)
    
maxlist()
    
    