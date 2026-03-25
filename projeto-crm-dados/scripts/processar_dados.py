import pandas as pd

# 1. Simulando a criação de dados (O que o CRM exportaria)
dados = {
    'id_cliente': [1, 2, 3, 4],
    'nome': ['Joao', 'Maria', 'Jose', 'Ana'],
    'valor_compra': [1200, 300, 4500, 150],
    'dias_sem_comprar': [10, 120, 5, 200]
}

df = pd.DataFrame(dados)

# 2. Criando a regra de segmentação
# Se comprou há mais de 90 dias, é "Inativo". Se gastou mais de 2000, é "VIP".
df['status'] = df['dias_sem_comprar'].apply(lambda x: 'Ativo' if x <= 90 else 'Churn/Inativo')
df['segmento'] = df['valor_compra'].apply(lambda x: 'Premium/VIP' if x >= 2000 else 'Standard')

# 3. Salvando o resultado na pasta data
df.to_csv('data/clientes_final.csv', index=False)
print("Arquivo processado com sucesso na pasta data!")