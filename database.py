from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = 'mysql+mysqldb://'+user+':'+password+'@'+host+'/'+db_name

#Create whatever database engine instance u want
engine = create_engine(DATABASE_URL)

#Create declaritive base meta instance
Base = declarative_base()

#Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)