create database studentsNotesManagement;
use studentsNotesManagement;
create table users(
id bigint unsigned auto_increment primary key,
name varchar(100) not null,
email varchar(255) not null unique,
password_hash varchar(255) not null,
is_verified boolean not null default false,
created_at timestamp default current_timestamp
);
desc users;
create table notes(
id bigint unsigned auto_increment primary key,
user_id bigint unsigned not null,
title varchar(150) not null,
content text not null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
foreign key (user_id) references users(id) on delete cascade
);

create table file_data(
id bigint unsigned auto_increment primary key,
user_id bigint unsigned not null,
orginal_name varchar(255) not null,
stored_name varchar(255) not null,
mime_type varchar(120) not null,
size_bytes bigint unsigned not null,
storage_path varchar(500),
foreign key (user_id) references users(id) on delete cascade
);




