https://github.com/kelvinEL20/3334Group.git
The project is private, please contact 18053131d@connect.polyu.hk if you want access
The .exe file is in dist folder

User account for testing:
1.
username: user
pw: user
2.
username: user1
pw: user1

The application need a local database to run.
Port: 3306
Database name: 3334group
username: kelvin
password: kelvin

Tables created by:
1.
CREATE TABLE IF NOT EXISTS login_table
(
username varchar(20),
salt varchar(20),
pw_hash varchar(255),
PRIMARY KEY(username)
);

2.
CREATE TABLE IF NOT EXISTS artwork_table
(
token_id INT AUTO_INCREMENT PRIMARY KEY,
artwork_name varchar(100),
upload_datetime DATETIME,
artwork_url varchar(1000),
UNIQUE (artwork_name)
);

3.
CREATE TABLE IF NOT EXISTS the_chain
(
nonce INT AUTO_INCREMENT PRIMARY KEY,
previous_hash varchar(64),
user_name varchar(20),
user_sign varchar(64),
art_name varchar(20),
base64_art_hash varchar(64),
tran_from_to varchar(100) DEFAULT '',
upload_owner varchar(75) DEFAULT '',
current_hash varchar(64)
);
