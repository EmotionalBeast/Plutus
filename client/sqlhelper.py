from dbutils.pooled_db import PooledDB
import pymysql

# 全局变量定义连接池，只加载一次
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=5,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    ping=0,
    host='172.16.0.103',
    port=3306,
    user='root',
    password='123456',
    database='plutus',
    charset='utf8'
)


class SQLHelper(object):

    def __init__(self):
        self.conn = None
        self.cur = None

    def open(self):
        conn = POOL.connection()  # 去连接池中获取一个连接
        cur = conn.cursor()
        return conn, cur

    def close(self, conn, cur):
        cur.close()
        conn.close()  # 将连接放回到连接池，并不会关闭连接，当线程终止时，连接自动关闭

    def get_list(self, sql, args=None):
        """
        获取所有数据
        :param sql: SQL语句
        :param args: SQL语句的占位参数
        :return: 查询结果
        """
        conn, cur = self.open()
        cur.execute(sql, args)
        result = cur.fetchall()
        self.close(conn, cur)
        return result

    def get_one(self, sql, args=None):
        """
        获取单条数据
        :return: 查询结果
        """
        conn, cur = self.open()
        cur.execute(sql, args)
        result = cur.fetchone()
        self.close(conn, cur)
        return result

    def modify(self, sql, args=None):
        """
        修改、增加、删除操作
        :return: 受影响的行数
        """
        conn, cur = self.open()
        result = cur.execute(sql, args)
        conn.commit()
        self.close(conn, cur)
        return result

    def bulk_modify(self, sql, args=None):
        """
        批量修改、增加、删除操作
        :return: 受影响的行数
        """
        conn, cur = self.open()
        result = cur.executemany(sql, args)
        conn.commit()
        self.close(conn, cur)
        return result

    def create(self, sql, args=None):
        """
        增加数据
        :return: 新增数据行的ID
        """
        conn, cur = self.open()
        cur.execute(sql, args)
        conn.commit()
        self.close(conn, cur)
        return cur.lastrowid

    def __enter__(self):
        self.conn, self.cur = self.open()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
