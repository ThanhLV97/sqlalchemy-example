from sqlalchemy import Column, Integer, String, ForeignKey
from utils import Base


class Customer(Base):
    __tablename__ = 'Customer'
    id = Column('id', Integer, primary_key=True)
    name = Column('Name', String)
    phone = Column('Phone', String)
    address = Column('Address', String)


class Item(Base):
    """[summary]

    Args:
        Base ([type]): [description]
    """
    id = Column('id', Integer, primary_key=True)
    name = Column('Name', String)
    item_type = Column('Type', String)
    price = Column('Price', String)
