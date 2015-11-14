import mysql.connector
import configparser
import sqlalchemy
import sqlalchemy.orm

url = 'mysql+mysqlconnector://username:password@localhost:3306/dbname'
engine = sqlalchemy.create_engine(url, echo=True)

# セッションを作成
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
