with open(r"example.txt",'r') as file:
    for line in reversed(list(file)):
        print(line.rsplit())
        