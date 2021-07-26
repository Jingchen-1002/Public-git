# -*- coding:utf-8 -*-
# @Author:chenjing

import pymysql
import selenium.webdriver.support.color

"""
    This is mysql connect
"""

_HOST = '127.0.0.1'
_PORT = 426
_USER = 'root'
_DB = 'api-test'
_PASSWORD = '123456'


class DataBase:
    """
    This is base with mysql connect
    """

    def __init__(self):
        try:
            self.connection = pymysql.connect(host=_HOST,
                                              port=_PORT,
                                              user=_USER,
                                              password=_PASSWORD,
                                              database=_DB)
        except Exception as e:
            print('Connect Failed %s' % e)

    # clear table
    def clear(self, table_name: str) -> None:
        """
        table
        :param tablename: str
        :return:
        """
        real_sql = 'delete from' + table_name + ';'
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    # insert
    def insert(self, table_name: str, table_data: dict) -> None:
        """
        insert
        :param table_name:
        :param table_data
        :return:
        """
        for key in table_data:
            table_data[key] = "'" + table_data[key] + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = 'INSERT INTO' + table_name + '(' + key + ')' + 'VALUES' + '(' + value + ')'

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    # close
    def close(self):
        """
        close
        :return:
        """
        self.connection.close()

    # init data
    def init_data(self, data: str, datas: dict) -> None:
        """
        init
        :return:
        """
        for table, data in datas.items():
            self.clear(table)
            for item in data:
                self.insert(table, item)
            self.close()


def main() -> None:
    data_name = DataBase()
    table_name = 'test_name'
    data = {'aaa': 1, 'bbb': 2, 'ccc': 3}
    data_name.clear(table_name)
    data_name.insert(table_name, data)
    data_name.close()


if __name__ == '__main__':
    main()
