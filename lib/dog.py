from models import Dog
from sqlalchemy import (create_engine, desc,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:memory:')

def create_table(base, engine):
    pass

def save(session, dog):
    sql = """
            INSERT INTO dogs (name, breed) VALUES (:name, :breed)
        """
    session.execute(sql, {"name": dog.name, "breed": dog.breed})

def get_all(session):
    sql = """
        SELECT * FROM dogs
    """
    result = session.execute(sql)
    all_dogs = [Dog(name=row.name, breed=row.breed) for row in result]
    return all_dogs

def find_by_name(session, name):
    sql = """
        SELECT * FROM dogs WHERE name = :name
    """
    result = session.execute(sql, {"name": name})
    row = result.fetchone()
    if row is not None:
        dog = Dog(name=row.name, breed=row.breed)
        return dog
    return None


def find_by_id(session, id):
    dog = session.query(Dog).filter_by(id=id).first()
    return dog


def find_by_name_and_breed(session, name, breed):
    sql = """
        SELECT * FROM dogs WHERE name = :name AND breed = :breed
    """
    result = session.execute(sql, {"name": name, "breed": breed})
    row = result.fetchone()
    if row is not None:
        dog = Dog(name=row.name, breed=row.breed)
        return dog

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    row = session.query(Dog).filter_by(id=dog.id).first()
    return row.breed == breed