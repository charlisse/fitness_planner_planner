class WorkoutPlan:
    """
    Generates a weekly workout plan based on the user's fitness level. 

    Attributes:
        gender (str): Users gender
        age (int): users age
        level (str): users fitness level
    """

    def __init__(self, gender, age, level):
        """
        Initialises the WorkoutPlan with user attributes.

        Parameters:
            gender (str): The users gender
            age (int): The users age
            level (str): The users fitness level
        """
        self.gender = gender.lower()
        self.age = age
        self.level = level.lower()
    
    def generate(self):
        """
        Generates a dictionary of workouts for each day of the week based on the users fitness level. 

        Returns:
            dict: Workout plan with day-to-activity mapping

        Raises:
            ValueError: If the fitness level is not supported. 
        """
        plans = {
            "beginner": {
                "Monday": "Stretch + Brisk Walk",
                "Tuesday": "Bodyweight Squats",
                "Wednesday": "Rest",
                "Thursday": "Lunges",
                "Friday": "Core + Plank",
                "Saturday": "Situps",
                "Sunday": "Rest"
            },
            "intermediate": {
                "Monday": "Circuit Training",
                "Tuesday": "Upper Body + Jog",
                "Wednesday": "Core + Yoga",
                "Thursday": "HIIT + Lower Body",
                "Friday": "Recovery",
                "Saturday": "Full Body Strength",
                "Sunday": "Rest"
            },
            "advanced": {
                "Monday": "Heavy Lifting",
                "Tuesday": "Leg Day + Sprints",
                "Wednesday": "Back & Core",
                "Thursday": "HIIT",
                "Friday": "Endurance",
                "Saturday": "Strength Circuits",
                "Sunday": "Rest"
            }
        }

        if self.level not in plans:
            raise ValueError(f"Unsupported fitness level: {self.level}. Please try again.")
        return plans[self.level]

