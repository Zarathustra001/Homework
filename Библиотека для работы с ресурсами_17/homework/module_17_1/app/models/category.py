fromm app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlAlchemy.orm import relationship

class Category(Base):
  __tablename__="categories"
  __table_args__ = {'keep_existing': True}
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  slug= Column(String, unique=True, index=True)
  is_active = Column(Boolean, default=True)
  parent_id = Column(Integer, ForeignKey("categories.id"), nullable= True)

  products = relationship("Product", back_populates="category")

from sqlalchemy.shcema import CreateTable
print(CreateTable(Category.__table__))
  
