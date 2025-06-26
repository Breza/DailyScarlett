# content_generator.py
# (This is a simplified example)
from datetime import datetime


# You would import your weather and SLM functions here
# from weather import get_forecast_data
# from slm import run_morning_model

def generate_morning_summary():
    summary_text = f"Hi Scarlett!\n\nThe current date and time is {datetime.now().strftime('%m/%d/%Y')}"
    return summary_text


def get_bedtime_checklist():
    return "[ ] Brush Teeth\n[ ] Pajamas On\n[ ] Read a Book\n[ ] Tucked In Tight\n\nGoodnight!\n"
