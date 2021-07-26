# -*- coding:utf-8 -*-
# @Author:chenjing

import pymysql
from warnings import filterwarnings

# 忽略mysql告警信息

filterwarnings("ignore", category=pymysql.Warning)


# conn = pymysql.connect(
#     host="192.168.48.128",
#     user="root",
#     password="123456",
#     database="api-test")
#
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# try:
#     real_sql = "select * from `case`"
#     cursor.execute(real_sql)
#     data = cursor.fetchall()
#     print(data)
# except Exception as e:
#     print("error{}".format(e))
# finally:
#     conn.close()

class MysqlDb:

    def __init__(self):
        self.conn = pymysql.connect(
            host="192.168.48.128",
            user="root",
            password="123456",
            database="api-test"
        )
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql, state="all"):
        """
        查询
        :param sql:
        :param state: 'all'
        :return:
        """
        self.cur.execute(sql)

        if state == "all":
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()
        return data

    def execute(self, sql):
        """
        增加、删除、修改
        :param sql:
        :return:
        """
        try:
            rows = self.cur.execute(sql)
            self.conn.commit()
            return rows
        except Exception as e:
            print("数据库操作异常{}".format(e))
            self.conn.rollback()


if __name__ == '__main__':
    db = MysqlDb()
    # 查询
    # real_sql = "select * from `case`;"
    # r = db.query(real_sql)
    # print(r)
    # 插入
    # real_sql = 'insert into `case`(`app`) values ("xd")'
    # real_sql = 'insert into `case` (`app`) values ("cj")'
    # i = db.execute(real_sql)
    # print(i)
    # 修改
    # real_sql = 'update `case` set `app`="cj" where `id`=11'
    # real_sql = 'update `case` set `title`="嘻嘻嘻嘻" where `id`=11'
    # real_sql = 'update `case` set `method`="delete" where `id`=11'
    # real_sql = 'update `case` set `title`="哈哈哈哈" where `id`=12'
    # u = db.execute(real_sql)
    # print(u)
    # 删除
    # real_sql = 'delete from `case` where `id`=11'
    # d = db.execute(real_sql)
    # print(d)

