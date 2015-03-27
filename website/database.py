__author__ = 'wei'
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
import pymysql as sql
engine = create_engine('mysql://weixc1234:wxc16888@cloud.comtnuycjpkv.us-west-2.rds.amazonaws.com/cloud', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

#init_db()

keyword = "man"
query = "%" + keyword + "%"

print query
