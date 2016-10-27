CREATE USER IF NOT EXISTS 'unchained_user' identified BY 'asdfasdfasdf';
CREATE DATABASE IF NOT EXISTS unchained_db CHARACTER SET utf8;
GRANT ALL ON unchained_db.* TO 'unchained_user';