
with open(r"example.txt",'r') as file:
   
    print(file.read().replace("\n"," "))