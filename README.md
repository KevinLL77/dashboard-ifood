# 🔴 iFood | Operations, SLA & AI Analytics

<p align="center">
  <b>Painel analítico de desempenho logístico, monitoramento de SLA e predição de atrasos com Machine Learning.</b>
</p>

---

## 🚀 Sobre o Projeto
Este projeto simula um cenário real de **operações e logística de entregas no setor de delivery**. Além de fornecer uma visão em tempo real da eficiência das operações e do controle de SLA, o painel agora integra **Inteligência Artificial e Machine Learning** para gerar diagnósticos executivos automáticos e prever riscos de atraso em novos pedidos.

A interface foi desenhada seguindo a identidade visual corporativa, priorizando uma experiência de usuário limpa, intuitiva e altamente interativa.

---

## 🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando um ecossistema moderno voltado para análise de dados e IA:
* **Python** (Linguagem principal)
* **Streamlit** (Construção da interface web interativa)
* **Pandas** (Manipulação e estruturação dos dados)
* **Plotly** (Gráficos dinâmicos e modernos)
* **Scikit-learn** (Modelo preditivo de Regressão Logística para Machine Learning)
* **SQLite** (Armazenamento local e persistência dos pedidos)

---

## 🧠 Principais Funcionalidades & Recursos de IA
* **🤖 Assistente de IA (Diagnóstico Operacional):** Analisa os dados filtrados em tempo real e gera um sumário executivo automático destacando gargalos e recomendações operacionais.
* **🔮 Simulador Preditivo de Risco (Machine Learning):** Um modelo de Regressão Logística treinado com os dados do banco para calcular a probabilidade de atraso de um pedido com base no valor e na meta de SLA.
* **📊 Métricas e KPIs em Tempo Real:** Volume total de pedidos, faturamento consolidado, tempo médio de entrega e taxa de atraso baseada em metas.
* **📈 Gráficos Interativos (Plotly):** Distribuição percentual do status e análise comparativa de tempo médio por restaurante.

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/KevinLL77/dashboard-ifood.git](https://github.com/KevinLL77/dashboard-ifood.git)
   cd dashboard-ifood
   dashboard-ifood/
│
├── app.py              # Código principal da interface e modelos de IA (Streamlit & Scikit-learn)
├── gerar_dados.py      # Script Python para geração da base SQLite simulada
├── pedidos_ifood.db    # Banco de dados local com 100+ registros de pedidos
└── requirements.txt    # Dependências e bibliotecas do projeto