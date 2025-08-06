# no external or third party imports used in this file 

class User:
    """
    Represents a user of the fitness program.

    Attributes:
        gender (str): The users gender.
        age (init): The users age.
        fitness_level (str): The users fitness level 
    """
    def __init__(self, gender, age, fitness_level):
        """
        Initialises the User object with gender, age, and fitness level. 

        Parameters:
            gender (str): Users gender.
            age (init): users age.
            fitness_level (str): Users fitness level
        """
        self.gender = gender.lower()
        self.age = age
        self.fitness_level = fitness_level.lower()

    def is_eligible(self):
        """
        Checks if the user is eligible based on age (between 18 and 65).

        Returns:
            bool: True if eligible, False otherwise.
        """
        return 18 <= self.age <= 65
    
    def __str__(self):
        """
        Returns a string representation of the user. 

        Returns:
            str: User information
        """
        return f"Gender: {self.gender}, Age: {self.age}, Fitness Level: {self.fitness_level}"
