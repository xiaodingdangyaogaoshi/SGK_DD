dialect='mysql'
driver='mysqldb'
username='root'
password='zys9970304'
host='127.0.0.1'
port='3306'
database='sgk'
SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(dialect,driver,username,password,host,port,database)
SQLALCHEMY_TRACK_MODIFICATIONS=False
