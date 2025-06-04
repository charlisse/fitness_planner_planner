from workout import WorkoutPlan
from utils import fetch_motivation, save_plan_to_file
from rich.console import Console
from user import User

console = Console()

class InvalidAgeError(Exception):
    """Raised when age is not between 18 and 65."""
    pass

def get_valid_input(prompt, validator, error_message='Invalid input.', exception_type=ValueError):
    while True:
        try:
            value = input(prompt).strip()
            if value.lower() == 'q':
                console.print('[bold red]Exiting program. Goodbye![/bold red]')
                exit()
            if not validator(value):
                raise exception_type(error_message)
            return value
        except Exception as ve:
            console.print(f'[red]{ve} Please try again.[/red]')

def main():

    try:
        console.print('[bold cyan]Welcome to the Personalised Training Program![/bold cyan]')
        console.print('[italic]Type "q" at any prompt to exit.[/italic]')

        gender = get_valid_input('Enter your gender (male/female/other): ',
                            lambda g: g.lower() in ['m', 'male', 'f', 'female', 'o', 'other'])
        gender_map = {'m': 'male', 'f': 'female', 'o': 'other'}
        gender = gender_map.get(gender.lower(), gender.lower())

        age = get_valid_input('Enter your age: ',
                             lambda a: a.isdigit() and User("temp", int(a), "temp").is_eligible(),
                             "Sorry, this program is only for users between 18 and 65 years old.", 
                             exception_type=InvalidAgeError)
        age = int(age)

        fitness = get_valid_input('Enter fitness level (beginner/intermediate/advanced): ',
                            lambda f: f.lower() in ['b', 'beginner', 'i', 'intermediate', 'a', 'advanced'])
        fitness_map = {'b': 'beginner', 'i': 'intermediate', 'a': 'advanced'}
        fitness = fitness_map.get(fitness.lower(), fitness.lower())


        console.print('\n[bold green]Summary of Your Choices:[/bold green]')
        console.print(f'Gender: [yellow]{gender}[/yellow]')
        console.print(f'Age: [yellow]{age}[/yellow]')
        console.print(f'Fitness Level: [yellow]{fitness}[/yellow]')

        user = User(gender, age, fitness)
        workout = WorkoutPlan(user.gender, user.age, user.fitness_level)
        plan = workout.generate()

        console.print('\n[bold green]Your Weekly Workout Plan:[/bold green]')
        for day, activity in plan.items():
            console.print(f'[yellow]{day}[/yellow]: {activity}')
        
        save_plan_to_file(plan)

        quote = fetch_motivation()
        console.print(f'\n[italic magenta]Motivation of the day:[/italic magenta] {quote}')

    except (ValueError, InvalidAgeError) as e:
        console.print(f'[red]{e}[/red]')
    except Exception as e:
        console.print(f'[red]An unexpected error occurred:[/red] {e}')

if __name__ == "__main__":
    main()

