import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT * FROM tasks WHERE status_id =  (SELECT id FROM table_status WHERE status_name = 'new');
"""

print(execute_query(sql))