-- Crie um banco de dados, adicione tabelas e determine quais são os atributos de cada uma. Em seguida, execute um trigger que se relacione com algum comando, como insert, select, delete ou update.

CREATE DATABASE ESCOLA;
USE ESCOLA;

CREATE TABLE ALUNO (
  ID INT PRIMARY KEY,
  NOME VARCHAR(100),
  EMAIL VARCHAR(100),
  ENDERECO VARCHAR(255)
);

CREATE TABLE PROFESSOR (
  ID INT PRIMARY KEY,
  NOME VARCHAR(100),
  EMAIL VARCHAR(100),
  ENDERECO VARCHAR(255),
  ID_ALUNO INT,
  FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(ID)
);

CREATE TRIGGER atualiza_email_aluno
AFTER INSERT ON PROFESSOR
FOR EACH ROW
BEGIN
  UPDATE ALUNO SET EMAIL = NEW.EMAIL WHERE ID = NEW.ID_ALUNO;
END;