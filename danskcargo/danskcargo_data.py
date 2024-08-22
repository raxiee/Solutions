from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox



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

class Aircraft(Base):
    __tablename__ = "aircraft"  # name of table in SQL database
    id = Column(Integer, primary_key=True)
    max_cargo_weight = Column(Integer)
    registration = Column(String)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Aircraft({self.id=:4}    {self.max_cargo_weight=:5}    {self.registration=})"

    def convert_to_tuple(self):  # Convert Aircraft to tuple
        return self.id, self.max_cargo_weight, self.registration

    def valid(self):
        try:
            value = int(self.max_cargo_weight)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Aircraft
        aircraft = Aircraft(id=tuple_[0], max_cargo_weight=tuple_[1], registration=tuple_[2])
        return aircraft

class Transport(Base):
    __tablename__ = "transport"  # name of table in SQL database
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    container_id = Column(Integer, ForeignKey("container.id"), nullable=False)
    aircraft_id = Column(Integer, ForeignKey("aircraft.id"), nullable=False)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Container({self.id=:4}    {self.weight=:5}    {self.destination=})"

    def convert_to_tuple(self):  # Convert Transport to tuple
        return self.id, self.weight, self.destination

    def valid(self):
        try:
            value = int(self.weight)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Transport
        try:
            if tuple_[0] != '':  # unnecessary precaution?
                id_ = int(tuple_[0])
            else:
                id_ = 0
            date = parser.parse(tuple_[1])
            container_id = int(tuple_[2])
            aircraft_id = int(tuple_[3])
            # transport = Transport(id=tuple_[0], date=date, container_id=tuple_[2], aircraft_id=tuple_[3])  # unnecessary precaution?
            transport = Transport(id=id_, date=date, container_id=container_id, aircraft_id=aircraft_id)
            return transport
        except:
            messagebox.showwarning("", "Entries could not be converted to transport!")