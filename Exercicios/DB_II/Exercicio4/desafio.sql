DELIMITER //

CREATE FUNCTION SomarClientesCadastradosNoDia(dataConsulta DATE) RETURNS INT
BEGIN
    DECLARE totalClientes INT;

    SELECT COUNT(*) INTO totalClientes
    FROM clientes
    WHERE DATE(data_cadastro) = dataConsulta;

    RETURN totalClientes;
END //

DELIMITER ;


SELECT SomarClientesCadastradosNoDia('2024-01-26') AS TotalClientesCadastrados;
