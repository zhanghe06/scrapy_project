# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), server_default=text("''"))
    site = Column(String(45), server_default=text("''"))
    address = Column(String(100), server_default=text("''"))
    industry = Column(String(45), server_default=text("''"))
    email = Column(String(45), server_default=text("''"))
    phone = Column(String(45), server_default=text("''"))


class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True)
    title = Column(String(45), server_default=text("''"))
    city = Column(String(45), server_default=text("''"))
    address = Column(String(100), server_default=text("''"))
    industry = Column(String(45), server_default=text("''"))
    email = Column(String(45), server_default=text("''"))
    phone = Column(String(45), server_default=text("''"))
    description = Column(String(500), server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), server_default=text("''"))
    age = Column(Integer, server_default=text("'0'"))
