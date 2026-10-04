# Curso Análise de Dados com Python - Hashtag
# Aula 4: Sistema de Vendas e Gestão Online

# Passo a passo do projeto:
# Passo 1: Criar a tela do sistema (front end)
    # Seção Cadastrar Vendas
        # Campo Data
        # Campo Vendedor - Ana, Bruno, Carla
        # Campo Produto - Notebook, Fone, Celular
        # Campo Quantidade
        # Campor Valor
        # Botão Cadastrar Vendas
            # Quando clicar no botão -> adicionar a venda na tabela e atualizar tudo na tela
    # Seção Vendas Cadastadas
        # Tabela com as vendas
    # Seção Dashboard
        # Card/Mértica -> Faturamento Total
        # Gráfico de Barra/Coluna -> Venda por vendedor
        # Gráfico de Pizza -> Venda por Produto

# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos


# pip install streamlit pandas plotly -> já instalados
import streamlit as st # cria sites
import pandas as pd # cria base de dados
import plotly.express as px # cria gráficos

# Passo 1: Criar a tela do sistema
st.write("# Sistema de Vendas") # Título

tabela_vendas = pd.read_csv("vendas.csv") # Carregar a base de vendas

# Passo 2: Criar o formulário de cadastro
st.sidebar.write("## Cadastrar venda")
data = st.sidebar.date_input("Data") # em barra lateral, a variável data receberá o campo de "Data", do tipo date_input
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"]) # em barra lateral, a variável vendedeor receberá o campo de "Vendedor", do tipo selectbox, com alista ["Ana", "Bruno", "Carla"] 
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1) # em barra lateral, a quantidade receberá o campo de "Quantidade", do tipo number_input, de 1 em 1
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar venda") # em barra lateral, a variável botao receberá o campo de "Cadastar Venda", do tipo button

# Passo 3: Salvar a venda na base de dados
if botao_cadastrar: # se clicar no botão "Cadastrar vendas"
    # nova_venda = [data, vendedor, produto, quantidade, valor] # criar uma lista com essas variáveis 
    nova_venda = [str(data), vendedor, produto, quantidade, valor] # data em formato de texto (string)
    tabela_vendas.loc[len(tabela_vendas)] = nova_venda # "loc" = localize/adicione em; "len" = lenght (altura); "len(tabela)" -> altura da tabela_vendas (quantidade de linhas, da linha 0 a última -> a última linha)
    # ultima_linha = len(tabela_vendas)
    # tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False) # a partir tabela_vendas (from), criar uma (to) .csv (o banco de dados); sem (False) o índice (index) das vendas
    st.success("Venda cadastrada!") # criar uma mensagem de sucesso

# Passo 4: Mostrar a base de dados na tela
st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas) # dataframe é tabela no Pandas; usando st.dataframe, o Streamlite entende que é uma tabela do Pandas

# Passo 5: Criar o dashboard
st.write("## Dashboard")
faturamento = tabela_vendas["valor"].sum() # A variável faturamento recebe a soma dos valores da coluna "valor" da "tabela_vendas"
st.metric("Faturamento total", f"R${faturamento}") # se tiver uma variável (faturamento) dentro de um texto ("R$ faturamento"), coloca-se um "f" antes do texto e a variável entre chaves {faturamento} 
# st.metric("Faturamento total", faturamento) -> assim sai só o faturamento, sem textos

grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto") # cores por produto
st.plotly_chart(grafico1) # para exibir o gráfico do Plotly na tela do site
# grafico1.show() # assim, o gráfico seria exibido no terminal

grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5) # "pie" -> "torta" - no BR chamamos "pizza"; hole=0.5 -> inserir um buraco de 50% no meio do gráfico (vira gráfico de rosca) 
st.plotly_chart(grafico2)

# streamlit run main.py -> rodar em novo terminal; streamlit cria o site
