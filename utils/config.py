from enum import Enum
class Enum:
    def __repr__(self):
        return self.value

class Config(Enum):
    url = 'sqlite:///database.db'
    