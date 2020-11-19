from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///db.db', echo=True)
Session = sessionmaker(bind=engine)


class President(Base):
    __tablename__ = "presidents"

    id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)


def run():
    pass


if __name__ == "__main__":
    run()
