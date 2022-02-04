import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from setting import Base
from setting import ENGINE

class Test(Base):
    __tablename__ = 'test'
    id = Column('id', Integer, primary_key=True)
    column1 = Column('column1', String(100))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == '__main__':
    main(sys.argv)
