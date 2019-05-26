#在python中使用mysql 练习
#导入模块
from pymysql import *

def main():
    #创建连接，俺的理解就是mysql -u root -p --> enter password --> use databasename
    conn = connect(host='localhost',port=3306,user='root',password='lilin123',database='liangdong',charset='utf8')
    #得到Cursor(谷歌翻译为：光标)对象
    cs = conn.cursor()
    count = cs.execute('select goods_id,goods_name from goods where shop_price<20')
    print('查询到{}条数据:'.format(count))

    for i in range(count):
        #如果有多条结果，一条一条的取
        result = cs.fetchone()
        print(result)
    #关闭Cursor对象
    cs.close()
    conn.close()

if __name__ == '__main__':
    main()
