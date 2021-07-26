# -*- coding:utf-8 -*-
# @Author:chenjing
import pymysql


class MySQLHelper:
    """数据库"""

    def __init__(self, host, username, password, db, port=3306, charset="utf-8"):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset

    def connect(self):
        """
        连接数据库
        :return:
        """
        self.conn = pymysql.connect(host=self.host,
                                    user=self.username,
                                    password=self.password,
                                    db=self.db,
                                    port=self.port,
                                    charset=self.charset)
        # 创建游标
        self.cur = self.conn.cursor()

    def close(self):
        """关闭"""
        self.conn.close()

    def get_one(self, sql, params=()):
        """
        查询一条数据
        :param params:
        :return:
        """
        ret = None
        try:
            self.connect()
            self.cur.execute(sql, params)
            ret = self.cur.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return ret

    def get_all(self, sql, params=()):
        """
        查询所有数据
        :param sql:
        :param params:
        :return:
        """
        list_data = None
        try:
            self.connect()
            self.cur.execute(sql, params)
            list_data = self.cur.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list_data

    def __edit(self, sql, params=()):
        """
        edit
        :param sql:
        :param params:
        :return:
        """
        count = 0
        try:
            self.connect()
            count = self.cur.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count

    def insert(self, sql, params=()):
        """
        增加
        :param sql:
        :param params:
        :return:
        """
        return self.__edit(sql, params)

    def update(self, sql, params=()):
        """
        更新
        :param sql:
        :param params:
        :return:
        """
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        """
        删除
        :param sql:
        :param params:
        :return:
        """
        return self.__edit((sql, params))
