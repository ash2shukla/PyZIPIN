from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .createDB import ZIP, Base
from csv import reader
from codecs import open as copen

def ZIPs(file_name):
# Pincodelist.csv has some inconsistencies
	rd = reader(copen(file_name,'r',encoding='utf-8',errors='ignore'),delimiter=',', quotechar='|')
	# Store Header
	dic = rd.__next__()
	for i in rd:
		if len(i) != 10:
			try:
				int(i[2])
				# indeces will be + 1
				i.pop(0)
			except:
				# index 4,9 will be district,
				i.pop(8)
		yield i

def populate(file_name,DB_URI):
	engine = create_engine(DB_URI)
	Base.metadata.bind = engine

	DBSession = sessionmaker(bind= engine)

	session = DBSession()
	total = 155050
	iter_i = 0
	for i in ZIPs(file_name):
		iter_i+=1
		new_zip = ZIP(\
			officename = i[0],\
			pincode = i[1],\
			officetype = i[2],\
			Deliverystatus = i[3],\
			divisionname = i[4],\
			regionname = i[5],\
			circlename = i[6],\
			taluk = i[7],\
			districtname = i[8],\
			statename = i[9])
		session.add(new_zip)
		print(chr(27) + "[2J")
		print((iter_i/total)*100)
	session.commit()y
