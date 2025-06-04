class User:
    def __init__(self, gender, age, fitness_level):
        self.gender = gender.lower()
        self.age = age
        self.fitness_level = fitness_level.lower()

    def is_eligible(self):
        return 18 <= self.age <= 65
    
    def __str__(self):
        return f"Gender: {self.gender}, Age: {self.age}, Fitness Level: {self.fitness_level}"
