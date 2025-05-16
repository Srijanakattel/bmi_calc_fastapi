from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_bmi_underweight():
    response = client.post("/calculate-bmi/", json={"weight": 50, "height": 1.8})
    assert response.status_code == 200
    assert response.json() == {"bmi": 15.43, "category": "Underweight"}

def test_calculate_bmi_normal():
    response = client.post("/calculate-bmi/", json={"weight": 70, "height": 1.75})
    assert response.status_code == 200
    assert response.json() == {"bmi": 22.86, "category": "Normal weight"}

def test_calculate_bmi_overweight():
    response = client.post("/calculate-bmi/", json={"weight": 85, "height": 1.75})
    assert response.status_code == 200
    assert response.json() == {"bmi": 27.76, "category": "Overweight"}

def test_calculate_bmi_obesity():
    response = client.post("/calculate-bmi/", json={"weight": 120, "height": 1.75})
    assert response.status_code == 200
    assert response.json() == {"bmi": 39.18, "category": "Obesity"}
