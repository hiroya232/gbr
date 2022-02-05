import sys
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.sql.functions import current_timestamp
from setting import Base, ENGINE, session

class Contribution(Base):
    __tablename__ = 'border_contribution'
    id = Column('id', Integer, primary_key=True)
    created_at = Column('created_at', DateTime, server_default=current_timestamp(), nullable=False)
    updated_at = Column('updated_at', DateTime, server_default=current_timestamp(), onupdate=datetime.now(), nullable=False)
    rank_1 = Column('rank_1', String(100))
    rank_2 = Column('rank_2', String(100))
    rank_3 = Column('rank_3', String(100))
    rank_2000 = Column('rank_2000', String(100))
    rank_80000 = Column('rank_80000', String(100))
    rank_140000 = Column('rank_140000', String(100))
    rank_180000 = Column('rank_180000', String(100))
    rank_270000 = Column('rank_270000', String(100))
    rank_370000 = Column('rank_370000', String(100))

def insert(rank_border_list):
    contribution = Contribution(
        rank_1=rank_border_list[0],
        rank_2=rank_border_list[1],
        rank_3=rank_border_list[2],
        rank_2000=rank_border_list[3],
        rank_80000=rank_border_list[4],
        rank_140000=rank_border_list[5],
        rank_180000=rank_border_list[6],
        rank_270000=rank_border_list[7],
        rank_370000=rank_border_list[8]
    )
    session.add(contribution)
    session.flush()
    session.commit()

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == '__main__':
    main(sys.argv)
