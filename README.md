# Personalised Training Program App

This Python application generates a customised weekly workout plan based on user inputs: gender, age, and fitness level. It also provides a daily motivational quote to encourage your fitness journey.

## Features

- Takes user input for gender, age, and fitness level
- Validates user input with helpful error messages
- Generates workout plans for beginner, intermediate, and advanced levels
- Saves the generated workout plan as a JSON file (`data/workouts.json`)
- Displays a motivational quote each time the program runs
- Graceful error handling to prevent crashes

## Prerequisities

- Python 3.7 or higher 

## Setup

1. Clone this repo or download the files.
   ```bash
   git clone https://github.com/your-username/fitness_planner_planner.git
   cd fitness_planner_planner

2. Create a virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

3. Install dependencies 
    ```bash
    pip install -r requirements.txt
    ```

4. To deactivate the virtual environment, run:
    ```bash 
    deactivate
    ```

## Usage 

1. Run the program with 
    ```bash
    python3 main.py 
    ```

You will be prompted to enter:
- Your gender (male/female/other)
- Your age (must be between 18 and 65)
- Your fitness level (beginner/intermediate/advanced)

The app will then:
- Display your personalised weekly workout plan
- Save the workout plan to ```data/workouts.json```
- Show a motivational quote

Type ```q``` at any prompt to exit the program early.

## Requirements and Licensing 

This project uses the following third-party packages:
- ```rich``` (MIT License): For styled terminal output. The MIT license allows free personal/commercial use with attribution.

Please ensure compliance with these open-source licenses when distributing or modifying the app.

## Error Handling

The app gracefully handles:
- Invalid inputs (e.g., non-numeric age, invalid gender or fitness levels)
- Out-of-range ages (only accepts 18 to 65)
- File writing errors (e.g., missing folders)
- Program exit on typing ```q``` at any prompt

## Contact / Support 
For questions or feedback, please contact 16332@coderacademy.edu.au
Thank you for using the Personalised Training Program App! Keep pushing your limits!

