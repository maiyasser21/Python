def swap(string, **kwargs):
    for value in kwargs.values():
        string+=value
    return string

print(swap("",name='mai',lastname='mohamed'))