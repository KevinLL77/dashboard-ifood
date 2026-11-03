import sqlite3
import random
from datetime import datetime, timedelta

# Conecta ou cria o banco de dados SQLite local
conn = sqlite3.connect('pedidos_ifood.db')
cursor = conn.cursor()

# Cria a tabela de pedidos
cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    id TEXT PRIMARY KEY,
    cliente TEXT,
    restaurante TEXT,
    valor REAL,
    tempo_entrega_minutos INTEGER,
    meta_sla_minutos INTEGER,
    status TEXT,
    data TIMESTAMP
)
''')

# Dados para simulação
restaurantes = ["iFood Hub Morumbi", "Burger King Centro", "Pizza Hut Zona Sul", "Sushi Express"]
status_opcoes = ["Entregue", "Entregue", "Entregue", "Atrasado", "Cancelado"]

# Gerar 100 pedidos simulados
for i in range(1, 101):
    pedido_id = f"ORD-2026-{1000 + i}"
    cliente = f"Cliente {i}"
    restaurante = random.choice(restaurantes)
    valor = round(random.uniform(25.0, 180.0), 2)
    meta_sla = 45
    tempo_entrega = random.randint(25, 65)
    
    # Se o tempo passar do SLA, ajusta status para Atrasado
    status = "Atrasado" if tempo_entrega > meta_sla else random.choice(status_opcoes)
    data = datetime.now() - timedelta(days=random.randint(0, 7), hours=random.randint(0, 23))

    cursor.execute('''
    INSERT INTO pedidos (id, cliente, restaurante, valor, tempo_entrega_minutos, meta_sla_minutos, status, data)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (pedido_id, cliente, restaurante, valor, tempo_entrega, meta_sla, status, data.strftime('%Y-%m-%d %H:%M:%S')))

conn.commit()
conn.close()
print("Banco de dados 'pedidos_ifood.db' criado com sucesso com 100 pedidos!")