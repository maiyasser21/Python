with open(r"example.txt",'r') as file:
    lines=file.read().split()
    print(max(lines,key=len))