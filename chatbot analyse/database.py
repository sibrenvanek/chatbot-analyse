import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///keywords.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

class keyword:
    __tablename__ = 'keywords'
    Id = Column(Integer, primary_key=True)
    Keyword = Column(String)
    Answer = Column(String)

def createTablesDB():
    Base.metadata.create_all(engine)

def getAllKeywords():
    session = DBSession()
    keywords = session.query(keyword).all()
    return keywords
