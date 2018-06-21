import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.sql.expression import func

Base = declarative_base()
engine = create_engine('sqlite:///keywords.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

class keyword(Base):
    __tablename__ = 'keywords'
    Id = Column(Integer, primary_key=True)
    Keyword = Column(String(50))
    Answer = Column(String(200))

def createTablesDB():
    Base.metadata.create_all(engine)

def getAllKeywords():
    session = DBSession()
    keywords = session.query(keyword).all()
    return keywords

def printKeywords():
    keywords = getAllKeywords()
    for k in keywords:
        print(str(k.Id) + ": " + k.Keyword + " -> " + k.Answer)

def getId(session):
    qry = session.query(func.max(keyword.Id))
    id = qry.one()[0]
    if id == None:
        return 0
    return id + 1

def addKeyword(Keyword, Answer):
    session = DBSession()
    id = getId(session)
    k = keyword(Id = id, Keyword = Keyword, Answer = Answer)
    session.add(k)
    session.commit()
    session.close()