lst1 = []
lst2 = []
n1 = int(input("enter number of elements in the first list: "))
for i in range(0, n1):
    ele1 = int(input("Enter elements of the first list: "))
    lst1.append(ele1)

n2 = int(input("enter number of elements in the second list: "))
for i in range(0, n2):
    ele2 = int(input("Enter elements of the second list: "))
    lst2.append(ele2)


def listOflists(*args):
    lst3 = []
    for arg in args:
        lst3 +=arg
    print(lst3)
    
listOflists(lst1,lst2)
    
