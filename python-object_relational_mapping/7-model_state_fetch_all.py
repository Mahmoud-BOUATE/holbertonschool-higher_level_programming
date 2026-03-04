#!/usr/bin/python3
"""
7. All states via SQLAlchemy
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Assurez-vous que model_state.py est dans le même dossier

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Création de l'engine pour MySQL
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Création de session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Récupère tous les états triés par id
        states = session.query(State).order_by(State.id).all()

        for state in states:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print("Error:", e)
    finally:
        session.close()

if __name__ == "__main__":
    main()