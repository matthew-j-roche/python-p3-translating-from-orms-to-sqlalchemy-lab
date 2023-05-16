#!/usr/bin/env python3

from typing import Any
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

