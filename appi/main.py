from fastapi import FastAPI
from database import SessionLocal
from schema import Plant, Family, Seed

app = FastAPI()

Plants = []
Family = []
Seed = []

@app.post("/plants/")
def create_plant(plant: Plant):
    db = SessionLocal()
    db.add(plant)
    db.commit()
    db.refresh(plant)
    return plant

@app.get("/plants/{plant_id}")
def get_plant(plant_id: int):
    db = SessionLocal()
    plant = db.query(Plant).filter(Plant.id == plant_id).first()
    return plant

@app.get("/plants")
def get_all_plants():
    db = SessionLocal()
    plants = db.query(Plant).all()
    return plants



@app.get("/families/{family_id}")
def get_family(family_id: int):
    db = SessionLocal()
    family = db.query(Family).filter(Family.id == family_id).first()
    return family

@app.get("/families")
def get_all_families():
    db = SessionLocal()
    families = db.query(Family).all()
    return families



@app.get("/seeds/{seed_id}")
def get_seed(seed_id: int):
    db = SessionLocal()
    seed = db.query(Seed).filter(Seed.id == seed_id).first()
    return seed

@app.get("/seeds")
def get_all_seeds():
    db = SessionLocal()
    seeds = db.query(Seed).all()
    return seeds

