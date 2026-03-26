import pandas as pd

# Simulando as 3 "bases"
clientes = pd.DataFrame({'id_cliente': [1, 2], 'nome': ['Joao', 'Maria']})
interacoes = pd.DataFrame({'id_cliente': [1, 1, 2], 'campanha': ['Black Friday', 'Natal', 'Black Friday'], 'abriu_email': [1, 0, 1]})

# União dos dados
df_final = pd.merge(interacoes, clientes, on="id_cliente", how="left")

# Salvando o resultado
df_final.to_csv('base_pronta_crm.csv', index=False)
print("Pipeline concluído com sucesso!")
