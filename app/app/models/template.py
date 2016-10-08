# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, server_default=text("nextval('company_id_seq'::regclass)"))
    name = Column(String(45), server_default=text("''::character varying"))
    site = Column(String(45), server_default=text("''::character varying"))
    address = Column(String(100), server_default=text("''::character varying"))
    industry = Column(String(45), server_default=text("''::character varying"))
    email = Column(String(45), server_default=text("''::character varying"))
    phone = Column(String(45), server_default=text("''::character varying"))


class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True, server_default=text("nextval('position_id_seq'::regclass)"))
    title = Column(String(45), server_default=text("''::character varying"))
    city = Column(String(45), server_default=text("''::character varying"))
    address = Column(String(100), server_default=text("''::character varying"))
    industry = Column(String(45), server_default=text("''::character varying"))
    email = Column(String(45), server_default=text("''::character varying"))
    phone = Column(String(45), server_default=text("''::character varying"))
    description = Column(String(500), server_default=text("''::character varying"))
    detail_url = Column(String(500), unique=True, server_default=text("''::character varying"))
    list_url = Column(String(500), server_default=text("''::character varying"))
    create_time = Column(DateTime, server_default=text("now()"))
    update_time = Column(DateTime, server_default=text("now()"))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, server_default=text("nextval('user_id_seq'::regclass)"))
    name = Column(String(40), server_default=text("''::character varying"))
    age = Column(Integer, server_default=text("0"))
