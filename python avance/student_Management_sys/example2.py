
class Product : 
    def __init__(self,name,price):
          self.name = name
          self.price = price



class VendingMachine: 
    def __init__(self,password):
        self.password = password
        self.items = []
        self.balance = 0
    def add_item(self,name,price,password):
        if(password != self.password):
            print("Incorrect Password")
        else : self.items.append(Product(name,price))
    def purchase_item(self,index,pay):
        if pay < self.items[index].price and self.:
            return (None,pay)
        else : 
            self.balance+=self.items[index].price
            return (self.items[index].name,pay-self.items[index].price)
    def __str__(self):
        # print(f"Vending Machine Balence : {self.balance}")
        # for i in range(len(self.items)):
        #     print(f"{self.items[i].name} : {self.items[i].price}")
        lines = []
        lines +=[f"\n{self.items[i].name} : {self.items[i].price}" for  i in range(len(self.items))]
        return f"Vending Machine Balence : {self.balance} $" +  "\n".join(lines)
    
    
march : VendingMachine = VendingMachine("1234")
march.add_item("bimo",1,"1234")
print(march)
rest=march.purchase_item(0,12)
print(f"\n{rest}\n")
print(march)