#  object = A "bundle of related attributes (variables) and methods (functions)"
#  class = (blueprint) used to design the structure and layout of an object


# from Mymodule import Car

# car1 = Car("Mustang", 2024, "red", False)
# car2 = Car("Fortuner",2024,"black",True)
# car3 = Car("Harrier",2024,"black",True)


# print(car3.model, end = " ")
# print(car3.year, end = " ")
# print(car3.color, end = " ")
# print(car3.for_sale, end = " ")
# print()

# car3.drive()
# car3.stop()


# print(car2.model, end = " ")
# print(car2.year, end = " ")
# print(car2.color, end = " ")
# print(car2.for_sale, end = " ")
# print()
# car2.drive()
# car2.stop()


# print(car1.model, end = " ")
# print(car1.year, end = " ")
# print(car1.color, end = " ")
# print(car1.for_sale, end = " ")
# print()
# car1.drive()
# car1.stop()



# ****** Class Variables and Object Variables ******



# class Student:
#     class_year = 2025 #Class Variable
#     num_students = 0 #Class Variable

#     def __init__(self, name, age):
#         self.name = name #object variables
#         self.age = age  #object variables
#         Student.num_students += 1


# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)
# student3 = Student('Squiward', 55)
# student4 = Student("Sandy", 27)

# # print(student1.name)
# # print(student1.age)
# # print(Student.class_year)
# # print()
# # print(student2.name)
# # print(student2.age)
# # print(Student.class_year)

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students:")
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)




# ****** Inheritance ******


# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.isalive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")



# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass


# class Mouse(Animal):
#     pass

    


# dog = Dog("Scooby")
# cat = Cat("Tom")
# mouse = Mouse("Jerry")

# print(dog.isalive)
# dog.eat()
# dog.sleep()
# print()

# cat.eat()
# cat.sleep()
# print()

# mouse.eat()
# mouse.sleep()

# **** Multiple Inheritance ****


# class Prey:
#     def flee(self):
#         print("This animal is fleeing")
    
# class Predator:
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):

#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.flee()#Fish is inheriting Prey as wll as Predator class
# fish.hunt()


# ****** Multilevel Inheritance ******

class Mammals():
     def __init__ (self,name):
        self.name = name
     def injury(self):
        print(f"{self.name} is injured.. ")

# Mammals class is inherited by Animal class
    
class Animal(Mammals):
   
    def eat(self):
        print(f"{self.name} is eating")

        # Animal class is inherited by Prey and Predator class
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
    
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
# Prey and Predator classes are inherited by Rabbit, Hawk, Fish class
class Rabbit(Prey):

    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Alex")
fish = Fish("Nimo")

rabbit.flee()
hawk.hunt()
fish.flee()#Fish is inheriting Prey as wll as Predator class
fish.hunt()
rabbit.injury() 