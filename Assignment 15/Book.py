class Book:
    def __init__(self, bid, bname, bprice, bauthor):
        self.id = bid
        self.name = bname
        self.price = bprice
        self.author = bauthor

    def display(self):
        print("bid", self.id)
        print("bname", self.name)
        print("bprice", self.price)
        print("bauthor", self.author)

    def __del__(self):
        pass

b1 = Book(111, "Wings of Fire", 500, "Dr. APJ Abdul Kalam")
b2 = Book(201, "Written in her name", 650, "Divyansh Shrimali")
b1.display()
print("###################")
b2.display()


        