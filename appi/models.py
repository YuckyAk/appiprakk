from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

metadata = MetaData()

app = FastAPI()

Base = declarative_base()

class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    family_id = Column(Integer, ForeignKey('families.id'))

    family = relationship("Family", back_populates="plants")

class Family(Base):
    __tablename__ = 'families'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    plants = relationship("Plant", back_populates="family")


class Seed(Base):
    __tablename__ = 'seeds'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    plant_id = Column(Integer, ForeignKey('plants.id'))

    plant = relationship("Plant", back_populates="seeds")


