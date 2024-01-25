-- Desenvolva um banco de dados e relacione tabelas através de chaves estrangeiras ou nomes de colunas iguais. Siga as instruções:
-- crie uma base de dados; 
-- crie tabelas nessa base de dados;
-- em cada tabela, adicione atributos;
-- insira dados em cada tabela;
-- utilize os comandos Joins para realizar consultas nas tabelas. 

CREATE DATABASE escola;

USE escola;

CREATE TABLE aluno (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100),
  email VARCHAR(100),
  endereco VARCHAR(255)
);

CREATE TABLE professor (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100),
  email VARCHAR(100),
  endereco VARCHAR(255),
  id_aluno INT,
  FOREIGN KEY (id_aluno) REFERENCES aluno(id)
);

INSERT INTO aluno (nome, email, endereco)
VALUES ('Aluno 1', 'aluno1@email.com', 'Endereço do Aluno 1'),
       ('Aluno 2', 'aluno2@email.com', 'Endereço do Aluno 2'),
       ('Aluno 3', 'aluno3@email.com', 'Endereço do Aluno 3');

INSERT INTO professor (nome, email, endereco, id_aluno)
VALUES ('Professor 1', 'professor1@email.com', 'Endereço do Professor 1', 1),
       ('Professor 2', 'professor2@email.com', 'Endereço do Professor 2', 2),
       ('Professor 3', 'professor3@email.com', 'Endereço do Professor 3', 3);

SELECT *
FROM aluno
JOIN professor ON aluno.id = professor.id_aluno;