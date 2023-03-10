def newlist():
    lst=[]
    lstnew=[]
    n=int(input("enter number of elements in the list: "))
    for i in range(0,n):
        ele=int(input("Enter elements of the list: "))
        lst.append(ele)
    print("old list is :",lst)
    
    for i in lst:
        if (i%2==0):
            lstnew.append(i)
    print("New list is :",lstnew)
    
newlist()