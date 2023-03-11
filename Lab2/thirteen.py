def list():
    lst=[]
    n=int(input("enter number of elements in the list: "))
    for i in range(0,n):
        ele=int(input("Enter elements of the list: "))
        lst.append(ele)
    
    
    largestItem=lst[0]
    smallestItem=lst[0]
    for n in lst:
        if (n>largestItem):
            largestItem=n
            print("The largest item is :", largestItem)
            
    for n in lst:
        if (n<smallestItem):
            smallestItem=n
            print("The smallest item is :",smallestItem)
            
    
list()
    
    
    

        