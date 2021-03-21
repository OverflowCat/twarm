from tinydb import TinyDB, Query
db = TinyDB('locations.json')

def record(vid: str, name: str) -> int:
	# 在 Swarm 通过分享地点到 bot 即可添加地点至数据库
	statement = {'v': vid, 'n': name}
	print("DB ADD RECORD:")
	print(statement)
	return db.insert(statement)
Place = Query()

def lookup(name: str):
	res = db.search(Place.n == name)
	print(res)
	return res