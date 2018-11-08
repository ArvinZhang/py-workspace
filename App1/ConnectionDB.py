# -*- coding: UTF-8 -*-

import MySQLdb


def connctionMySQL():
    # open connection
    db = MySQLdb.connect("localhost", "py", "123456", "pydb")

    # 用cursor()方法获取操作游标
    cursor = db.cursor()

    query_sql = """select * from test_db limit 10"""

    cursor.execute(query_sql)

    results = cursor.fetchall   ()

    for row in results:
        print row[2]
        print id(row[2])
        print row[4]

    # len
    print len(results)

    cursor.close()
    db.close()
