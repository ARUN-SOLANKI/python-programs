class Laptops:
    discount = 10
    def __init__(self , lp_name , lp_model , lp_color , lp_price) :
        self.lp_name  = lp_name
        self.lp_model = lp_model 
        self.lp_color = lp_color 
        self.lp_price = lp_price
    def lp_discount(self):
        return f" discount is {(Laptops.discount/100)*self.lp_price} \n final prize is {self.lp_price - (Laptops.discount/100)*self.lp_price} \n {self.__dict__}"


# Laptops.discount = 5

hp_laptop = Laptops("hp","hp323322a","black",100000) 
dell_laptop = Laptops("dell","del322d","sea blue",80000)
lenovo_laptop = Laptops("lenovo","ideapad330s","grey",50000)
hcl_laptop = Laptops("hcl","hp323322a","black",200000)
samsung_laptop = Laptops("samsung","hp323322a","navy blue",40000)

# print(hp_laptop.lp_discount())
# print("\n\n")
# print(dell_laptop.lp_discount())
# print("\n\n")
print(lenovo_laptop.lp_discount())
# print("\n\n")
# print(hcl_laptop.lp_discount())
# print("\n\n")
# print(samsung_laptop.lp_discount())
