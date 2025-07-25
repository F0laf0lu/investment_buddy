-- Setting up DB
CREATE DATABASE IF NOT EXISTS dbname CHARACTER SET utf8;

CREATE USER IF NOT EXISTS 'username'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON dbname.* TO 'username'@'localhost';