# This is a short exercise to practice creating classes that follow the 4 OOP principles.
# Part 1 
# Create a Student class that takes the name and age on creation.
# Create 2 objects of your student class and get the age of one of them.
# Part 2
# With your Student class, make modifications for the class to accept the student’s current class (as in a classroom) on creation.
# Then add a method that takes 3 test scores and calculates the student’s average test score.
# Part 3
# Create 3 classes, A bird parent class and then an Owl and Dodo class.
# Make use of the 4 OOP Principles.

# Part 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1_age = student1.age
print(student1_age)

# Part 2
class Student:
    def __init__(self, name, age, classroom):
        self.name = name
        self.age = age
        self.classroom = classroom

    def average_score(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3
    
student1 = Student("Alice", 20, "10th Grade")
average = student1.average_score(85, 90, 95)
print(average)

# Part 3
# Encapsulation → keep data inside the class, control access
# Inheritance → child classes reuse parent class logic
# Polymorphism → same method name, different behavior
# Abstraction → parent defines what must exist, not how

from abc import ABC, abstractmethod

# Abstraction and Encapsulation
class Bird(ABC):
    def __init__(self, species):
        self.species = species   # Encapsulation, attributes are protected and accessed via methods.
    
    @abstractmethod              # Abstraction
    def fly(self):
        pass

# Inheritance and Polymorphism 
class Owl(Bird):
    def fly(self):
        return f"The {self.species} is flying silently."

    def sound(self):
        return "Hoot hoot"
    
# Inheritance + Polymorphism
class Dodo(Bird):
    def fly(self):
        return f"The {self.species} cannot fly."

    def sound(self):
        return "Squawk"

    
birds = [
    Owl("Snowy Owl"),
    Dodo("Mauritius Dodo")
]

for bird in birds:
    print(bird.fly())
    print(bird.sound())