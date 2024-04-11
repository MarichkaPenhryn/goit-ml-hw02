-- Table: status
DROP TABLE IF EXISTS table_status;
CREATE TABLE table_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO table_status ( status_name)
VALUES ( 'new'), ( 'in progress'), ( 'completed');


-- Table: users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100)UNIQUE NOT NULL

);

-- Table: tasks
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    task_description TEXT NOT NULL,
    status_id INTEGER,
    user_id INTEGER,
    
    FOREIGN KEY (status_id) REFERENCES table_status (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    
    FOREIGN KEY (user_id) REFERENCES users (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
