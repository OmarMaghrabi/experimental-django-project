CREATE DATABASE IF NOT EXISTS social_media;
USE social_media;

CREATE TABLE IF NOT EXISTS table_user(
	id INT,
    username VARCHAR(50),
    email VARCHAR(255),
    passkey VARCHAR(255),
    
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS table_post(
	id INT,
    fk_user_id INT,
    post_text VARCHAR(255),
    time_posted DATETIME,
    
    PRIMARY KEY (id),
    FOREIGN KEY (fk_user_id) REFERENCES table_user(id)
);

CREATE TABLE IF NOT EXISTS table_post_img(
	id INT,
	fk_post_id INT,
    img_path VARCHAR(255),
    
    PRIMARY KEY (id),
    FOREIGN KEY (fk_post_id) REFERENCES table_post(id)
);

CREATE TABLE IF NOT EXISTS table_post_vid(
	id INT,
	fk_post_id INT,
    vid_path VARCHAR(255),
    
    PRIMARY KEY (id),
    FOREIGN KEY (fk_post_id) REFERENCES table_post(id)
);

CREATE TABLE IF NOT EXISTS table_post_comments(
	id INT,
	fk_user_id INT,
    fk_post_id INT,
	comment_text VARCHAR(255),
    
	PRIMARY KEY (id),
	FOREIGN KEY (fk_user_id) REFERENCES table_user(id),
    FOREIGN KEY (fk_post_id) REFERENCES table_post(id)
);

CREATE TABLE IF NOT EXISTS table_likes_saves(
	id INT,
	fk_user_id INT,
	fk_post_id INT,
	liked BOOL,
	saved BOOL,


	PRIMARY KEY (id),
	FOREIGN KEY (fk_user_id) REFERENCES table_user(id),
    FOREIGN KEY (fk_post_id) REFERENCES table_post(id)
);

