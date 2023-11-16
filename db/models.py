from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def register_models(engine) -> None:
    Base.metadata.create_all(bind=engine)


class NoteBooks(Base):
    __tablename__ = 'notebooks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    characteristics = Column(String, unique=True, index=True)
    price = Column(Integer, unique=True, index=True)
