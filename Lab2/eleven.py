def stringlist():
    lst = []
    newlst = []
    n = int(input("enter number of elements in the list: "))
    for i in range(0, n):
        ele = (input("Enter elements of the list: "))
        lst.append(ele)

    for n in lst:
        if n.startswith('a') or n.startswith('A'):
            newlst.append(n)
    print(newlst)
    

stringlist()