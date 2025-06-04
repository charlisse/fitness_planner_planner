class User:
    def __init__(self, gender, age, fitness_level):
        self.gender = gender.lower()
        self.age = age
        self.fitness_level = fitness_level.lower()

    def is_eligible(self):
        return 18 <= self.age <= 65