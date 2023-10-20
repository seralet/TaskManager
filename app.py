import argh
from db import SQL

# configure the database
sql = SQL()

# configure the app
def get_all():
    tasks = sql.get_all_tasks()
    for task in tasks:
        print(task)

argh.dispatch_commands([get_all])
