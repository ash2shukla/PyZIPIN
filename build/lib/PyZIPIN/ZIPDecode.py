from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from .createDB import ZIP, Base
from json import dumps
from os import path

DB_URI = 'sqlite:///'+path.join(path.dirname(path.abspath(__file__)), "ZIPInfo.db")

engine = create_engine(DB_URI,connect_args={'check_same_thread':False},poolclass=StaticPool)
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
_session = DBSession()

# Define the retrieving functions here

def decode(zip_code,all_results=False):
	'''
		for a ZIP returns:

		'officename'
		'pincode'
		'officetype'
		'Deliverystatus'
		'divisionname'
		'regionname'
		'circlename'
		'taluk'
		'districtname'
		'statename'

		officetype has 3 values:
		H.O. Head Post Office
		B.O. Branch Post Office
		S.O. Sub Post Office
	'''
	try:
		int(zip_code)
	except:
		return None

	if all_results :
		retval = []
		results = _session.query(ZIP).filter(ZIP.pincode == str(zip_code))
		for i in results:
			retval.append(i.as_dict())
		return dumps(retval)
	else:
		res =  _session.query(ZIP).filter(ZIP.pincode == str(zip_code)).first()
		if res is not None:
			return dumps(res.as_dict())
		else:
			return None


def encode(district, all_results=False):
	'''
		returns ZIP and officename for a districtname
	'''
	if all_results:
		retval = []
		for i in _session.query(ZIP).filter(ZIP.districtname==district):
			i = i.as_dict()
			retval.append({'pincode':i['pincode'],'officename':i['officename']})
		return dumps(retval)
	else:
		res = _session.query(ZIP).filter(ZIP.districtname==district).first()
		if res is not None:
			res = res.as_dict()
			return dumps({'pincode':res['pincode'],'officename':res['officename']})
		else:
			return None
