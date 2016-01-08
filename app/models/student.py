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

def insert(session, name, kana):
    '''
    :param Session session
    :param String name
    :param String kana
    '''
    new_student = Student(name=name, kana=kana)
    session.add(new_student)
    session.commit()

def update(session, name, change_name):
    '''
    :param Session session
    :param String name
    :param String kana
    '''
    session.query(Student).filter_by(name=name).update({"name": change_name})
    session.commit()

def delete(session, name, kana):
    '''
    :param Session session
    :param String name
    :param String kana
    '''
    found_student = session.query(Student).filter_by(name=name).first()
    if found_student is not None:
        session.delete(found_student)
        session.commit()

def select(session, name):
    '''
    :param Session session: name
    :return found_student
    '''
    try:
        with session.begin(subtransactions=True):
            query = session.query(Student).with_lockmode('update')
            found_student = session.query(Student).filter_by(name=name).first()
            return found_student
    except SQLAlchemyError:
        session.rollback()

def select_all(session):
    '''
    :param Session session
    :return result
    '''
    results = session.query(Student).all()
    return results
