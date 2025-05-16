# BMI Calculator

This is a simple FastAPI application that calculates the Body Mass Index (BMI) and provides the health category based on the BMI value.

## Features
- Accepts weight (in kilograms) and height (in meters) as input.
- Returns the calculated BMI and the corresponding health category.
- Provides both a REST API and a command-line interface (CLI).

## How to Run

### Locally
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd bmicalculator
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open your browser and navigate to `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/docs` to access the Swagger UI.
   - The root URL `/` will automatically redirect you to the API documentation at `/docs`.

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t bmicalculator .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 bmicalculator
   ```
3. Open your browser and navigate to `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/docs` to access the Swagger UI.

## API Usage
- **Endpoint:** `POST /calculate-bmi/`
- **Request Body (JSON):**
  ```json
  {
    "weight": 70,
    "height": 1.75
  }
  ```
- **Response:**
  ```json
  {
    "bmi": 22.86,
    "category": "Normal weight"
  }
  ```
- You can use the Swagger UI to test the API interactively.

## Command-Line Interface (CLI)
You can also calculate BMI using the CLI script:

```bash
python bmi_cli.py
```
You will be prompted to enter your weight and height, and the script will display your BMI and health category.

## Health Categories
- **Underweight**: BMI < 18.5
- **Normal weight**: 18.5 ≤ BMI < 24.9
- **Overweight**: 25 ≤ BMI < 29.9
- **Obesity**: BMI ≥ 30

## Tests
- Unit tests are included to validate the BMI calculation logic.
- To run tests locally:
  ```bash
  pytest
  ```

