import configparser
import sqlalchemy
import sqlalchemy.orm

config = configparser.ConfigParser()
config.read('config/db.cnf')

host = config.get('db', 'host')
port = config.getint('db','port')
user = config.get('db', 'user')
passwd = config.get('db', 'password')
db = config.get('db', 'database')

url = 'mysql+mysqlconnector://' + user + ':' + passwd + '@' + host + ':' + str(port) + '/' + db
engine = sqlalchemy.create_engine(url, echo=True)

# セッションを作成
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
