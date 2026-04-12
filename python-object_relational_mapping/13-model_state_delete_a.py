#!/usr/bin/python3
"""Deletes all State objects containing the letter 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Connects to the MySQL database and deletes states with 'a'."""

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for state in states:
        if 'a' in state.name:
            session.delete(state)

    session.commit()
    session.close()
