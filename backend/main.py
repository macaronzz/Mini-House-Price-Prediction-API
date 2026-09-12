from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Task 1: Prediction function
def predict_price(area: float, bedrooms: int, location: str) -> float:
    base_price = 500_000_000
    area_price = 15_000_000 * area
    bed_price = 50_000_000 * bedrooms
    
    total = base_price + area_price + bed_price
    
    loc_lower = location.lower()
    if loc_lower == "hanoi":
        total *= 1.3
    elif loc_lower == "hcmc":
        total *= 1.25
        
    return round(total / 1_000_000) * 1_000_000

# Task 2: GET /predict endpoint
@app.get("/predict")
def get_predict(area: float, bedrooms: int, location: str = "other"):
    price = predict_price(area, bedrooms, location)
    return {
        "area": area,
        "bedrooms": bedrooms,
        "location": location,
        "predicted_price": price
    }

# Task 6: Bonus POST /predict endpoint
class HouseInput(BaseModel):
    area: float
    bedrooms: int
    location: str = "other"

@app.post("/predict")
def post_predict(data: HouseInput):
    price = predict_price(data.area, data.bedrooms, data.location)
    return {
        "area": data.area,
        "bedrooms": data.bedrooms,
        "location": data.location,
        "predicted_price": price
    }

# Task 4: Serve the frontend from the same origin
app.mount("/static", StaticFiles(directory="../frontend"), name="static")