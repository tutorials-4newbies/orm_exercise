from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///db.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class President(Base):
    __tablename__ = "presidents"

    id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)


def load():
    """
    after you model the President Class

    Pseudo code describing the algo:
    open the file
    load the content to json
    iterate over the list

    for each item in the list:
        item = President(fields mapping would be here)
        session.add(item)
    session.commit()
    """
    pass


def filter_by_party(party_name: str):
    """
    Pseudo code describing the algo:
    result = President.filter(some conditionals here).all()
    


    """
    pass


def run():
    load()


if __name__ == "__main__":
    run()
