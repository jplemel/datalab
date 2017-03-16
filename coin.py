from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.engine import Engine

from base import Base
'''Listen for DB connections to enforce Foreign Key constraints'''
@event.listens_for(Engine, "connect")

def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Coin(Base):

    '''Defines metadata about a coins table. Will create Merch objects from rows in this table'''

    __tablename__ = 'coins'

    #Columms: ID, State, Year Issued, Description
    #These attributes will be column names, and have the types specified

    id = Column(Integer, primary_key=True)
    state = Column(String)
    yearIssued = Column(Integer)
    description = Column(String)

    def __repr__(self):

        '''Returns string representation of this object, helpful for debugging'''
        #This method gets called when a Merch object is printed

        return 'Coin: Id = {} State = {} Year Issued = {} Description = {}'.format(self.id, self.state, self.yearIssued, self.description)

#update the DB schema to enforce foreign key constraints
engine = create_engine('sqlite:///coins.db', echo=False)
Base.metadata.create_all(engine)
