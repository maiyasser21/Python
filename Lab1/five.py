def maxliststr():
    lst=[]
    count=0
    maxlst=[]
    n=int(input("enter number of elements in the list: "))
    for i in range(0,n):
        ele=input("Enter elements of the list: ")
        lst.append(ele)
    print(lst)
    for i in lst:
        count=0
        for x in i:
            count+=1
            maxlst.append(count)
    maxnumber=max(maxlst)
    print("max is :", maxnumber)
    
        
maxliststr()
    
    