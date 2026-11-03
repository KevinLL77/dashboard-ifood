# 🔴 iFood | Operations & SLA Analytics

<p align="center">
  <b>Painel analítico de desempenho logístico, monitoramento de SLA e métricas operacionais para delivery.</b>
</p>

---

## 🚀 Sobre o Projeto
Este projeto foi desenvolvido com foco em simular um cenário real de **operações e logística de entregas**. O objetivo principal é fornecer aos gestores e equipes de operações uma visão em tempo real da eficiência das entregas, identificação de gargalos (pedidos fora do SLA) e controle do faturamento por restaurante/hub.

A interface foi desenhada seguindo a identidade visual corporativa, priorizando uma experiência de usuário (UX) limpa, intuitiva e altamente interativa.

---

## 🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando o ecossistema Python voltado para análise de dados e web apps:
* **Python** (Linguagem principal)
* **Streamlit** (Construção da interface web interativa)
* **Pandas** (Manipulação e estruturação dos dados)
* **Plotly** (Gráficos dinâmicos e modernos)
* **SQLite** (Armazenamento local e persistência dos pedidos)

---

## 📊 Principais Funcionalidades & KPIs
* **Métricas em Tempo Real:** Volume total de pedidos, faturamento consolidado, tempo médio de entrega e taxa de atraso baseada em metas de SLA.
* **Filtros Operacionais Dinâmicos:** Filtragem por restaurante específico e status de entrega (Entregue, Atrasado, Cancelado).
* **Gráficos Interativos (Plotly):** 
  * Distribuição percentual do status dos pedidos.
  * Análise comparativa do tempo médio de entrega por hub/restaurante.
* **Tabela de Detalhamento:** Listagem completa com formatação customizada de valores monetários e tempos.

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/KevinLL77/dashboard-ifood.git](https://github.com/KevinLL77/dashboard-ifood.git)
   cd dashboard-ifood
   dashboard-ifood/
│
├── app.py              # Código principal da interface do Streamlit
├── gerar_dados.py      # Script Python para geração da base SQLite simulada
├── pedidos_ifood.db    # Banco de dados local com 100+ registros de pedidos
└── requirements.txt    # Dependências e bibliotecas do projeto