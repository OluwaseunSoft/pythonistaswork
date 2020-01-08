class Dog:
    def __init__(self, color, name, size, breed):
        self.color = color
        self.name = name
        self.size = size
        self.breed = breed

    def sit(self):
        print("My " + self.name + " is sitting")

    def bark(self):
        print("The name of my dog is " + self.name)

    def boom(self):
        print("The size of my dog is " + self.size)

    def international(self):
        print("The breed of my dog is " + self.breed)


my_dog = Dog("brown", "Jack", "Big", "Altasian")

my_dog.bark()
my_dog.sit()
my_dog.international()
my_dog.boom()
