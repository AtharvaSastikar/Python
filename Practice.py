

# ******List in Python********

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# thislist = list(("apple", "banana", "cherry"))
# print(thislist)

# print(thislist[1])

# thislist[1] = "blackcurrant"
# print(thislist)

# for x in thislist:
#     print(x)

# if "apple" in thislist:
#     print("Yes")

# print(len(thislist))

# thislist.append("orange")
# print(thislist)

# thislist.insert(1,"orange")
# print(thislist)

# thislist.remove("orange")
# print(thislist)

# thislist.pop()
# print(thislist)


# del thislist[0]
# print(thislist)


# thislist.clear()
# print(thislist)




# *********Set in Python**********

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# for  x in thisset:
#     print(x)

# print("banana" in thisset)

# thisset.add("orange")
# print(thisset)

# thisset.update(["orange","mango","grapes"])
# print(thisset)

# print(len(thisset))

# thisset.remove("banana")
# print(thisset)

# thisset.discard("orange")
# print(thisset)

# print(thisset.pop())

# print(thisset.clear())

# del thisset

# print(thisset)





# *********Dictionary in python********** 


# thisdict = {
#     "brand":"Ford",
#     "model":"Mustang",
#     "year" : 1964
# }

# x = thisdict["model"]
# print(x)


# thisdict["year"] = 2000
# print(thisdict)

# for x in thisdict:
#     print(x)

# for x in thisdict:
#     print(thisdict[x])

# # for x in thisdict.values():
#     # print(x)

# for x,y in thisdict.items():
#     print(x,":",y)


# if  "model" in thisdict:
#     print("Yes, 'model' is one of the keys.")


# print(len(thisdict))

# thisdict["color"] = "red"
# print( thisdict)

# thisdict.pop("model")
# print(thisdict)

# thisdict.clear()
# print(thisdict)

# thisdict= dict(brand = "Ford",model = "Mustang",year=1964)
# print(thisdict)




# ******** String in Python **************
# a = "  Hello, World!  "
# print(a[1])  #printing string value at the given index

# print(a[2:5]) ##printing multiple values at the given indices
#              # This will print string values at 2,3,4

# print(a)
# print(a.strip()) #To remove whitespaces at start and end

# print(len(a))  #returns length of string

# print(a.lower())  #converts string to lower case
# print(a.upper())  #converts string to upper case

# print(a.replace("H","J")) #replaces givwn atring value with other string value

# print(a.split(",")) #splits the string from the given string value



#***** If-else in Python**********



# a = 33
# b = 200

# #  if statement
# if b > a:
#     print("b is greater than a")

# # if-elif statement
# if b > a :
#     print("b is greater than a")

# elif a == b:
#     print("a and b are equal..")

# # if-elif-else statement

# if b > a :
#     print("b is greater than a")

# elif a == b:
#     print("a and b are equal..")

# else:
#     print("a is greater thn b")

# #Short Hand If
# a = 200 ; b = 33

# if a > b: print("a is greater than b")

# #Short hand if-else

# print("A")if a > b else print("B")


# # and keyword

# a = 200; b = 33; c = 500

# if a>b and c>a :
#     print("C is greater")


# # or keyword

# if a>b or a>c:
#     print("a is greater than at least one ")





# ***** While Loop in Python *******


# while loop

# i = 1
# while i < 6 :
#     print(i)
#     i += 1

# #break statement in while

# i = 1
# while i < 6:
#     print(i)
#     if(i==3):
#         break
#     i+=1


# #continue statement in while

# i = 0
# while i <6:
#     i = i+1
#     if i ==3:
#         continue
#     print(i)


# ******* For Loop in Python********

#for loop

# fruits=["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# #loop through the string

# for x in "banana":
#     print(x)

# #break in for loop

# for x in fruits:
#     print (x)
#     if(x=="banana"):
#         break

# #continue in for loop

# for x in fruits:
#     if x == "banana":
#         continue

# for x in range(10):
#     print(x)

# #using else in for loop

# for x in range(6):
#     print(x)
# else:
#     print("Finally Finished")

# #Nested for loop

# adj=["red","big","tasty"]
# fruits=["apple","banana","cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

 

# ***** Functions in Python *******


# Creating and calling a function

# def my_function():
#     print("Hello from a function...")

# my_function()


#Function using Parameters

# def my_function(fname):
#     print(fname+" details")
# my_function("Email")
# my_function("Calling")
# my_function("Address")


# # Using default Parameters

# def my_function(country="Norway"):
#     print("I am from "+country)

# my_function("India")
# my_function()


# # Returning a value using function

# def my_function(x):
#     return 5 * x

# print(my_function(3))
# print(my_function(5))



# #Recursion

# def tri_recursion(k=1):
#     if(k > 0):
#         result  = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
    
# print("\n\n Results")
# tri_recursion(5)



# Accepting input from user

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(f"Hello {name}")
# print(f"You are {age} years old")

# ****** Mad Lib *********

# adjective1 = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# adjective2 = input("Enter an adjective: ")
# verb = input("Enter a verb: ")
# adjective3 = input("Enter an adjective: ")

# print(f"Today I went to a {adjective1} park.")
# print(f"In the park I saw {noun}")
# print(f"{noun} was {adjective2} and {verb}")
# print(f"I was {adjective3}")


# ******** Area of Rectangle ********

# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# height = int(input("Enter the height: "))

# area = length * width * height
# print(f"The area of rectangle is {area}")


#  ******** Shopping Cart ********


# item=(input("What item would you like to buy? : "))
# price = float(input("What is the price? :"))
# quantity = int(input("How many would you like? : "))


# total = price * quantity


# print(f"You have bought {quantity} x {item}")
# print(f"Your total is {total,2}")


# Maths needed in python

# x = 3.14; y = 4; z = 5

# # Rounding off the value

# result = round(x)
# print(result)


# #Distance from 0 considering value as whole number
# y = -4
# result = abs(y)
# print(result)


# # Number to the power of given value
# result = pow(z,3)
# print(result)

# # Maximum value out of three
# result = max(x,y,z)
# print(result)

# # Minimum value out of three
# result = min(x,y,z)
# print(result)


# # *** Math Class ***
# import math

# print(math.pi)
# print(math.e)
# print(math.sqrt(25))
# print(math.ceil(9.1))
# print(math.floor(9.9 ))


# radius = float(input("Enter the radius of circle: "))

# circumference = 2 * math.pi * radius
# area = math.pi * pow(radius,2)
# print(f"The circumfrence is {round(circumference,2)}cm^2")
# print(f"The area is {round(area,2)}cm^2")



# ******* Calculator *********

# operator = input("Enter an operator(+ - * /): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter the second number: "))


# if operator == "+":
#     result = num1+num2
#     print(round(result,2))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result,2))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result,2))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result,2))
# else:
#     print("Invalid Input")


# ****** Weight Converter *******

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds?(K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"Your weight is {round(weight,2)} {unit}")
# elif unit == "L":
#     weight = weight/2.205
#     unit = "Kgs"
#     print(f"Your weight is {round(weight,2)} {unit}")
# else:
#     print(f"{unit} was not valid")



# ******* Temprature Conversion ********


# unit = input("Is the temprature in Celsius of Farenheit(C/F): ")
# temp = float(input("Enter the temprature: "))

# if unit == "C":
#     temp = round((9*temp)/5 +32, 2)
#     print(f"The temprature in Farenheit is: {temp}F")
# elif unit == "F":
#     temp = round((temp-32)*5/9, 2)
#     print(f"the temprature in celsius is {temp}C")
# else:
#     print(f"{unit} is an invalid unit of measurement")



# ******* and || or || not

# temp = 25
# sunny = True
# if temp > 0 and temp < 30:
#     print("Temprature is good.")
# else:
#     print("Temprature is bad..")


# temp2 = 50
# if temp2 < 0 or temp2 > 30:
#     print("Temprature is bad.")
# else:
#     print("Temprature is good.")

# if not sunny:
#     print("It is cloudy outside.")
# else:
#     print("It is sunny outside.")


#   ******String functions in Python*********

# number = input("Enter Your Phone_Number: ")
# result = len(name)
# result = name.find("o")
# print(result)
# result = name.rfind("q")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# print(name)
# result = name.isalpha()
# result = number.count("-")
# result = number.replace("-"," ")
# print(result)



# ****** If else in Python *******

# username = input("Enter a username: ")

# if len(username) > 12:
#     print("Your username can't be more than 12 characters..")
# elif not (username.find(" ") == -1):
#     print("The username can't have spaces..")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome: {username}")



# ******** indexing in python ********

# indexing = accessing elements of a sequence using [] (indexing operator)
#  [star : end : step]


# credit_number = "1234-5678-9012-3456"
# last_digits = credit_number[-4:]
# # print(credit_number[0])
# # print(credit_number[:4])
# # print(credit_number[5:9])
# # print(credit_number[5:])
# # print(credit_number[-1])
# # print(credit_number[::2])
# # print(f"xxxx-xxxx-xxxx-{last_digits}")
# email = input("Enter Your email: ")
# index = email.index("@")
# username = email[:index]
# domain = email[index +1:]

# print(f"Your username is {username} and domain is {domain}")





# **** Format Specifiers in Python ********

# price1 = 3000.14159
# price2 = -98700.65
# price3 = 1200.34

#Formats upto two decimal points
# print(f"Price 1 is ${price1: .2f}")
# print(f"Price 2 is ${price2: .2f}")
# print(f"Price 3 is ${price3: .2f}")

#Formats upto three decimal points
# print(f"Price 1 is ${price1: .3f}")
# print(f"Price 2 is ${price2: .3f}")
# print(f"Price 3 is ${price3: .3f}")

#adds zero preceeding and places the number such that it ends on 10th index
# print(f"Price 1 is ${price1: 010}")
# print(f"Price 2 is ${price2: 010}")
# print(f"Price 3 is ${price3: 010}")


#number ends on 10th index
# print(f"Price 1 is ${price1: 10}")
# print(f"Price 2 is ${price2: 10}")
# print(f"Price 3 is ${price3: 10}")

# shifts the number to leftmost index
# print(f"Price 1 is ${price1: <10}")
# print(f"Price 2 is ${price2: <10}")
# print(f"Price 3 is ${price3: <10}")

# print(f"Price 1 is ${price1: ^10}")
# print(f"Price 2 is ${price2: ^10}")
# print(f"Price 3 is ${price3: ^10}")

# Adds positive or negative sign before the number
# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")


#Adds commas to thousand'th places
# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")




# ******* While Loop In Python *********



# name = input("Enter your name: ")
# while name=="":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")



# age = int(input("Enter your age: "))
# while age<0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"Your age is {age}")



# food = input("enter your favourite food: ")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter your favourite food: ")
# print("Bye")


# num = int(input("Enter a number between 1-10: "))
# while num < 1 or num >10:
#     print("Num is not valid")
#     num = int(input("Enter a number between 1-10: "))

# print(f"Your number is {num}")


# ********  COMPOUND INTEREST CALCULATOR *********


# principle = 0
# rate = 0
# time = 0

# while principle <= 0 :
#     principle = float(input("Enter the principle amount:"))
#     if principle <= 0:
#             print("Your principle can't be zero")

# while rate <= 0 :
#     rate = float(input("Enter the rate :"))
#     if rate <= 0:
#             print("Your rate can't be zero")

# while time <= 0 :
#     time = float(input("Enter the time :"))
#     if time <= 0:
#             print("Your time can't be zero")

# total = principle * pow((1 + rate/100),time)
# # print(principle)
# # print(rate)
# # print(time)
# print(f"Balance after {time} years is {total}")

# ****** Including Zero *******
# principle = 0
# rate = 0
# time = 0

# while True :
#     principle = float(input("Enter the principle amount:"))
#     if principle < 0:
#             print("Your principle can't be zero")
#     else : break
# while True:
#     rate = float(input("Enter the rate :"))
#     if rate < 0:
#             print("Your rate can't be zero")
#     else : break

# while True :
#     time = float(input("Enter the time :"))
#     if time < 0:
#             print("Your time can't be zero")
#     else : break
# total = principle * pow((1 + rate/100),time)
# # print(principle)
# # print(rate)
# # print(time)
# print(f"Balance after {time} years is {total: .2f}")




# ******* For loop in Python ********


# for x in range(1,11):
    # print(x)


# for x in reversed(range(1,11)):
#     print(x)

# for x in range(1,11,2):
#     print(x)

# credit_card = "1234-5678-9874-6569"
# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x == 13:
#         continue
#     else:
#         print(x)


# for x in range(1,21):
#     if x == 13:
#         break
#     else:
#         print(x)




# ****** Nested Loops *********

# for x in range(3):
#     for y in range(1,10):
#         print(y,end = "")
#     print()

# ****** Rows and Column Pattern ********

# rows = int(input('Enter number of rows: '))
# columns = int(input('Enter number of coloumns: '))
# symbol = input("Enter symbol: ")


# for x in range(rows):
#     for y in range(columns):
#         print(symbol,end = "")
#     print()



# ******** Countdown Timer **********

# import time

# my_time = int(input("Enter the time in Seconds:"))

# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = (int(x/3600))
#     print(f"{hours}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!!")



# ***** Collection in Python: List[], Set{}, Tuple() ********
    # List = [] ordered and changeable. Duplicates OK
    # Set  = {} unordered and immutable, but Add/Remove OK. NO duplicates
    # Tuple = () ordered and unchangeable. Duplicates OK. Faster


    #List

# fruits=["apple", "orange", "banana", "coconut"]
# # print(dir(fruits))
# # print(help(fruits))
# print(len(fruits))
# # fruits[0] = "pineapple"

# fruits.append("pineapple")
# fruits.remove("apple")
# print(fruits)
# fruits.insert(0, "grapes")
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# print(fruits.index("grapes"))
# print(fruits.count("grapes"))

#Set
# fruits={"apple", "orange", "banana", "coconut"}
# print(fruits)
# #cannot use index method
# # cannot change the elements but we can add or remove elements

# fruits.add("pineapple")

# fruits.remove("apple")
# print(fruits)


# Tuple
# fruits=("apple", "orange", "banana", "coconut","coconut")
# print(fruits.count("coconut"))

# Dictionary

# capitals = { "USA" : "Washington D.C",
#              "India": "New Delhi",
#              "China": "Beijing",
#              "Russia": "Moscow"
#            }
# print(capitals.get("India"))
# if (capitals.get("Japan")) :
    # print("This capital exists..")
# else:
    # print("This capital doesn't exist..")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "California"})
# print(capitals)
# capitals.pop("China")

# print(capitals.popitem())
# print(capitals)

# print(capitals.keys())
# print(capitals.values())
# items = capitals.items()
# print(items)
# for key,value in capitals.items():
#     print(f"{key}:{value}")



# ******* Food Cart Program *******



# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy(q to quit):" )
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("------ YOUR CART ------")


# for food in foods:
#     print(food)
# for price in prices:
#     total += price

# print(f"Your total is: ${total}")

# ****** Functions in Python *******


# ***Positional arguments***

# def happy_birthday(name,age):
#     print(f"Happy Birthday to {name}")
#     print(f"You are {age} years old.")
#     print("Happy Birthday to you!!")
#     print()
# happy_birthday("Sonu",25)
# happy_birthday("Monu",30)
# happy_birthday("Vinu",30)


# ***Default arguments***


# Here discount and tax values are set default 
# If we specify values then our values are selected


# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price*(1-discount)*(1-tax)

# print(net_price(500))

# import time

# def count(end,start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!!")

# count(30, 15)


# *** Keywords arguments ***


# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"


# phone_num = get_phone(country=1, area = 123, first=456, last=7890)
# print(phone_num)



# *** Arbitary Arguments ***


# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3))

# # *args = allows to pass multiple non-key arguments
# # **kwargs = allows to pass multiple keyword arguments
# # * unpacking parameter


# def address(**kwargs):
#         for key, value in kwargs.items():
#              print(f"{key} : {value}")
  

# address(street= "SV Road",city="Mumbai",state="Maharashtra",zip="400068")\




# ***** Modules in Python *********

# print(help("modules"))

# import Mymodule

# result = Mymodule.pi

# print(result)

# result = Mymodule.square(19)
# print(result)
# result = Mymodule.cube(5)
# print(result)
# result = Mymodule.circumference(7)
# print(result)
# result = Mymodule.area(7)
# print(result)


# ******* Scope Resolution in Python *******


# scope resolution = Local -> Encolsed -> Global -> Built-in

# def func1():
#     x = 1
#     print(x)

# def func2():
# #    x = 2
#     print(x)
# x = 5
# func1()
# func2()

