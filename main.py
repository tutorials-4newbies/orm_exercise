
from sqlalchemy import create_engine
engine = create_engine('sqlite:///db.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class President(Base):
    __tablename__ = "presidents"

    id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)



