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


-- Comandos para facilitarme la vida 
--  cd cs415_project/API/cs415/
-- python3 manage.py runserver

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

+---------+------------+-----------+------------------------+----------+---------------------+
| user_id | first_name | last_name | email                  | password | created_date        |
+---------+------------+-----------+------------------------+----------+---------------------+
|       1 | Dereck     | Angeles   | holadereck@gmail.com   | 12345    | 2024-02-09 22:24:50 |
|       2 | Sadie      | Angeles   | holasadie@gmail.com    | 12345    | 2024-02-09 22:29:40 |
|       3 | Jabir      | Angeles   | holajabir@gmail.com    | 12345    | 2024-02-09 22:32:58 |
|       4 | Michelle   | Angeles   | holaMichelle@gmail.com | 12345    | 2024-02-16 08:11:09 |
|       5 |            |           |                        | NULL     | 2024-02-16 21:10:19 |
|       6 |            |           |                        | NULL     | 2024-02-16 21:27:14 |
|       7 | hola1      | adios1    | julietajc.jj@gmail.com | NULL     | 2024-02-16 21:28:51 |
|       8 | hola12     | adios12   | 23r4tey@gmail.com      | 12345    | 2024-02-16 21:35:31 |
|       9 |            |           |                        |          | 2024-02-16 21:51:00 |
|      10 | hola2      | adios2    | 23r4tey@gmail.com      | 12345    | 2024-02-16 21:53:00 |
|      11 | hola3      | adios3    | holadereck@gmail.com   | 12345    | 2024-02-16 22:02:52 |
|      12 |            |           |                        |          | 2024-02-16 22:02:58 |
|      13 |            |           |                        |          | 2024-02-16 22:02:59 |
|      14 |            |           |                        |          | 2024-02-16 22:02:59 |
|      15 |            |           |                        |          | 2024-02-16 22:03:00 |
|      16 |            |           | asdf@gmail.com         |          | 2024-02-16 22:20:34 |
|      17 | hola5      | adios5    | adios5@gmail.com       | 12345    | 2024-03-01 21:48:07 |
|      18 | hola5      | adios5    | holadereck@gmail.com   | 12345    | 2024-03-01 21:51:39 |
|      19 | hola6      | adios6    | hola6@gmail.com        | 12345    | 2024-03-07 18:53:35 |
|      20 | hola7      | adios7    | hola7@gmail.com        | 12345    | 2024-03-07 21:09:35 |
|      21 | hola8      | adios8    | hola8@gmail.com        | 12345    | 2024-03-08 06:28:57 |
|      22 | abd        | abd       | abd@gmail.com          | 12345    | 2024-03-08 06:44:28 |
|      23 | hola9      | adios9    | hola9@gmail.com        | 12345    | 2024-03-08 06:49:06 |
|      24 | h10        | a10       | h10@gmail.com          | 12345    | 2024-03-08 06:50:49 |
|      25 | h11        | a11       | h11@gmail.com          | 12345    | 2024-03-08 07:00:04 |
|      26 | h12        | a12       | h12@gmail.com          | 12345    | 2024-03-08 07:14:12 |
|      27 | h13        | a13       | h13@gmail.com          | 12345    | 2024-03-08 09:15:48 |
|      28 | h14        | a14       | h14@gmaill.com         | 12345    | 2024-03-08 09:24:00 |
+---------+------------+-----------+------------------------+----------+---------------------+