import json
import requests
from rich.console import Console

console = Console()

def save_plan_to_file(plan, path="data/workouts.json"):
    try:
        with open(path, "w") as f:
            json.dump(plan, f, indent=2)
        console.print(f"[green]Workout plan saved to {path}[/green]")
    except FileNotFoundError:
        console.print("[red]Error: File Path does not exist.[/red]")
    except IOError as ioe:
        console.print(f"[red]I/O error when saving the plan: {ioe}[/red]")

def fetch_motivation():
    try:
        response = requests.get("https://type.fit/api/quotes", timeout=5)
        if response.ok:
            quotes = response.json()
            return quotes[0]["text"]
        return "Keep pushing your limits!"
    except (requests.RequestException, ValueError):
        return "You're stronger than you think!"
    