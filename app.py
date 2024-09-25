import streamlit as st
import pandas as pd
from pandas import errors
 
st.title("Dashboard Automático")
 
# Carregar o arquivo CSV
file = st.file_uploader(
    'Suba seu arquivo CSV aqui!',
    type=['csv']
)
 
if file:
    try:
        # Tenta abrir o arquivo com codificação utf-8
        df = pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        # Se falhar, tenta com a codificação latin1
        df = pd.read_csv(file, encoding='latin1')
    except errors.EmptyDataError:
        st.error("O arquivo está vazio ou não contém dados.")
        df = None
 
    if df is not None:
        # Exibir o dataframe completo na interface do Streamlit
        st.write(df)
 
        # Filtrar apenas as colunas numéricas
        df_numerico = df.select_dtypes(include=['float64', 'int64'])
 
        # Verificar se há colunas numéricas suficientes para gerar gráficos
        if not df_numerico.empty:
            st.subheader("Gráficos")
           
            # Escolher qual coluna usar para os gráficos
            coluna_x = st.selectbox("Escolha a coluna para o eixo X:", df_numerico.columns)
            coluna_y = st.selectbox("Escolha a coluna para o eixo Y:", df_numerico.columns)
 
            # Verificar se a coluna escolhida para Y não é a mesma que a coluna escolhida para X
            if coluna_x != coluna_y:
                # Criar gráficos
                st.line_chart(df_numerico[[coluna_x, coluna_y]])
                st.bar_chart(df_numerico[[coluna_x, coluna_y]])
            else:
                st.warning("As colunas para os eixos X e Y não podem ser as mesmas.")
        else:
            st.warning("O arquivo CSV não contém colunas numéricas suficientes para gerar gráficos")
else:
    st.warning('Ainda não tenho arquivo!')