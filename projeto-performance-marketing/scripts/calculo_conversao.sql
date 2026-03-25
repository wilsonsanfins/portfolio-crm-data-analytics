-- Query para analisar a performance real das campanhas
SELECT 
    campanha,
    COUNT(*) as total_envios,
    SUM(abriu) as total_aberturas,
    (SUM(abriu) * 100.0 / COUNT(*)) as taxa_abertura
FROM performance_campanhas
GROUP BY campanha;