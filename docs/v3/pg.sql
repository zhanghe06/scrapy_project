-- 创建表
DROP TABLE IF EXISTS public."origin_service_v3";
CREATE TABLE "origin_service_v3" (
  id              SERIAL NOT NULL,
  source_type     SMALLINT      DEFAULT 0,
  title           VARCHAR(500)  DEFAULT '',
  provider_name   VARCHAR(500)  DEFAULT '',
  source_cid      VARCHAR(200)  DEFAULT '',
  summary         VARCHAR(500)  DEFAULT '',
  phone           VARCHAR(500)  DEFAULT '',
  city_id         VARCHAR(100)  DEFAULT 0,
  city_name       VARCHAR(50)   DEFAULT '',
  service_area    VARCHAR(500)  DEFAULT '',
  page_num        INTEGER       DEFAULT 0,
  industry        VARCHAR(100)  DEFAULT '',
  source_sid      VARCHAR(200)  DEFAULT '',
  classify_url    VARCHAR(255)  DEFAULT '',
  detail_url      VARCHAR(1024) DEFAULT '',
  url_md5         CHAR(32)      DEFAULT '',
  pub_time        DATE,
  fetch_time      TIMESTAMP     DEFAULT CURRENT_TIMESTAMP,
  clean_flag      SMALLINT      DEFAULT 0,
  publisher       VARCHAR(100)  DEFAULT '',
  picture         VARCHAR(500)  DEFAULT '',
  export_flag     SMALLINT      DEFAULT 0,
  identity_verify SMALLINT      DEFAULT 0,
  PRIMARY KEY (id),
  UNIQUE (detail_url)
);
-- 表说明
COMMENT ON TABLE "origin_service_v3" IS '服务表';
-- 字段说明
COMMENT ON COLUMN "origin_service_v3".id IS '主键ID';
COMMENT ON COLUMN "origin_service_v3".source_type IS '来源网站';
COMMENT ON COLUMN "origin_service_v3".title IS '服务标题';
COMMENT ON COLUMN "origin_service_v3".provider_name IS '服务商、公司名称';
COMMENT ON COLUMN "origin_service_v3".source_cid IS '原始cid';
COMMENT ON COLUMN "origin_service_v3".summary IS '服务简介';
COMMENT ON COLUMN "origin_service_v3".phone IS '电话';
COMMENT ON COLUMN "origin_service_v3".city_id IS '城市id';
COMMENT ON COLUMN "origin_service_v3".city_name IS '城市名称';
COMMENT ON COLUMN "origin_service_v3".service_area IS '服务地区';
COMMENT ON COLUMN "origin_service_v3".page_num IS '页码';
COMMENT ON COLUMN "origin_service_v3".industry IS '行业';
COMMENT ON COLUMN "origin_service_v3".source_sid IS '原始service_id';
COMMENT ON COLUMN "origin_service_v3".classify_url IS '来源页面';
COMMENT ON COLUMN "origin_service_v3".detail_url IS '详细页面';
COMMENT ON COLUMN "origin_service_v3".url_md5 IS '详细页面md5';
COMMENT ON COLUMN "origin_service_v3".pub_time IS '发布时间';
COMMENT ON COLUMN "origin_service_v3".fetch_time IS '抓取时间';
COMMENT ON COLUMN "origin_service_v3".clean_flag IS '清洗标记';
COMMENT ON COLUMN "origin_service_v3".publisher IS '发布人';
COMMENT ON COLUMN "origin_service_v3".picture IS '服务图片';
COMMENT ON COLUMN "origin_service_v3".export_flag IS '导出标记';
COMMENT ON COLUMN "origin_service_v3".identity_verify IS '个人身份认证状态';
-- 创建索引
CREATE INDEX service_provider_name_idx
  ON origin_service_v3 (provider_name);

-- 创建表
DROP TABLE IF EXISTS public."origin_provider_v3";
CREATE TABLE "origin_provider_v3" (
  id             SERIAL NOT NULL,
  source_type    SMALLINT     DEFAULT 0,
  full_name      VARCHAR(500) DEFAULT '',
  city_name      VARCHAR(50)  DEFAULT '',
  logo_path      VARCHAR(500) DEFAULT '',
  homepage       VARCHAR(255) DEFAULT '',
  industry       VARCHAR(100) DEFAULT '',
  attr           VARCHAR(255) DEFAULT '',
  scale          VARCHAR(50)  DEFAULT '',
  source_cid     VARCHAR(200) DEFAULT '',
  address        VARCHAR(500) DEFAULT '',
  service_circle VARCHAR(500) DEFAULT '',
  classify_url   VARCHAR(255) DEFAULT '',
  fetch_time     DATE,
  clean_flag     SMALLINT     DEFAULT 0,
  phone          VARCHAR(255) DEFAULT '',
  city_id        VARCHAR(100) DEFAULT '',
  export_flag    SMALLINT     DEFAULT 0,
  vip58_year     SMALLINT     DEFAULT 0,
  vip58_index    SMALLINT     DEFAULT 0,
  star           REAL         DEFAULT 0.0,
  reserve        INTEGER      DEFAULT 0,
  evaluate       INTEGER      DEFAULT 0,
  license_verify SMALLINT     DEFAULT 0,
  PRIMARY KEY (id),
  UNIQUE (source_type, full_name, phone)
);
-- 表说明
COMMENT ON TABLE "origin_provider_v3" IS '服务商家表';
-- 字段说明
COMMENT ON COLUMN "origin_provider_v3".id IS '主键ID';
COMMENT ON COLUMN "origin_provider_v3".source_type IS '来源网站';
COMMENT ON COLUMN "origin_provider_v3".full_name IS '服务标题';
COMMENT ON COLUMN "origin_provider_v3".city_name IS '城市名';
COMMENT ON COLUMN "origin_provider_v3".logo_path IS '公司logo';
COMMENT ON COLUMN "origin_provider_v3".homepage IS '公司链接';
COMMENT ON COLUMN "origin_provider_v3".industry IS '公司行业';
COMMENT ON COLUMN "origin_provider_v3".attr IS '属性、分类';
COMMENT ON COLUMN "origin_provider_v3".scale IS '规模';
COMMENT ON COLUMN "origin_provider_v3".source_cid IS '原始cid';
COMMENT ON COLUMN "origin_provider_v3".address IS '服务商地址';
COMMENT ON COLUMN "origin_provider_v3".service_circle IS '服务商圈';
COMMENT ON COLUMN "origin_provider_v3".classify_url IS '分类入口url';
COMMENT ON COLUMN "origin_provider_v3".fetch_time IS '抓取时间';
COMMENT ON COLUMN "origin_provider_v3".clean_flag IS '清洗标记';
COMMENT ON COLUMN "origin_provider_v3".phone IS '联系电话';
COMMENT ON COLUMN "origin_provider_v3".city_id IS '城市id';
COMMENT ON COLUMN "origin_provider_v3".export_flag IS '导出标记';
COMMENT ON COLUMN "origin_provider_v3".vip58_year IS '网邻通年数';
COMMENT ON COLUMN "origin_provider_v3".vip58_index IS '网邻通指数';
COMMENT ON COLUMN "origin_provider_v3".star IS '星级';
COMMENT ON COLUMN "origin_provider_v3".reserve IS '预约人数';
COMMENT ON COLUMN "origin_provider_v3".evaluate IS '评价次数';
COMMENT ON COLUMN "origin_provider_v3".license_verify IS '营业执照认证状态，公司认证状态';

-- 创建索引
CREATE INDEX service_full_name_idx
  ON origin_provider_v3 (full_name);
