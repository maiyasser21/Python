def stringSort():
    lst=[]
   
    x=int(input("Enter Number of elements: "))
    for i in range(0,x):
        ele=input("Enter elements of the list: ")
        lst.append(ele)
    print("Old list: ")
    print(lst)
    lst.sort()
    print("Sorted list: ")
    print(lst)
    
    
    
    
            
    
    
    
stringSort()