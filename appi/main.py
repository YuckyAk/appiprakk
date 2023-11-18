from  models import Base, engine, Plant, Seed, FruitTree

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Создание нового растения
plant1 = Plant(name='Роза', description='Кустарник со цветами различных оттенков.', family_id=1)
session.add(plant1)

# Создание нового семени
seed1 = Seed(name='Розовые семена', description='Семена для разведения роз.', plant_id=1)
session.add(seed1)

# Создание нового плодового дерева
fruit_tree1 = FruitTree(name='Яблоня', description='Плодовое дерево, дающее яблоки.', plant_id=1)
session.add(fruit_tree1)

session.commit()

# Получение всех растений
plants = session.query(Plant).all()
for plant in plants:
    print(plant.name)

# Получение информации о семенах растений
seeds = session.query(Seed).all()
for seed in seeds:
    print(seed.name)

# Получение информации о плодовых деревьях
fruit_trees = session.query(FruitTree).all()
for fruit_tree in fruit_trees:
    print(fruit_tree.name)

