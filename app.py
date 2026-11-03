import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="iFood - Dashboard de Performance Logística",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS customizada (Identidade Visual iFood)
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #EA1D2C;
        margin-bottom: 0rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555555;
        margin-bottom: 1.5rem;
    }
    .stMetric {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #EA1D2C;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Principal
st.markdown('<p class="main-header">🔴 iFood | Operations & SLA Analytics</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Painel de monitoramento de eficiência de entregas, cumprimento de SLA e faturamento em tempo real.</p>', unsafe_allow_html=True)

# Conexão e Carga dos Dados
@st.cache_data
def carregar_dados():
    conn = sqlite3.connect('pedidos_ifood.db')
    df = pd.read_sql_query("SELECT * FROM pedidos", conn)
    conn.close()
    df['data'] = pd.to_datetime(df['data'])
    return df

df = carregar_dados()

# Barra Lateral (Filtros)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/9/91/IFood_logo.svg", width=140)
st.sidebar.title("Filtros Operacionais")

# Filtro de Restaurante
lista_restaurantes = ["Todos"] + list(df['restaurante'].unique())
restaurante_selecionado = st.sidebar.selectbox("Selecionar Restaurante:", lista_restaurantes)

# Filtro de Status
lista_status = ["Todos"] + list(df['status'].unique())
status_selecionado = st.sidebar.selectbox("Status do Pedido:", lista_status)

# Filtrando o DataFrame
df_filtrado = df.copy()

if restaurante_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['restaurante'] == restaurante_selecionado]

if status_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['status'] == status_selecionado]

# Indicadores Chave (KPIs)
total_pedidos = len(df_filtrado)
faturamento_total = df_filtrado['valor'].sum() if total_pedidos > 0 else 0
tempo_medio = df_filtrado['tempo_entrega_minutos'].mean() if total_pedidos > 0 else 0
atrasados = len(df_filtrado[df_filtrado['status'] == 'Atrasado'])
taxa_atraso = (atrasados / total_pedidos * 100) if total_pedidos > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Volume Total de Pedidos", f"{total_pedidos:,}")
col2.metric("Faturamento Gerado", f"R$ {faturamento_total:,.2f}")
col3.metric("Tempo Médio de Entrega", f"{tempo_medio:.1f} min")
col4.metric("Taxa de Atraso (Fora do SLA)", f"{taxa_atraso:.1f}%", delta=f"{atrasados} pedidos", delta_color="inverse")

st.divider()

# Seção de Gráficos Interativos (Plotly)
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("📊 Distribuição de Pedidos por Status")
    if not df_filtrado.empty:
        fig_status = px.pie(
            df_filtrado, 
            names='status', 
            hole=0.4,
            color='status',
            color_discrete_map={'Entregue': '#2ECC71', 'Atrasado': '#E74C3C', 'Cancelado': '#95A5A6'}
        )
        fig_status.update_traces(textinfo='percent+label')
        fig_status.update_layout(showlegend=False, margin=dict(t=30, b=0, l=0, r=0))
        st.plotly_chart(fig_status, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")

with col_graf2:
    st.subheader("⏱️ Tempo Médio de Entrega por Hub/Restaurante")
    if not df_filtrado.empty:
        df_tempo = df_filtrado.groupby('restaurante')['tempo_entrega_minutos'].mean().reset_index()
        fig_tempo = px.bar(
            df_tempo,
            x='restaurante',
            y='tempo_entrega_minutos',
            text_auto='.1f',
            color_discrete_sequence=['#EA1D2C']
        )
        fig_tempo.update_layout(xaxis_title="", yaxis_title="Minutos Médios", margin=dict(t=30, b=0, l=0, r=0))
        st.plotly_chart(fig_tempo, use_container_width=True)
    else:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")

st.divider()

# Tabela Detalhada com os Registros
st.subheader("📋 Detalhamento dos Pedidos")
st.dataframe(
    df_filtrado[['id', 'data', 'restaurante', 'cliente', 'valor', 'tempo_entrega_minutos', 'status']].sort_values(by='data', ascending=False),
    column_config={
        "id": "ID do Pedido",
        "data": "Data/Hora",
        "restaurante": "Restaurante",
        "cliente": "Cliente",
        "valor": st.column_config.NumberColumn("Valor (R$)", format="R$ %.2f"),
        "tempo_entrega_minutos": st.column_config.NumberColumn("Tempo (min)", format="%d min"),
        "status": "Status de Entrega"
    },
    use_container_width=True,
    hide_index=True
)