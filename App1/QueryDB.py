# -*- coding: UTF-8 -*-
import MySQLdb
import traceback

# open connection
db = MySQLdb.connect("localhost", "py", "123456", "pydb");
# 用cursor()方法获取操作游标
cursor = db.cursor();
# 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()");

# 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone();

# print "Database version : %s " % data;

# cursor.execute("DROP TABLE IF EXISTS TEST_DB");

# 创建数据表SQL语句
sql = """CREATE TABLE TEST_DB (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(10),
         INCOME FLOAT)"""

# cursor.execute(sql);


# insert
insert_sql = """insert into TEST_DB(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES ('arvin','Chang',26,'male',1000.0);"""

# try:
#     count=0;
#     for index in range(1,20):
#         data=cursor.execute(insert_sql);
#         count+=data;
#     print count;
#     db.commit();
# except Exception, e:
#     print 'str(Exception):\t', str(Exception)
#     print 'str(e):\t\t', str(e)
#     print 'repr(e):\t', repr(e)
#     print 'e.message:\t', e.message
#     print 'traceback.print_exc():'; traceback.print_exc()
#     print 'traceback.format_exc():\n%s' % traceback.format_exc()
#     db.rollback();

update_sql = """update TEST_DB set age=28"""
# try:
#     data=cursor.execute(update_sql);
#     print data;
#     db.commit();
# except Exception,e:
#     print 'str(Exception):\t', str(Exception)
#     print 'str(e):\t\t', str(e)
#     print 'repr(e):\t', repr(e)
#     print 'e.message:\t', e.message
#     print 'traceback.print_exc():'; traceback.print_exc()
#     print 'traceback.format_exc():\n%s' % traceback.format_exc()
#     db.rollback();

query_testdb_sql = """select * from test_db"""

try:
    cursor.execute(query_testdb_sql);
    results = cursor.fetchall();

    list_test = list();

    for row in results:
        frist_name = row[0];
        last_name = row[1];
        age = row[2];
        sex = row[3];
        #         print frist_name,sex;
        #         testDB=TestDB;
        #         testDB.first_name=frist_name;
        #         testDB.last_name=last_name;
        #         testDB.age=age;
        #         list_test.__add__(testDB);
        li = {'first_name': frist_name, 'last_name': last_name, 'age': age, 'sex': sex};
        list_test.append(li);
    print list_test.__len__();
    print list_test;
    for li in list_test:
        if li.get('first_name') == 'arvin':
            print li.get('first_name')
        else:
            print 'false'

        if li.has_key('last_name'):
            print 'has key last_name'
        else:
            print 'not found key last_name'
except Exception, e:
    print 'str(Exception):\t', str(Exception)
    print 'str(e):\t\t', str(e)
    print 'repr(e):\t', repr(e)
    print 'e.message:\t', e.message
    print 'traceback.print_exc():';
    traceback.print_exc()
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    db.rollback();

# close connection
db.close();