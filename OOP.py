# the main concept of oop are class object inheritance polymorphism abstraction incapsulation
#class is basic template for creating objects in python we use def keyword for class
# syntax class employee:
# objects are run time entities
# obj=myclass() is for creating objects
# inheritance is for code reuseability
# abstraction means only shoe essential information ton user (_ for abstraction)

#code 1
class programmer:
    company="microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_info(self):
        print(f"the {self.name} is working in {self.company} and his salary is {self.salary}")
satyam=programmer("satyam",90000)
diksha=programmer("diksha",90000)
satyam.get_info()
diksha.get_info()
#code 2

class square:
    def __init__(self,num):
        self.num=num
    def squaree(self):
        return self.num*self.num
sqr=square(8)
print(sqr.squaree())

@staticmethod
def greet():
    print("good to see you")

# inheritance 
class Animal:
    def __init__(self,name,legs,horns):
        self.name=name
        self.legs = legs
        self.horns=horns

class Pets(Animal):
    def pets(self):
        print(self.name,self.legs,self.horns)

class Dog(Pets):
    @classmethod
    def bark(cls):
        print("dog is barking")

# example showing use of super()
class Mammal(Dog):
    def __init__(self, name, legs, horns, has_fur=True):
        super().__init__(name, legs, horns)  # calls Animal.__init__ via the MRO
        self.has_fur = has_fur

    def show(self):
        print(f"{self.name}: legs={self.legs}, horns={self.horns}, has_fur={self.has_fur}")

mamal = Mammal("Lion", 4, 0)
mamal.show()
mamal.pets()
mamal.bark()

# polymorphism
# polymorphism means many forms
# method overloading means same method name with different parameters
# method overriding means same method name in parent and child class
# operator overloading means same operator with different data types
# polymorphism with function

def add(a,b):
    return a+b
print(add(5,6))
print(add("satyam ","panwar"))
print(add([1,2],[3,4]))
print(add((1,2),(3,4)))
print(add(5.5,6.5))
print(add(5+6j,6+7j))
print(add(True,False))

print(add(b"hello ",b"world"))
# polymorphism with class
# example of polymorphism with class
class Bird:
    def intro(self):
        print("all birds can fly")
    def fly(self):
        print("some bird can not fly")
class Sparrow(Bird):
    def fly(self):
        print("sparrow can also fly")
class Ostrich(Bird):
    def fly(self):
        print("ostrich can not fly")
        
bird=Bird()
sparrow=Sparrow()
ostrich=Ostrich()
bird.intro()
bird.fly()
sparrow.intro()
sparrow.fly()
ostrich.intro()
ostrich.fly()
# polymorphism with class without inheritance
class Bird:
    def intro(self):
        print("all birds can fly")
    def fly(self):
        print("some bird can not fly")

class Sparrow:
    def fly(self):
        print("sparrow can also fly")
class Ostrich:
    def fly(self):
        print("ostrich can not fly")
bird=Bird()
sparrow=Sparrow()
ostrich=Ostrich()
print(bird.intro(),bird.fly)
print(sparrow.fly())
print(ostrich.fly)
