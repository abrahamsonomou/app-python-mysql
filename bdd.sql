CREATE TABLE if not exists users (
    id_user int unsigned auto_increment primary key,
    username varchar(100) not null,
    login varchar(100) unique not null,
    password varchar(100),
    role int unsigned not null,
    date_create timestamp not null)
    engine=innodb charset=utf8 
    collate=utf8_general_ci;

INSERT INTO users values
  (null,'Saolomou','user1',sha1('user1'),1,null);