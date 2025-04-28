create database if not exists jogo_milhao;

use jogo_milhao;

create table if not exists usuario (
	id INT PRIMARY KEY auto_increment,
    email varchar(255) not null unique,
    nome varchar(100) not null,
	senha blob not null, 
    type boolean not null
);

create table if not exists questao(
	id int primary key auto_increment,
    enunciado text not null, 
    dica text
);

create table if not exists alternativa(
	id int primary key auto_increment,
    q_id int not null, 
    enunciado text not null,
    verify boolean not null, 
    foreign key (q_id) references questao(id) on delete cascade
);

create table if not exists rodada(
	id int primary key auto_increment,
    pontuacao int not null, 
    data date not null, 
    id_usuario int not null, 
    foreign key (id_usuario) references usuario(id) on delete cascade
);