def list():
    lst=[]
    sqlst=[]
    n=int(input("enter number of elements in the list: "))
    for i in range(0,n):
        ele=int(input("Enter elements of the list: "))
        lst.append(ele)
        
    for n in lst:
        sqlst.append(n*n)
    print(sqlst)
    
list()
        