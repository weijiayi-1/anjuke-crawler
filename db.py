import pymysql
from config import DB_CONFIG

TABLE_NAME = 'ershoufang_list'

FIELDS = [
    '标题', '户型', '面积', '方位', '楼层', '时间', '所属小区', '所属区域', '总价', '均价', '房龄'
]

CREATE_TABLE_SQL = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    标题 VARCHAR(255),
    户型 VARCHAR(64),
    面积 VARCHAR(64),
    方位 VARCHAR(64),
    楼层 VARCHAR(64),
    时间 VARCHAR(64),
    所属小区 VARCHAR(255),
    所属区域 VARCHAR(255),
    总价 VARCHAR(64),
    均价 VARCHAR(64),
    房龄 VARCHAR(32)
) CHARACTER SET utf8mb4;
"""

class DB:
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(CREATE_TABLE_SQL)
        self.conn.commit()

    def insert_data(self, data: dict):
        keys = ','.join(FIELDS)
        values = ','.join(['%s'] * len(FIELDS))
        sql = f"INSERT INTO {TABLE_NAME} ({keys}) VALUES ({values})"
        vals = [data.get(f, '') for f in FIELDS]
        self.cursor.execute(sql, vals)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close() 