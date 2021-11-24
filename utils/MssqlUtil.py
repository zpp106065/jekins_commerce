from utils.LogUtil import my_log
import pymssql


# 1、创建封装类
class Mssql:
    # 2、初始化数据，连接数据库，光标对象
    def __init__(self,host,user,password,database,charset="utf-8",port=3306):
        self.log = my_log()
        self.conn = pymssql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
            )
        self.cur = self.conn.cursor()

    # 3、创建查询、执行方法
    def fetchone(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def fetchall(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self,sql):
        """
        执行
        :return:
        """
        try:
            if self.conn and self.cur:
                self.cur.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mssql 执行失败")
            self.log.error(ex)
            return False
        return True

# 4、关闭对象
    def close_mysql(self):
        # 关闭光标对象
        # if self.cur is not None:
        self.cur.close()
        # 关闭连接对象
        # if self.conn is not None:
        self.conn.close()


if __name__ == "__main__":
    mssql = Mssql("ec2-54-212-203-216.us-west-2.compute.amazonaws.com",
                  "amz_app",
                  "1qaz^YHN*IK",
                  "commerce",
                  charset="utf8",
                  )
    res = mssql.fetchone("select vendor_account,amazon_account from Commerce_Vendor_Account")
    print(res)


"""
import pymssql
# 2、连接database
conn = pymssql.connect(
    host="ec2-54-212-203-216.us-west-2.compute.amazonaws.com",
    user="amz_app",
    password="1qaz^YHN*IK",
    database="commerce",
    charset="UTF8"
)
# 3、获取执行sql的光标对象
cursor = conn.cursor()
# 4、执行sql
sql = "select vendor_account,amazon_account from Commerce_Vendor_Account"
cursor.execute(sql)
res = cursor.fetchone()
print(res)
# 5、关闭对象
cursor.close()
"""
