# Dashboard Automático com Streamlit

Este projeto é uma aplicação web simples que permite aos usuários carregar um arquivo CSV e visualizar gráficos a partir dos dados numéricos contidos nele. O aplicativo foi construído utilizando a biblioteca [Streamlit](https://streamlit.io/) e [Pandas](https://pandas.pydata.org/).

## Funcionalidades

- Carregamento de arquivo CSV.
- Suporte a codificação `utf-8` e `latin1` para ler os dados do CSV.
- Exibição do conteúdo do arquivo CSV na interface.
- Filtragem automática das colunas numéricas.
- Criação de gráficos de linha e barra a partir de duas colunas numéricas escolhidas pelo usuário.

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você pode verificar isso executando o seguinte comando no terminal:

```bash
python --version
```

Além disso, instale as seguintes bibliotecas Python necessárias:

```bash
pip install streamlit pandas
```

### Rodando o aplicativo

1. Salve o código no arquivo `app.py`.
2. No terminal, navegue até o diretório onde o arquivo `app.py` está localizado.
3. Execute o comando para iniciar o Streamlit:

   ```bash
   streamlit run app.py
   ```

4. Uma nova janela do navegador será aberta com a interface da aplicação.

### Utilização

1. Na interface do aplicativo, clique em "Browse files" ou "Suba seu arquivo CSV aqui!" e selecione um arquivo CSV para carregar.
2. O aplicativo tentará abrir o arquivo com codificação `utf-8`. Se falhar, tentará novamente com a codificação `latin1`.
3. Após carregar o arquivo, o conteúdo será exibido na página.
4. Se houver colunas numéricas no arquivo, você poderá escolher as colunas para os eixos X e Y, e gráficos de linha e barra serão gerados automaticamente.
5. Se as colunas para os eixos X e Y forem iguais ou se o arquivo não contiver dados numéricos suficientes, mensagens de aviso serão exibidas.

## Estrutura do Código

- `st.title`: Define o título da página.
- `st.file_uploader`: Permite o upload de arquivos CSV.
- `pd.read_csv`: Lê o arquivo CSV, tentando diferentes codificações (UTF-8 e Latin1).
- `st.write`: Exibe o dataframe completo.
- `select_dtypes`: Filtra apenas as colunas numéricas.
- `st.selectbox`: Permite que o usuário selecione colunas numéricas para criar os gráficos.
- `st.line_chart` e `st.bar_chart`: Geram gráficos de linha e barra com as colunas selecionadas.

## Tratamento de Erros

- Se o arquivo não puder ser lido com a codificação `utf-8`, a aplicação tentará abrir o arquivo com a codificação `latin1`.
- Se o arquivo estiver vazio ou não contiver dados, uma mensagem de erro será exibida.
- Se não houver colunas numéricas no arquivo, o usuário será alertado.

## Exemplo de Uso

1. Suba um arquivo CSV contendo dados numéricos.
2. Escolha as colunas para os eixos X e Y.
3. Visualize os gráficos gerados automaticamente.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou encontrar bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.
