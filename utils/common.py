from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Config

Base = declarative_base()
print(Config.url)
engine = create_engine(Config.url, echo=True)
_sesion_provider = sessionmaker(bind=engine)

def session_provider():
    """[summary]
    """
    Base.metadata.create_all(bind=engine)
    return _sesion_provider()
