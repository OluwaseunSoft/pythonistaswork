class FirstClass:
        def __init__(self, age, name, height, weight):
            self.age = age
            self.name = name
            self.height = height
            self.weight = weight

        def howOld(self):
            print("I'm " + self.age + " years old")

        def callMe(self):
            print("My name is " + self.name)
        
        def iMtall(self):
            print("My height is " + self.height)

        def iMBig(self):
            print("My height is " + self.weight)  


class SecondClass:
        def __init__(self, state, country, city, home):
            self.state = state
            self.country = country
            self.city = city
            self.home = home

        def nationality(self):
            print("The name of my country is" + self.country)

        def urbanArea(self):
            print("I'm from " + self.city + "city")
        
        def address(self):
            print("I love working from " + self.home)

        def stateInCountry(self):
            print("I moved from a remote state to " + self.state)  

myfirst = FirstClass(34, "Paul", "45m", "89kg")
mysecond = SecondClass("Lagos", "Nigeria", "Ikeja", "Home")

myfirst.callMe()
mysecond.urbanArea()