-- Query para saber quanto cada segmento gastou no total
SELECT 
    segmento, 
    SUM(valor_compra) as total_faturado,
    COUNT(id_cliente) as qtd_clientes
FROM clientes
GROUP BY segmento;