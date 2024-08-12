from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer

class Base:
    # The next 2 lines are needed _before_ data classes / sql tables are defined
    Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.


class Container(Base):
    __tablename__ = "container"  # name of table in SQL database
    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    destination = Column(String)


def __repr__(self):  # Optional. Only for test purposes.
    return f"Container({self.id=:4}    {self.weight=:5}    {self.destination=})"


def convert_to_tuple(self):  # Convert Container to tuple
    return self.id, self.weight, self.destination


def valid(self):
    try:
        value = int(self.weight)
    except ValueError:
        return False
    return value >= 0


@staticmethod
def convert_from_tuple(tuple_):  # Convert tuple to Container
    container = Container(id=tuple_[0], weight=tuple_[1], destination=tuple_[2])
    return container
