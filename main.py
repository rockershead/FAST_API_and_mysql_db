#main.py

from fastapi import FastAPI, Body, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)

def get_session():
 session = SessionLocal()
 try:
  yield session
 finally:
  session.close()

 



app = FastAPI()

@app.get("/users")
def getAllUsers(session: Session = Depends(get_session)):
 users = session.query(models.Pyden_User).all()
 return users

@app.get("/users/{id}")
def getUser(id:int, session: Session = Depends(get_session)):
 user = session.query(models.Pyden_User).get(id)
 return user

@app.post("/user/")
def addUser(user:schemas.Pyden_User, session: Session = Depends(get_session)):
 user = models.Pyden_User(**user.dict())      ##to include all fields instead of manually typing all fields
 session.add(user)
 session.commit()
 session.refresh(user)

 return user

@app.put("/user/{id}")
def updateUser(id:int, user:schemas.Pyden_User, session: Session = Depends(get_session)):
 userObject = session.query(models.Pyden_User).get(id)
 
 user_data = user.dict(exclude_unset=True)
 for key, value in user_data.items():
  setattr(userObject, key, value)
  
 session.add(userObject)
 
 session.commit()
 session.refresh(userObject) 
 return userObject
