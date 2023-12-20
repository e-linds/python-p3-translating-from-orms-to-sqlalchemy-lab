from models import *


def create_table(Base, engine):

    Base.metadata.create_all(engine)

def save(session, dog):
    if type(dog) is Dog:
        session.add(dog)
        session.commit()

def get_all(session):
    all_dogs = session.query(Dog).all()
    return all_dogs
    

def find_by_name(session, name):
    dogs = session.query(Dog).filter(Dog.name == name).first()
    return dogs

def find_by_id(session, id):
    dog = session.query(Dog).filter(Dog.id == id).first()
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog

def update_breed(session, dog, breed):
    if type(dog) is Dog:
        dog.breed = breed
        session.commit()