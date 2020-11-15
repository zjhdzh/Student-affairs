import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
db = pymysql.connect(host='localhost', user='root', password='root', db='test')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('DATABASE VERSION IS: %s' % data)

db.close()