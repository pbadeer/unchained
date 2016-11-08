CREATE USER IF NOT EXISTS `unchained_user`@localhost IDENTIFIED BY 'asdfasdfasdf';
CREATE DATABASE IF NOT EXISTS `unchained_db` CHARACTER SET utf8;
GRANT ALL PRIVILEGES ON `unchained_db`.* TO `unchained_user`@localhost;