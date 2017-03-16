'''ORM = Object-relational mapping

Define the fields of your objects; which maps to the structure of rows in your database
- Can request a list of objects (DB is queried & object/list of objects is returned)
- Can create an object, and it can be saved to DB
- Can manipulate objects, and updates are saved to DB'''
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from base import Base
from coin import Coin


#Engine represents the core interface to the database

#The first argument is the url of the database;
#this points to a sqlitedb saved in a file called phone.db
#echo=True turns on SQLAlchemy logging for debugging

engine = create_engine('sqlite:///coins.db', echo = False)

#Base = declarative_base() #All of the mapped classes inherit from this class
Base.metadata.create_all(engine) #Create a table for all the classes that use Base

'''Need a session to talk to the database'''
#A session manages mappings of objects to rows in the database
#Make a session class -- only need to do this one time
Session = sessionmaker(bind=engine) #using the engine created earlier



def setup():
    #Ask the session to instantiate a session object
    #Use the session object to talk to DB
    save_session = Session()

    # #Create a merch object; use named args to set values of the object
    # item1 = Merch(description = 'Band Shirt', price = 20)
    # item2 = Merch(description = 'Band CD', price = 10)
    # item3 = Merch(description = 'Sticker/Pin', price = 5)

    # for merch in [item1, item2, item3]:
    #     #if it doesn't already exist
    #     if not (getItem(merch.description)):
    #         #Add merch object to session -- this tells the session that you want to map
    #         # the merch object to a row in the DB
    #         save_session.add(merch)
    #         # The merch is pending - not yet saved
    #         # Doesn't save to DB until session is committed, or closed

    # Commit to save changes
    save_session.commit() #now merch should be saved in DB
    save_session.close()
