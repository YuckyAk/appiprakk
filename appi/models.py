from pip._vendor.distlib.metadata import Metadata
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
engine = create_engine("postgresql://postgres:123@localhost/postgres")
Base = declarative_base()
metadata=Metadata()

class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    family_id = Column(Integer, ForeignKey('families.id'))

    family = relationship("Family", back_populates="plants")


class Family(Base):
    __tablename__ = 'families'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    plants = relationship("Plant", back_populates="family")

class Seed(Base):
    __tablename__ = 'seeds'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    plant_id = Column(Integer, ForeignKey('plants.id'))

    plant = relationship("Plant", back_populates="seeds")

class FruitTree(Base):
    __tablename__ = 'fruit_trees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    plant_id = Column(Integer, ForeignKey('plants.id'))

    plant = relationship("Plant", back_populates="fruit_tree")

