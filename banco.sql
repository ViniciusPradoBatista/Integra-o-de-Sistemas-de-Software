CREATE DATABASE loja;
USE loja;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    fornecedor VARCHAR(100) NOT NULL,
    endereco_fornecedor VARCHAR(200) NOT NULL,
    quantidade INT NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    preco_unitario FLOAT NOT NULL
);

INSERT INTO produtos (nome, fornecedor, endereco_fornecedor, quantidade, endereco, preco_unitario) 
VALUES
    ('Produto A', 'Fornecedor 1', 'Rua A, 123', 10, 'Rua B, 456', 50.0),
    ('Produto B', 'Fornecedor 2', 'Rua C, 789', 20, 'Rua D, 101', 30.0),
    ('Produto C', 'Fornecedor 3', 'Rua E, 112', 15, 'Rua F, 131', 40.0),
    ('Produto D', 'Fornecedor 4', 'Rua G, 415', 5, 'Rua H, 161', 60.0);

SELECT * FROM produtos;