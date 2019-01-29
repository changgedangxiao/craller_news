#coding=utf-8
import MySQLdb


class DBConn():
    def __init__(self, host, user, passwd, dbname,):
        try:
            self.conn = MySQLdb.connect(host, user, passwd, dbname,charset="utf8")
        except Exception as e:
            print "Database connection Error"
            print e

    def insert_data(self,sql):
        try:
            cursor=self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except Exception,e:
            print "insert error:", e

    def select_one(self,sql):
        try:
            cursor=self.conn.cursor()
            cursor.execute(sql)
            ret=cursor.fetchone()
            cursor.close()
        except Exception,e:
            print "db select error",e

        return ret

    def db_close(self):
        self.conn.close()



if __name__ == '__main__':
    db_host = "127.0.0.1"
    db_user = "root"
    db_passwd = "Tianhu201"
    db_name = "news"

    db_conn = DBConn(db_host, db_user, db_passwd, db_name)

    sql1="""select  title from NewsStories"""
    for i in db_conn.select_one(sql1):
        print i
