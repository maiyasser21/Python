def stringvowels():
    x=input("Enter a string:")
    lst=['a','e','o','u','i']
    count=0
    for i in x:
        if i in lst:
            count+=1
    print(count)

stringvowels()