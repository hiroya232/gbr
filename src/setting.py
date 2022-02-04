import os
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base


DATABASE = 'mysql+mysqldb://%s:%s@%s/%s?charset=utf8' % (
    os.environ.get('MYSQL_USER'),
    os.environ.get('MYSQL_PASSWORD'),
    os.environ.get('MYSQL_HOST'),
    os.environ.get('MYSQL_DATABASE'),
)

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE,
    )
)

Base = declarative_base()
Base.query = session.query_property()
