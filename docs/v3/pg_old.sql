CREATE SEQUENCE origin_service_v3_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;


CREATE SEQUENCE origin_provider_v3_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;


--
-- PostgreSQL database dump
--

-- Dumped from database version 8.4.20
-- Dumped by pg_dump version 9.5.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: origin_service_v3; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE origin_service_v3 (
    id bigint DEFAULT nextval('origin_service_v3_id_seq'::regclass) NOT NULL,
    source_type smallint DEFAULT 0,
    title character varying(500),
    provider_name character varying(500),
    source_cid character varying(200),
    summary character varying(500),
    phone character varying(500),
    city_id character varying(100) DEFAULT 0,
    city_name character varying(50),
    service_area character varying(500),
    page_num integer DEFAULT 0,
    industry character varying(100),
    source_sid character varying(200),
    classify_url character varying(255),
    detail_url character varying(1024),
    url_md5 character(32),
    pub_time timestamp(6) without time zone,
    fetch_time timestamp(6) without time zone,
    clean_flag smallint DEFAULT 0,
    publisher character varying(100),
    picture character varying(500),
    export_flag smallint DEFAULT 0,
    identity_verify smallint DEFAULT 0
);


ALTER TABLE origin_service_v3 OWNER TO postgres;

--
-- Name: COLUMN origin_service_v3.classify_url; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_service_v3.classify_url IS '分类入口';


--
-- Name: COLUMN origin_service_v3.publisher; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_service_v3.publisher IS '发布人';


--
-- Name: COLUMN origin_service_v3.picture; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_service_v3.picture IS '服务图片';


--
-- Name: COLUMN origin_service_v3.export_flag; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_service_v3.export_flag IS '0=待导出  1=已导出  2=不导出  3=出错';


--
-- Name: COLUMN origin_service_v3.identity_verify; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_service_v3.identity_verify IS '个人身份认证状态
0= 未认证
1=已认证';


--
-- Name: origin_service_v3_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY origin_service_v3
    ADD CONSTRAINT origin_service_v3_pkey PRIMARY KEY (id);


--
-- Name: unique_servicename_v3; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY origin_service_v3
    ADD CONSTRAINT unique_servicename_v3 UNIQUE (source_type, title);


--
-- Name: CONSTRAINT unique_servicename_v3 ON origin_service_v3; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON CONSTRAINT unique_servicename_v3 ON origin_service_v3 IS '服务名称';


--
-- Name: idx_ori_service_v3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_ori_service_v3 ON origin_service_v3 USING btree (source_type, source_sid);


--
-- PostgreSQL database dump complete
--


--
-- PostgreSQL database dump
--

-- Dumped from database version 8.4.20
-- Dumped by pg_dump version 9.5.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: origin_provider_v3; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE origin_provider_v3 (
    id bigint DEFAULT nextval('origin_provider_v3_id_seq'::regclass) NOT NULL,
    source_type smallint DEFAULT 0,
    full_name character varying(500),
    city_name character varying(50),
    logo_path character varying(500),
    homepage character varying(255),
    industry character varying(100),
    attr character varying(255),
    scale character varying(50),
    source_cid character varying(200),
    address character varying(500),
    service_circle character varying(500),
    classify_url character varying(255),
    url_md5 character(32),
    fetch_time timestamp(6) without time zone,
    clean_flag smallint DEFAULT 0,
    phone character varying(255),
    city_id character varying(100),
    export_flag smallint DEFAULT 0,
    vip58_year smallint,
    vip58_index smallint,
    star real DEFAULT 0.0,
    reserve integer DEFAULT 0,
    evaluate integer DEFAULT 0,
    license_verify smallint DEFAULT 0
);


ALTER TABLE origin_provider_v3 OWNER TO postgres;

--
-- Name: COLUMN origin_provider_v3.phone; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.phone IS '联系电话';


--
-- Name: COLUMN origin_provider_v3.export_flag; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.export_flag IS '0=待导出  1=已导出  2=不导出  3=出错';


--
-- Name: COLUMN origin_provider_v3.vip58_year; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.vip58_year IS '网邻通年数';


--
-- Name: COLUMN origin_provider_v3.vip58_index; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.vip58_index IS '网邻通指数';


--
-- Name: COLUMN origin_provider_v3.star; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.star IS '星级';


--
-- Name: COLUMN origin_provider_v3.reserve; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.reserve IS '预约人数';


--
-- Name: COLUMN origin_provider_v3.evaluate; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.evaluate IS '评价次数';


--
-- Name: COLUMN origin_provider_v3.license_verify; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN origin_provider_v3.license_verify IS '营业执照认证状态：
0= 未认证
1= 已认证 ';


--
-- Name: origin_provider_v3_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY origin_provider_v3
    ADD CONSTRAINT origin_provider_v3_pkey PRIMARY KEY (id);


--
-- Name: unique_fullname_v3; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY origin_provider_v3
    ADD CONSTRAINT unique_fullname_v3 UNIQUE (full_name, source_type);


--
-- Name: CONSTRAINT unique_fullname_v3 ON origin_provider_v3; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON CONSTRAINT unique_fullname_v3 ON origin_provider_v3 IS '公司名称';


--
-- Name: idx_ori_provider_v3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_ori_provider_v3 ON origin_provider_v3 USING btree (source_type, source_cid);


--
-- PostgreSQL database dump complete
--
