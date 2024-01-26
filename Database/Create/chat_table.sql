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




-- ALTER TABLE interview_friend
-- ADD FOREIGN KEY (user_id) REFERENCES user(user_id);
