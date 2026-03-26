import pandas as pd

#Dados de quem recebeu o e-mail
envios = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4, 5],
    'campanha': ['Black Friday', 'Black Friday', 'Natal', 'Natal', 'Natal']
})

#Dados de quem abriu o e-mail
aberturas = pd.DataFrame({
    'id_cliente': [1, 3, 5],
    'abriu': [1, 1, 1]
})

#Quem não está na lista de aberturas vai == "0" (não abriu)
df_final = pd.merge(envios, aberturas, on='id_cliente', how='left').fillna(0)

#Salvar o resultado pronto para o Dashboard
df_final.to_csv('output/base_performance.csv', index=False)
print("Pipeline executado! Dados prontos em /output")
