from sqlalchemy import Column, Integer, String
from database import Base 

class Pyden_User(Base):
 __tablename__ = 'main_app_pyden_user'
 id = Column(Integer, primary_key=True)
 name = Column(String(256))
 age= Column(Integer)
 hobby=Column(String(256))