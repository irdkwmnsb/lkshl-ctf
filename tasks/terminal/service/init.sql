CREATE USER 'dbuser'@'%' IDENTIFIED BY 'kjgeqwss';
GRANT SELECT ON cpanel.* TO 'dbuser'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE cpanel;

USE cpanel;

CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  login VARCHAR(30) NOT NULL,
  password VARCHAR(32) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO users VALUES (1, 'admin', '09f9995c3a50bc2471bcc7aff49e668f');