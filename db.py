import pymysql
import yaml

class SQL:
    def __init__(self):
        config = yaml.safe_load(open('./config.yml'))['mysql']
        self.db = pymysql.connect(
		host=config['host'], # 2. write code to create a connection from. i.e. host=config['host']
                user=config['user'],
		password=config['password'],
		database=config['database']
		)
				

    def __del__(self):
        self.db.close()

    def get_all_tasks(self):
        sql = 'select * from Tasks' # 3. write sql query to get all from Tasks table
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
