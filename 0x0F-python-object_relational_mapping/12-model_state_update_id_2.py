#!/usr/bin/python3
"""
Module  that changes the name of a State object from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    if len(argv) != 4:
        print("error")
    else:
        USER = argv[1]
        PASS = argv[2]
        DB = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(USER, PASS, DB), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        update_state = session.query(State).filter(State.id == 2).first()
        update_state.name = 'New Mexico'
        session.commit()
