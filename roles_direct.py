from flask_sqlalchemy import SQLAlchemy
from models import User,db

def insert_roles():
    # Create HOD and Coordinator roles
    hod_user = User(email='aiml@gmail.com', password='hod1234', role='HOD')
    coordinator_user = User(email='coordinator@gmail.com', password='pc1234', role='Coordinator')

    # Add to the session and commit to the database
    db.session.add(hod_user)
    db.session.add(coordinator_user)
    db.session.commit()

    print("HOD and Coordinator roles inserted successfully!")

