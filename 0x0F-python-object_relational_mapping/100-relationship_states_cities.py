#!/usr/bin/python3
"""
Prints all city objects from the database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    c_State = State(name='California')
    s_City = City(name='San Francisco')
    c_State.cities.append(s_City)

    session.add(c_State)
    session.add(s_City)
    session.commit()
