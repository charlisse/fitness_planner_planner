from workout import WorkoutPlan
from utils import fetch_motivation, save_plan_to_file
from rich.console import Console

console = Console()

class InvalidAgeError(Exception):
    """Raised when age is not between 18 and 65."""
    pass

def get_valid_input(prompt, validator, error_message='Invalid input.', exception_type=ValueError):
    while True:
        try:
            value = input(prompt).strip()
            if not validator(value):
                raise exception_type(error_message)
            return value
        except Exception as ve:
            console.print(f'[red]{ve} Please try again.[/red]')

def main():
    try:
        console.print('[bold cyan]Welcome to the Personalised Training Program![/bold cyan]')

        gender = get_valid_input('Enter your gender (male/female/other): ',
                            lambda g: g.lower() in ['male', 'female', 'other'])
    
        age = get_valid_input('Enter your age: ',
                             lambda a: a.isdigit() and 18 <= int(a) <= 65,
                             "Sorry this program is only for users between 18 and 65 years old.", 
                             exception_type=InvalidAgeError)
        age = int(age)

        fitness = get_valid_input('Enter fitness level (beginner/intermediate/advanced): ',
                              lambda f: f.lower() in ['beginner', 'intermediate', 'advanced'])

        workout = WorkoutPlan(gender, age, fitness)
        plan = workout.generate()

        console.print('\n[bold green]Your Weekly Workout Plan:[/bold green]')
        for day, activity in plan.items():
            console.print(f'[yellow]{day}[/yellow]: {activity}')
        
        save_plan_to_file(plan)

        quote = fetch_motivation()
        console.print(f'\n[italic magenta]Motivation of the day:[italic magenta] {quote}')

    except ValueError:
        console.print('[red]Invalid input. Please enter numeric values for age.[/red]')
    except Exception as e:
        console.print(f'[red]An unexpected error occurred:[red/] {e}')
    
if __name__ == "__main__":
    main()
