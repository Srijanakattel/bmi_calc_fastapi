from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

class BMICalculatorInput(BaseModel):
    weight: float  # in kilograms
    height: float  # in meters

@app.post("/calculate-bmi/")
def calculate_bmi(input_data: BMICalculatorInput):
    bmi = input_data.weight / (input_data.height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    return {"bmi": round(bmi, 2), "category": category}
