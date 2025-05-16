from main import BMICalculatorInput, calculate_bmi

if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        input_data = BMICalculatorInput(weight=weight, height=height)
        result = calculate_bmi(input_data)
        print(f"Your BMI is: {result['bmi']:.2f}")
        print(f"Health category: {result['category']}")
    except Exception as e:
        print(f"Invalid input: {e}")
