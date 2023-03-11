def dictionary():
    dictOne={"name":'mai',"age":23,"track":'iot'}
    newdict={}
    for key, value in dictOne.items():
        newdict[value]=key
    print("The new Dictionary : ",newdict)


dictionary()