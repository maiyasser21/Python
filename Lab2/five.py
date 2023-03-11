with open(r"example.txt",'r') as file:
    lines=len(file.readlines())
    print('Lines Count is : ',lines)