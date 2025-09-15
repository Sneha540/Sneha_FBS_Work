class Product:
    def __init__(self, pid, pname, pprice, pquantity):
        self.id = pid
        self.name = pname
        self.price = pprice
        self.quantity = pquantity

    def display(self):
        print("pid", self.id)
        print("pname", self.name)
        print("pprice", self.price)
        print("pquantity", self.quantity)

    def __del__(self):
        pass

p1 = Product(200, "Refrigerator", 40000, 1)
p2 = Product(201, "AC", 60000, 2)
p1.display()
print("###################")
p2.display()



    