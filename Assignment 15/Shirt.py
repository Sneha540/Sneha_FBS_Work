class Shirt:
    def __init__(self, sid, sname, sprice, stype, ssize):
        self.id = sid
        self.name = sname
        self.price = sprice
        self.type = stype
        self.size = ssize

    def display(self):
        print("sid", self.id)
        print("sname", self.name)
        print("sprice", self.price)
        print("stype", self.type)
        print("ssize", self.size)
        

    def __del__(self):
        pass

s1 = Shirt(101, "Roadstar", 600, "formal", "M")
s2 = Shirt(201, "Adidas", 500, "Partywear", "L")
s1.display()
print("###################")
s2.display()