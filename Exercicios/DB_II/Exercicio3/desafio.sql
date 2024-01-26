DELIMITER //

CREATE PROCEDURE LevantamentoDiario(IN dataConsulta DATE)
BEGIN
    SELECT
        data_venda AS Data,
        COUNT(*) AS QuantidadeProdutos
    FROM
        vendas
    WHERE
        DATE(data_venda) = dataConsulta
    GROUP BY
        data_venda;
END //

DELIMITER ;
