with open('example.txt','r') as readfile, open ('copy.txt','a') as copyfile:
    for line in readfile:
        copyfile.write(line)
        
        