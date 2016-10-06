-- 创建表
DROP TABLE IF EXISTS public."user";
CREATE TABLE "user" (
  id   SERIAL NOT NULL,
  name VARCHAR(40) DEFAULT '', -- 姓名
  age  INTEGER     DEFAULT 0, -- 年龄
  PRIMARY KEY (id)
);
-- 表说明
COMMENT ON TABLE "user" IS '用户表';
-- 字段说明
COMMENT ON COLUMN "user".id IS '主键ID';
COMMENT ON COLUMN "user".name IS '姓名';
COMMENT ON COLUMN "user".age IS '年龄';

-- 创建表
DROP TABLE IF EXISTS public."company";
CREATE TABLE "company" (
  id       SERIAL NOT NULL,
  name     VARCHAR(45)  DEFAULT '', -- 名称
  site     VARCHAR(45)  DEFAULT '', -- 网站
  address  VARCHAR(100) DEFAULT '', -- 地址
  industry VARCHAR(45)  DEFAULT '', -- 行业
  email    VARCHAR(45)  DEFAULT '', -- 邮箱
  phone    VARCHAR(45)  DEFAULT '', -- 电话
  PRIMARY KEY (id)
);
-- 表说明
COMMENT ON TABLE "company" IS '公司表';
-- 字段说明
COMMENT ON COLUMN "company".id IS '主键ID';
COMMENT ON COLUMN "company".name IS '名称';
COMMENT ON COLUMN "company".site IS '网站';
COMMENT ON COLUMN "company".address IS '地址';
COMMENT ON COLUMN "company".industry IS '行业';
COMMENT ON COLUMN "company".email IS '邮箱';
COMMENT ON COLUMN "company".phone IS '电话';

-- 创建表
DROP TABLE IF EXISTS public."position";
CREATE TABLE "position" (
  id          SERIAL NOT NULL,
  title       VARCHAR(45)  DEFAULT '', -- 名称
  city        VARCHAR(45)  DEFAULT '', -- 地区
  address     VARCHAR(100) DEFAULT '', -- 地址
  industry    VARCHAR(45)  DEFAULT '', -- 行业
  email       VARCHAR(45)  DEFAULT '', -- 邮箱
  phone       VARCHAR(45)  DEFAULT '', -- 电话
  description VARCHAR(500) DEFAULT '', -- 描述
  detail_url  VARCHAR(500) DEFAULT '', -- 抓取页面
  list_url    VARCHAR(500) DEFAULT '', -- 列表链接
  create_time TIMESTAMP    DEFAULT CURRENT_TIMESTAMP, -- 创建时间
  update_time TIMESTAMP    DEFAULT CURRENT_TIMESTAMP, -- 更新时间
  PRIMARY KEY (id),
  UNIQUE (detail_url)
);
-- 表说明
COMMENT ON TABLE "position" IS '职位表';
-- 字段说明
COMMENT ON COLUMN "position".id IS '主键ID';
COMMENT ON COLUMN "position".title IS '名称';
COMMENT ON COLUMN "position".city IS '地区';
COMMENT ON COLUMN "position".address IS '地址';
COMMENT ON COLUMN "position".industry IS '行业';
COMMENT ON COLUMN "position".email IS '邮箱';
COMMENT ON COLUMN "position".phone IS '电话';
COMMENT ON COLUMN "position".description IS '描述';
COMMENT ON COLUMN "position".create_time IS '创建时间';
COMMENT ON COLUMN "position".update_time IS '更新时间';

-- 创建表
DROP TABLE IF EXISTS public."service";
CREATE TABLE "service" (
  id          SERIAL NOT NULL,
  title       VARCHAR(45)  DEFAULT '', -- 名称
  city        VARCHAR(45)  DEFAULT '', -- 地区
  address     VARCHAR(100) DEFAULT '', -- 地址
  industry    VARCHAR(45)  DEFAULT '', -- 行业
  email       VARCHAR(45)  DEFAULT '', -- 邮箱
  phone       VARCHAR(45)  DEFAULT '', -- 电话
  description VARCHAR(500) DEFAULT '', -- 描述
  detail_url  VARCHAR(500) DEFAULT '', -- 抓取页面
  list_url    VARCHAR(500) DEFAULT '', -- 列表链接
  create_time TIMESTAMP    DEFAULT CURRENT_TIMESTAMP, -- 创建时间
  update_time TIMESTAMP    DEFAULT CURRENT_TIMESTAMP, -- 更新时间
  PRIMARY KEY (id),
  UNIQUE (detail_url)
);
-- 表说明
COMMENT ON TABLE "service" IS '服务表';
-- 字段说明
COMMENT ON COLUMN "service".id IS '主键ID';
COMMENT ON COLUMN "service".title IS '名称';
COMMENT ON COLUMN "service".city IS '地区';
COMMENT ON COLUMN "service".address IS '地址';
COMMENT ON COLUMN "service".industry IS '行业';
COMMENT ON COLUMN "service".email IS '邮箱';
COMMENT ON COLUMN "service".phone IS '电话';
COMMENT ON COLUMN "service".description IS '描述';
COMMENT ON COLUMN "service".create_time IS '创建时间';
COMMENT ON COLUMN "service".update_time IS '更新时间';
-- 创建索引
CREATE INDEX service_phone_idx ON service (phone);
