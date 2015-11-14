import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy.exc import SQLAlchemyError

Base = sqlalchemy.ext.declarative.declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(30))
    kana = sqlalchemy.Column(sqlalchemy.String(30))

def search(session):
    '''
    :param Session session: name
    :return found_student
    '''
    try:
        with session.begin(subtransactions=True):
            # SELECT 時に排他ロックを取得する
            query = session.query(Student).with_lockmode('update')
            # 追加したデータを検索
            found_student = session.query(Student).filter_by(name='saori takebe').first()
            return found_student
    except SQLAlchemyError:
        session.rollback()
