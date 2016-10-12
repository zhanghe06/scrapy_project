-- 创建表
DROP TABLE IF EXISTS public."service_v4";
CREATE TABLE "service_v4" (
  id                SERIAL NOT NULL,
  service_title     VARCHAR(100) DEFAULT '', -- 服务名称
  service_pub_date  DATE, -- 服务发布日期
  service_district  VARCHAR(100) DEFAULT '', -- 服务地区
  contact_user      VARCHAR(100) DEFAULT '', -- 联系人
  contact_phone     VARCHAR(100) DEFAULT '', -- 电话
  company_name      VARCHAR(100) DEFAULT '', -- 公司名称
  company_home_page VARCHAR(500) DEFAULT '', -- 公司主页
  company_district  VARCHAR(500) DEFAULT '', -- 公司地区
  company_address   VARCHAR(500) DEFAULT '', -- 公司地址
  company_reg_date  DATE, -- 公司注册日期
  fetch_platform    SMALLINT     DEFAULT 0, -- 抓取平台
  fetch_city_code   VARCHAR(100) DEFAULT '', -- 抓取城市编码
  fetch_cate_code   VARCHAR(100) DEFAULT '', -- 抓取分类编码
  fetch_detail_url  VARCHAR(500) DEFAULT '', -- 抓取详情链接
  fetch_list_url    VARCHAR(500) DEFAULT '', -- 抓取列表链接
  fetch_page_num    INTEGER      DEFAULT 0, -- 抓取列表页码
  verified_personal SMALLINT     DEFAULT 0, -- 个人验证标识
  verified_company  SMALLINT     DEFAULT 0, -- 公司验证标识
  export_flag       SMALLINT     DEFAULT 0, -- 导出标识
  create_time       TIMESTAMP    DEFAULT CURRENT_TIMESTAMP, -- 创建时间
  update_time       TIMESTAMP    DEFAULT CURRENT_TIMESTAMP, -- 更新时间
  PRIMARY KEY (id),
  UNIQUE (fetch_detail_url)
);
-- 表说明
COMMENT ON TABLE "service_v4" IS '服务表';
-- 字段说明
COMMENT ON COLUMN "service_v4".id IS '主键ID';
COMMENT ON COLUMN "service_v4".service_title IS '服务名称';
COMMENT ON COLUMN "service_v4".service_pub_date IS '服务发布日期';
COMMENT ON COLUMN "service_v4".service_district IS '服务地区';
COMMENT ON COLUMN "service_v4".contact_user IS '联系人';
COMMENT ON COLUMN "service_v4".contact_phone IS '电话';
COMMENT ON COLUMN "service_v4".company_name IS '公司名称';
COMMENT ON COLUMN "service_v4".company_home_page IS '公司主页';
COMMENT ON COLUMN "service_v4".company_district IS '公司地区';
COMMENT ON COLUMN "service_v4".company_address IS '公司地址';
COMMENT ON COLUMN "service_v4".company_reg_date IS '公司注册日期';
COMMENT ON COLUMN "service_v4".fetch_platform IS '抓取平台（5：58同城；1：自行添加的站外资源）';
COMMENT ON COLUMN "service_v4".fetch_city_code IS '抓取城市编码';
COMMENT ON COLUMN "service_v4".fetch_cate_code IS '抓取分类编码';
COMMENT ON COLUMN "service_v4".fetch_detail_url IS '抓取详情链接';
COMMENT ON COLUMN "service_v4".fetch_list_url IS '抓取列表链接';
COMMENT ON COLUMN "service_v4".fetch_page_num IS '抓取列表页码';
COMMENT ON COLUMN "service_v4".verified_personal IS '个人验证标识';
COMMENT ON COLUMN "service_v4".verified_company IS '公司验证标识';
COMMENT ON COLUMN "service_v4".export_flag IS '导出标识';
COMMENT ON COLUMN "service_v4".create_time IS '创建时间';
COMMENT ON COLUMN "service_v4".update_time IS '更新时间';
-- 创建索引
CREATE INDEX idx_service_contact_phone
  ON "service_v4" (contact_phone);
CREATE INDEX idx_service_company_name_idx
  ON "service_v4" (company_name);
