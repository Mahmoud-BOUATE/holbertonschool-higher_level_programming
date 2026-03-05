#!/usr/bin/python3
"""
Defines a State class and a Base instance using SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance
Base = declarative_base()


class City(Base):
    """State class that links to the states table"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
