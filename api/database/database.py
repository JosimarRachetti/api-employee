import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Sequence, String, Integer, Text, Float


engine = create_engine(os.environ["DATABASE_URI"])
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    registration = Column(Integer, Sequence('employee_registration_seq', start=1000, increment=1), primary_key=True)
    name = Column(String)
    last_name = Column(String)
    code_position = Column(Integer)
    salary = Column(Float)
    password = Column(String)
    status = Column(String)
    create = Column(String)
    last_update = Column(String)


class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, Sequence('position_id_seq', start=100, increment=1), primary_key=True)
    title = Column(String)
    description = Column(Text)
    code_team = Column(String)
    status = Column(String)
    create = Column(String)
    last_update = Column(String)

class Leader(Base):
    __tablename__ = 'leader'

    id = Column(Integer, primary_key=True)
    code_employee = Column(Integer)
    code_position = Column(Integer)
    code_team = Column(String)
    create = Column(String)

class Connection:
    def __init__(self):
        self.session = None
    
    def create_session(self):
        if self.session:
            return self.session
        Session = sessionmaker(bind=engine)
        self.session = Session()
        return self.session

    def finish_session(self):
        self.session.close()

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()

def finish_session(session):
    session.close()

if __name__ == '__main__':
    print("inicio criacao tabelas")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("tabelas criadas")


