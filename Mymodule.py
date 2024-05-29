# pi = 3.1459

# def square(x):
#     return x**2

# def cube(x):
#     return x**3

# def circumference(radius):
#     return 2 * pi* radius

# def area(radius):
#     return pi * radius ** 2

class Car:
    def __init__(self, model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def drive(self):
        print(f"You drive the {self.year} {self.color}  {self.model}..")

    
    def stop(self):
        print(f"You stop the  {self.year} {self.color} {self.model}..")