# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, Integer, SmallInteger, String, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict


class ServiceV4(Base):
    __tablename__ = 'service_v4'

    id = Column(Integer, primary_key=True, server_default=text("nextval('service_v4_id_seq'::regclass)"))
    service_title = Column(String(100), server_default=text("''::character varying"))
    service_pub_date = Column(Date)
    service_district = Column(String(100), server_default=text("''::character varying"))
    contact_user = Column(String(100), server_default=text("''::character varying"))
    contact_phone = Column(String(100), index=True, server_default=text("''::character varying"))
    company_name = Column(String(100), index=True, server_default=text("''::character varying"))
    company_home_page = Column(String(500), server_default=text("''::character varying"))
    company_district = Column(String(500), server_default=text("''::character varying"))
    company_address = Column(String(500), server_default=text("''::character varying"))
    company_reg_date = Column(Date)
    fetch_platform = Column(SmallInteger, server_default=text("0"))
    fetch_city_code = Column(String(100), server_default=text("''::character varying"))
    fetch_cate_code = Column(String(100), server_default=text("''::character varying"))
    fetch_detail_url = Column(String(500), unique=True, server_default=text("''::character varying"))
    fetch_list_url = Column(String(500), server_default=text("''::character varying"))
    fetch_page_num = Column(Integer, server_default=text("0"))
    verified_personal = Column(SmallInteger, server_default=text("0"))
    verified_company = Column(SmallInteger, server_default=text("0"))
    export_flag = Column(SmallInteger, server_default=text("0"))
    create_time = Column(DateTime, server_default=text("now()"))
    update_time = Column(DateTime, server_default=text("now()"))
