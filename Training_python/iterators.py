# a = ["hi", "dea", "how", "you"]

   

# itr = reversed(a)
# print(next(itr))


class RemoteControl:
    def __init__(self):
        self.channels=["cnn","zee","suvarna"]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1
        if self.channels==len(self.channels):
            raise StopIteration
    
        return self.channels[self.index]
    
r = RemoteControl()
itr = iter(r)
print(next(itr))