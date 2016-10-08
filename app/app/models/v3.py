# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, Integer, SmallInteger, String, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict


class OriginProviderV3(Base):
    __tablename__ = 'origin_provider_v3'
    __table_args__ = (
        UniqueConstraint('source_type', 'full_name', 'phone'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('origin_provider_v3_id_seq'::regclass)"))
    source_type = Column(SmallInteger, server_default=text("0"))
    full_name = Column(String(500), index=True, server_default=text("''::character varying"))
    city_name = Column(String(50), server_default=text("''::character varying"))
    logo_path = Column(String(500), server_default=text("''::character varying"))
    homepage = Column(String(255), server_default=text("''::character varying"))
    industry = Column(String(100), server_default=text("''::character varying"))
    attr = Column(String(255), server_default=text("''::character varying"))
    scale = Column(String(50), server_default=text("''::character varying"))
    source_cid = Column(String(200), server_default=text("''::character varying"))
    address = Column(String(500), server_default=text("''::character varying"))
    service_circle = Column(String(500), server_default=text("''::character varying"))
    classify_url = Column(String(255), server_default=text("''::character varying"))
    fetch_time = Column(Date)
    clean_flag = Column(SmallInteger, server_default=text("0"))
    phone = Column(String(255), server_default=text("''::character varying"))
    city_id = Column(String(100), server_default=text("''::character varying"))
    export_flag = Column(SmallInteger, server_default=text("0"))
    vip58_year = Column(SmallInteger, server_default=text("0"))
    vip58_index = Column(SmallInteger, server_default=text("0"))
    star = Column(Float, server_default=text("0.0"))
    reserve = Column(Integer, server_default=text("0"))
    evaluate = Column(Integer, server_default=text("0"))
    license_verify = Column(SmallInteger, server_default=text("0"))


class OriginServiceV3(Base):
    __tablename__ = 'origin_service_v3'

    id = Column(Integer, primary_key=True, server_default=text("nextval('origin_service_v3_id_seq'::regclass)"))
    source_type = Column(SmallInteger, server_default=text("0"))
    title = Column(String(500), server_default=text("''::character varying"))
    provider_name = Column(String(500), index=True, server_default=text("''::character varying"))
    source_cid = Column(String(200), server_default=text("''::character varying"))
    summary = Column(String(500), server_default=text("''::character varying"))
    phone = Column(String(500), server_default=text("''::character varying"))
    city_id = Column(String(100), server_default=text("0"))
    city_name = Column(String(50), server_default=text("''::character varying"))
    service_area = Column(String(500), server_default=text("''::character varying"))
    page_num = Column(Integer, server_default=text("0"))
    industry = Column(String(100), server_default=text("''::character varying"))
    source_sid = Column(String(200), server_default=text("''::character varying"))
    classify_url = Column(String(255), server_default=text("''::character varying"))
    detail_url = Column(String(1024), unique=True, server_default=text("''::character varying"))
    url_md5 = Column(String(32), server_default=text("''::bpchar"))
    pub_time = Column(Date)
    fetch_time = Column(DateTime, server_default=text("now()"))
    clean_flag = Column(SmallInteger, server_default=text("0"))
    publisher = Column(String(100), server_default=text("''::character varying"))
    picture = Column(String(500), server_default=text("''::character varying"))
    export_flag = Column(SmallInteger, server_default=text("0"))
    identity_verify = Column(SmallInteger, server_default=text("0"))
