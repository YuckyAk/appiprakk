from fastapi import FastAPI

from models import Plant, Family, Seed
from database import db
from schema import Plants_post

app = FastAPI()


@app.post("/plants/", response_model=Plants_post)
async def create_plant(plant: Plants_post):
    db.add(plant)
    db.commit()
    db.refresh(plant)
    return plant

@app.get("/plants/{plant_id}")
async def get_plant(plant_id: int):
    plant = db.query(Plant).filter(Plant.id == plant_id).first()
    return plant

@app.get("/plants")
async def get_all_plants():
    plants = db.query(Plant).all()
    return plants

@app.get("/families/{family_id}")
async def get_family(family_id: int):
    family = db.query(Family).filter(Family.id == family_id).first()
    return family

@app.get("/families")
async def get_all_families():
    families = db.query(Family).all()
    return families

@app.get("/seeds/{seed_id}")
async def get_seed(seed_id: int):
    seed = db.query(Seed).filter(Seed.id == seed_id).first()
    return seed

@app.get("/seeds")
def get_all_seeds():
    seeds = db.query(Seed).all()
    return seeds


