# Personalized Training Program App

This Python app generates a custom weekly workout plan based on user input: gender, age, and fitness level. It also provides a motivational quote of the day.

## Setup

1. Clone this repo or download the files.
   ```bash
   git clone https://github.com/your-username/fitness_planner_planner.git
   cd fitness_planner_planner

2. Create a virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependenies 
    ```bash
    pip install -r requirements.txt

## Usage 

1. Run the program with 
    ```bash
    python3 main.py 

You'll be prompted to enter your gender, age and fitness level. The app will then generate a personalised workout plan and save it to data/workouts.json

## Notes 

The app only accepts users aged between 18 and 65.
Plans are automatically saved into a JSON file (data/workouts.json) after generation. 
