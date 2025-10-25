#!/usr/bin/python3
"""
Prints the id of the State object whose name matches
the one given as argument, using SQLAlchemy ORM.
If no match is found, prints 'Not found'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == state_name)
        .first()
    )

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
