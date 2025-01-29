from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclaitiveBase
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///ecomerce.db", echo = True)

SessionLocal = sesionmaker(bind=engine)


class Base(DeclaitiveBase):
  pass

#class User(Base):
  #__tablename__ = "user"
  #id = Column(Integer, primary_key = True)
  #username = Column(String)
  #password = Column(String)





