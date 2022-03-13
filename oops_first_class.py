class Laptop :
    def __init__(self , brand_name , model_no , color):
        self.brand_name = brand_name
        self.model_no = model_no
        self.color = color

laptop1 = Laptop("lanavo" , "ideapad330s", "grey")
print(laptop1.brand_name)
print(laptop1.model_no)
print(laptop1.color)


# class Student:
#     def __init__(self , name , age , roll_no , stu_class):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#         self.stu_class = stu_class

# student1 = Student("arun solanki" , 22 , 1896202816 , "xii th")

# print(student1.name)
# print(student1.stu_class)
# print(student1.roll_no)
# print(student1.age)
