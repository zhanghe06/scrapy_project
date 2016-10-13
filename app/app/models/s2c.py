# coding: utf-8
from sqlalchemy import Column, DateTime, Index, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict


class CrawlService(Base):
    __tablename__ = 'crawl_service'
    __table_args__ = (
        Index('cateandcity', 'cate_id', 'city_id'),
    )

    id = Column(Integer, primary_key=True)
    source_type = Column(Integer, index=True, server_default=text("'0'"))
    title = Column(String(255), server_default=text("''"))
    detail_url = Column(String(255), server_default=text("''"))
    phone = Column(String(100), server_default=text("''"))
    city_id = Column(Integer, index=True)
    city_code = Column(String(20), server_default=text("''"))
    cate_id = Column(String(255), index=True, server_default=text("''"))
    service_type_code = Column(String(50), server_default=text("''"))
    publisher = Column(String(255), server_default=text("''"))
    identity_verify = Column(String(10), server_default=text("'0'"))
    provider_name = Column(String(255), server_default=text("''"))
    license_verify = Column(Integer, server_default=text("'0'"))
    star = Column(String(10), server_default=text("'0'"))
    reserve = Column(String(8), server_default=text("'0'"))
    evaluate = Column(String(8), server_default=text("'0'"))
    vip58_year = Column(String(8), server_default=text("'0'"))
    vip58_index = Column(String(8), server_default=text("'0'"))
    fetch_time = Column(DateTime, server_default=text("'0000-00-00 00:00:00'"))
    invite_time = Column(DateTime, server_default=text("'0000-00-00 00:00:00'"))
    coordinate = Column(String(50), nullable=False, server_default=text("''"))
    address = Column(String(250), server_default=text("''"))
    is_mobile = Column(Integer, server_default=text("'0'"))
    page_num = Column(Integer, server_default=text("'50'"))
    service_circle = Column(String(250), server_default=text("''"))
    service_area = Column(String(250), server_default=text("''"))
    sale_name = Column(String(50), server_default=text("'无'"))
    remark = Column(Text)
    invite_status = Column(Integer, server_default=text("'0'"))
    need_id = Column(Integer, index=True, server_default=text("'0'"))
    website = Column(String(100), server_default=text("''"))
    add_person = Column(String(20), server_default=text("''"))
    rid = Column(Integer, server_default=text("'0'"))
    is_register = Column(Integer, server_default=text("'0'"))
    register_time = Column(DateTime)
    add_mobile = Column(String(11))


class User(Base):
    __tablename__ = 'user'

    uid = Column(Integer, primary_key=True, index=True)
    mobile = Column(String(20), unique=True)
    nickname = Column(String(20), server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    status = Column(Integer, nullable=False, server_default=text("'1'"))
    image = Column(String(45), nullable=False, server_default=text("''"))
    is_active = Column(Integer, index=True, server_default=text("'1'"))
    login_pc_time = Column(DateTime)
    login_m_time = Column(DateTime)
    login_wx_time = Column(DateTime)
    last_login_time = Column(DateTime, index=True)
