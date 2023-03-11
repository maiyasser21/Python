def sumlist():
    sum=0
    lst=[]
    n=int(input("enter number of elements in the list: "))
    for i in range(0,n):
        ele=int(input("Enter elements of the list: "))
        lst.append(ele)
    
    for n in lst:
        if (n%2==0):
            sum+=n
    print ("The sum of even Numbers is : ",sum)
    
    
sumlist()