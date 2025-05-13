# lib/crud.py
from sqlalchemy.orm import sessionmaker
from models import engine, Student
from datetime import datetime

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create
student1 = Student(
    name="John Doe",
    email="john.doe@example.com",
    grade=10,
    birthday=datetime(2005, 5, 15),
    enrolled_date=datetime.now()
)
session.add(student1)
session.commit()
print(f"Created: {student1}")

# Read
students = session.query(Student).all()
print("All students:")
for student in students:
    print(student)

# Update
student1.grade = 11
session.commit()
print(f"Updated: {student1}")

# Delete
session.delete(student1)
session.commit()
print("Deleted student. Remaining students:")
for student in session.query(Student).all():
    print(student)

session.close()