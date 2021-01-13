#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2021/1/4 19:44 
# @File      : dbUtils.py
# @desc      :


import psycopg2
import pymysql
import redis
from common.logger import Mylog
from common.DoConfig import RWConfig

log = Mylog('dbUtils.py').getlog()


class PostgreConn:
    """Postgre数据库sql操作"""

    def __init__(self, env='test'):
        self.env = env
        if 'test' in self.env:
            self.DBconn = RWConfig().read_config_options_dict('test_db')
        elif 'pre' in self.env:
            self.DBconn = RWConfig().read_config_options_dict('pre_test')
        else:
            raise ValueError('postgre配置查询错误！请检查conf文件env配置')

    def runsql(self, sql):
        conn = psycopg2.connect(database="jhsaas", user=self.DBconn['user'], password=self.DBconn['password'],
                                host=self.DBconn['host'], port=self.DBconn['port'])
        cur = conn.cursor()
        cur.execute(sql)

    def SelectOperate(self, sql):
        conn = psycopg2.connect(database="jhsaas", user=self.DBconn['user'], password=self.DBconn['password'],
                                host=self.DBconn['host'], port=self.DBconn['port'])
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        log.info('Sql查询结果：{}'.format(rows))
        conn.close()
        return rows

    def UpdataOperate(self, sql):
        conn = psycopg2.connect(database="jhsaas", user=self.DBconn['user'], password=self.DBconn['password'],
                                host=self.DBconn['host'], port=self.DBconn['port'])
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        # rows = cur.fetchall()
        log.info('Sql更新结果：{}'.format(cur.rowcount))
        conn.close()
        return True


class mysqlconn:
    """mysql数据库sql操作"""

    def __init__(self):
        self.host = RWConfig().read_config_options_dict('mysql', 'host')
        self.user = RWConfig().read_config_options_dict('mysql', 'user')
        self.password = RWConfig().read_config_options_dict('mysql', 'password')

    def SelectOperate(self, database, sql):
        connect = pymysql.connect('192.168.200.104', self.user, self.password, database, port=3306)
        cursor = connect.cursor()
        # 执行sql
        cursor.execute(sql)
        # 获取执行结果,fetchone:获取一条；fetchall：获取所有
        result = cursor.fetchall()
        cursor.close()
        # 关闭数据库连接
        connect.close()
        return result


class RedisConn:
    """redis查询操作"""

    def __init__(self, env):
        self.env = env
        if 'test' in self.env:
            self.redisconn = RWConfig().read_config_options_dict('test_redis')
        elif 'pre' in self.env:
            self.redisconn = RWConfig().read_config_options_dict('pre_redis')
        else:
            raise ValueError('redis配置查询错误！请检查conf文件env配置')

    def redis_conn(self, key):
        print(self.redisconn)
        conn = redis.Redis(host=self.redisconn['host'], port=self.redisconn['port'], password=self.redisconn['password'], db=1)
        result = conn.get(key)
        return result

    def get_img_verify(self, key):
        # 获取图片验证码
        b = str(self.redis_conn('saas:captcha:' + key))[-5:-1]
        log.info('图片验证码：{}，写入conf文件成功！'.format(b))
        return b

    def get_phone_verify(self, phone):
        # 获取手机短信验证码
        b = self.redis_conn('ssxq:PIN:' + phone)
        log.info('短信验证码：{}'.format(int(b)))
        return b

    def get_all_wxtoken(self):
        # 获取所有wx-token，输出list
        conn = redis.Redis(host=self.redisconn['host'], port=self.redisconn['port'], password=self.redisconn['password'], db=1)
        result = conn.keys()
        token = []
        for res in result:
            res = str(res)
            if 'WXID' in res:
                wxtoken = res.split(":")[2][:-1]
                token.append(wxtoken)
        print(token)


if __name__ == '__main__':
    a = PostgreConn('test').UpdataOperate(
        "UPDATE tb_mf_mem_withdraw SET withdraw_status ='DISABLE1' where mem_id=(SELECT mem_id from tb_mf_mem_info WHERE mem_phone='13120806671') ;")
    print(a)
