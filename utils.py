import json
import os
import requests
from rich.console import Console
import random

console = Console()

def save_plan_to_file(plan, path="data/workouts.json"):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(plan, f, indent=2)
        console.print(f"[green]Workout plan saved to {os.path.abspath(path)}[/green]")
    except IOError as ioe:
        console.print(f"[red]I/O error when saving the plan: {ioe}[/red]")

local_quotes = [
   "Believe in yourself and all that you are.",
   "No pain, no gain!",
   "Don’t limit your challenges—challenge your limits."
   "Push harder than yesterday if you want a different tomorrow.",
   "Fall in love with taking care of yourself.",
   "Progress, not perfection.",
   "Your body can stand almost anything. It’s your mind that you have to convince.",
   "Discipline is doing it even when you don’t feel like it.",
   "Make yourself proud.",
   "The only bad workout is the one you didn’t do.",
]

def fetch_motivation():
    return random.choice(local_quotes)

