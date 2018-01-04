
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class ZIP(Base):
	__tablename__ = 'ZIPInfo'
	id = Column(Integer , primary_key=True)
	officename = Column(String(250))
	pincode = Column(String(250))
	officetype = Column(String(250))
	Deliverystatus = Column(String(250))
	divisionname = Column(String(250))
	regionname = Column(String(250))
	circlename = Column(String(250))
	taluk = Column(String(250))
	districtname = Column(String(250))
	statename = Column(String(250))

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns \
				if c.name is not 'id'}

	def __str__(self):
		return self.pincode

def createDB(DB_URI):
	engine = create_engine(DB_URI)
	Base.metadata.create_all(engine)
