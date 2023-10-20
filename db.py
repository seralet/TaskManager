import pymysql
import yaml

class SQL:
    def __init__(self):
        config = yaml.safe_load(open('./config.yml'))['mysql']
        self.db = pymysql.connect(
		host=config['host'],
                user=config['user'],
		password=config['password'],
		database=config['database']
		)
				

    def __del__(self):
        self.db.close()

    def get_all_tasks(self):
        sql = 'select * from Tasks'
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
