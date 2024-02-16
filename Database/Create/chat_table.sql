CREATE TABLE chat (
    fecha DATETIME,
    question VARCHAR(255),
    response VARCHAR(255),
    user_id INT,
);

CREATE TABLE ima2code (
    ima VARCHAR(5000),
    code VARCHAR(5000),
    user_id INT
);

CREATE TABLE interview_friend (
    name_interview VARCHAR(255),
    question VARCHAR(5000),
    response VARCHAR(5000),
    user_id INT
);


-- INSERT INTO user (first_name,last_name,email, password, created_date)
--     VALUES (
--         'Dereck',
--         'Angeles',
--         'holadereck@gmail.com',
--         '12345',
--         now()
--         );


-- Field        | Type        | Null | Key | Default | Extra          |
-- +--------------+-------------+------+-----+---------+----------------+
-- | user_id      | int         | NO   | PRI | NULL    | auto_increment |
-- | first_name   | varchar(25) | YES  |     | NULL    |                |
-- | last_name    | varchar(40) | YES  |     | NULL    |                |
-- | email        | varchar(40) | YES  |     | NULL    |                |
-- | password     | varchar(20) | YES  |     | NULL    |                |
-- | created_date | datetime    | YES  |     | NULL    |    



-- ALTER TABLE interview_friend
-- ADD FOREIGN KEY (user_id) REFERENCES user(user_id);


-- {
--     "first_name": "Jabir",
--     "last_name": "Angeles",
--     "email": "holajabir@gmail.com",
--     "password": "12345"
-- }