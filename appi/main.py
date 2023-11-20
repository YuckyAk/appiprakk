from appi.database import SessionLocal
from appi.models import Plant, Family, Seed


@app.get("/")
def read_root():
    return {"message": "Welcome to the Plants API!"}

@app.post("/plants")
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

@app.post("/families")
def create_family(family: Family):
    db = SessionLocal()
    db.add(family)
    db.commit()
    db.refresh(family)
    return family

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

@app.post("/seeds")
def create_seed(seed: Seed):
    db = SessionLocal()
    db.add(seed)
    db.commit()
    db.refresh(seed)
    return seed

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

