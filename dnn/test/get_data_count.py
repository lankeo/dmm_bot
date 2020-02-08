import time
from pymongo import MongoClient

db = dict(host="192.168.44.20", port=27017, dbname='dmm')
client = MongoClient(host=db.get('host'), port=db.get('port'))
collection = client[db.get('dbname')]['product']
i = 0
with open('./crawl.log', 'w+') as f:
	while i < 50010:
		s_count = collection.count()
		time.sleep(60)
		e_count = collection.count()
		t_count = e_count - s_count
		f.write("第%d个一分钟的抓取量为%s\n" % (i, t_count))
		i += 1
