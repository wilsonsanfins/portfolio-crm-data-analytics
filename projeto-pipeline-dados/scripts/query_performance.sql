SELECT 
  campanha,
  COUNT(*) as total_envios,
  SUM(abriu_email) as aberturas
FROM interacoes
GROUP BY campanha;