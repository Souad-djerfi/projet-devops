
use mysql;
CREATE USER app identified BY '';
GRANT ALL privileges ON * . * TO app;
FLUSH PRIVILEGES;
use test;
CREATE TABLE messages(id int PRIMARY KEY AUTO_INCREMENT, message varchar(255));
FLUSH PRIVILEGES;