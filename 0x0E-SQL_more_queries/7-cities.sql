-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should no

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT auto_generated NOT NULL ,
`state_id` INT NOT NULL REFERENCES `states`,
`name` VARCHAR(256)NOT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`state_id`)
REFERENCES `states`,
REFERENCES `states`(`state_id`)
);
