class WorkoutPlan:
    def __init__(self, gender, age, level):
        self.gender = gender.lower()
        self.age = age
        self.level = level.lower()
    
    def generate(self):
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

