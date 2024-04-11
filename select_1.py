import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
#-------------------select 1------------------
    
sql = """
SELECT * FROM tasks WHERE user_id = 1;
"""

#print(execute_query(sql))

#-------------------select 2 ------------------

sql = """
SELECT * FROM tasks WHERE status_id =  (SELECT id FROM table_status WHERE status_name = 'new');
"""

#print(execute_query(sql))

#-------------------select 3 ------------------

sql = """
UPDATE tasks SET status_id = 2 WHERE id = 5;
"""

#print(execute_query(sql))

#-------------------select 4 ------------------

sql = """
SELECT id, fullname
FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);"""

#print(execute_query(sql))

#-------------------select 5 ------------------

sql = """
INSERT INTO tasks (title, task_description, status_id, user_id)
VALUES ('colour of button', 'make the coulr green', 1, 2);"""

#print(execute_query(sql))

#-------------------select 6 ------------------

sql = """
SELECT id, title, task_description
FROM tasks
WHERE NOT status_id == 3;"""

#print(execute_query(sql))

#-------------------select 7 ------------------

sql = """
DELETE FROM tasks
WHERE id == 1;"""

#print(execute_query(sql))

#-------------------select 8 ------------------

sql = """
SELECT fullname, email
FROM users
WHERE email LIKE 'lalalala@gmail.com'
"""

#print(execute_query(sql))

#-------------------select 9 ------------------

sql = """
UPDATE users SET fullname = 'Marichka Penhryn' WHERE id = 5;
"""

#print(execute_query(sql))

#-------------------select 10 ------------------

sql = """
SELECT COUNT(status_id) as  status_id
FROM tasks
GROUP BY status_id;"""

#print(execute_query(sql))

#-------------------select 11 ------------------

sql = """
SELECT *
FROM tasks
WHERE user_id IN (SELECT id
    FROM users
    WHERE email LIKE '%@gmail.com');
"""

#print(execute_query(sql))

#-------------------select 12 ------------------

sql = """
SELECT *
FROM tasks
WHERE task_description IS NULL;
"""

#print(execute_query(sql))

#-------------------select 13 ------------------

sql = """
SELECT u.id, u.fullname, u.email, t.title, t.task_description  
FROM users AS u
INNER JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = 2;
"""

#print(execute_query(sql))

#-------------------select 14 ------------------

sql = """
SELECT u.id, u.fullname, COUNT(t.id) as task_count
FROM users AS u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id, u.fullname;


"""

#print(execute_query(sql))