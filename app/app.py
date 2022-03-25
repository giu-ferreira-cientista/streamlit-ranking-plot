import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import streamlit as st

# função para carregar o dataset
@st.cache
def get_data():
    return pd.read_csv("data/populacao.csv")

def load_pacient(paciente):
    paciente_joao = {
        "id": 1,
        "first_name": "Joao",
        "last_name": "Andrade",
        "idade": 44,
        "peso": 90,
        "altura": 180
    }

    paciente_mariana = {
        "id": 2,
        "first_name": "Mariana",
        "last_name": "Andrade",
        "idade": 35,
        "peso": 57,
        "altura": 154
    }

    paciente_antonio = {
        "id": 3,
        "first_name": "Antonio",
        "last_name": "Andrade",
        "idade": 20,
        "peso": 110,
        "altura": 190
    }

    paciente_camila = {
        "id": 4,
        "first_name": "Camila",
        "last_name": "Andrade",
        "idade": 18,
        "peso": 47,
        "altura": 160
    }

    if paciente == 0:
        return paciente_joao

    if paciente == 1:
        return paciente_mariana
    
    if paciente == 2:
        return paciente_antonio

    if paciente == 3:
        return paciente_camila



def show_data(paciente):
    # criando um dataframe
    st.write("Gerando gráficos incríveis...")
    
    dict_paciente = load_pacient(paciente)

    total = len(df_total)
    
    # Grafico de Peso
    peso_usuario = dict_paciente["peso"]

    df_menor = df_total[df_total['peso'] < peso_usuario]

    total_menor = len(df_menor)

    posicao = (1 - (total_menor / total)) * 100

    x = df_total["peso"].value_counts().sort_index().index.values
    y = df_total["peso"].value_counts().sort_index().values

    
    max_y = max(y) + 2
    max_ys = max_y + 3

    markers_on_x = [peso_usuario]
    markers_on_xs = [peso_usuario]
    markers_on_y = [max_y]
    markers_on_ys = [max_ys]

    fig = plt.figure(figsize = (19, 7))    
    fig.suptitle(dict_paciente["first_name"] + " é mais leve do que " + str(posicao) + '% das pessoas', fontsize=20)
    plt.xlabel("Peso das Pessoas", fontsize=18)
    plt.ylabel("Número de Pessoas", fontsize=18)
    plt.xticks(fontsize=14, rotation=90)
    plt.yticks(fontsize=14, rotation=90)
    plt.plot(markers_on_x, markers_on_y, 'v', markersize=30)
    plt.plot(markers_on_xs, markers_on_ys, 'r', markersize=35, marker='$VOCÊ$')
    plt.fill_between(x, y, color='#539ecd')
    df_total['peso'].value_counts().sort_index().plot(kind='line',figsize=(19,7))
    plt.grid()
    st.pyplot(fig)

    st.markdown("""<hr style="height:1px;border:none;color:blue;background-color:blue;" /> """, unsafe_allow_html=True)

    # Grafico de Altura
    altura_usuario = dict_paciente["altura"]

    df_menor = df_total[df_total['altura'] < altura_usuario]

    total_menor = len(df_menor)

    posicao = (1 - (total_menor / total)) * 100

    x = df_total["altura"].value_counts().sort_index().index.values
    y = df_total["altura"].value_counts().sort_index().values

    
    max_y = max(y) + 2
    max_ys = max_y + 3

    markers_on_x = [altura_usuario]
    markers_on_xs = [altura_usuario]
    markers_on_y = [max_y]
    markers_on_ys = [max_ys]

    fig = plt.figure(figsize = (19, 7))    
    fig.suptitle(dict_paciente["first_name"] + " é mais alto(a) do que " + str(posicao) + '% das pessoas', fontsize=20)
    plt.xlabel("Altura das Pessoas", fontsize=18)
    plt.ylabel("Número de Pessoas", fontsize=18)
    plt.xticks(fontsize=14, rotation=90)
    plt.yticks(fontsize=14, rotation=90)
    plt.plot(markers_on_x, markers_on_y, 'v', markersize=30)
    plt.plot(markers_on_xs, markers_on_ys, 'r', markersize=35, marker='$VOCÊ$')
    plt.fill_between(x, y, color='#539ecd')
    df_total['altura'].value_counts().sort_index().plot(kind='line',figsize=(19,7))
    plt.grid()
    st.pyplot(fig)

    st.markdown("""<hr style="height:1px;border:none;color:blue;background-color:blue;" /> """, unsafe_allow_html=True)
    
    # Grafico de Idade
    idade_usuario = dict_paciente["idade"]

    df_menor = df_total[df_total['idade'] < idade_usuario]

    total_menor = len(df_menor)

    posicao = (1 - (total_menor / total)) * 100

    x = df_total["idade"].value_counts().sort_index().index.values
    y = df_total["idade"].value_counts().sort_index().values

    
    max_y = max(y) + 2
    max_ys = max_y + 3

    markers_on_x = [idade_usuario]
    markers_on_xs = [idade_usuario]
    markers_on_y = [max_y]
    markers_on_ys = [max_ys]

    fig = plt.figure(figsize = (19, 7))    
    fig.suptitle(dict_paciente["first_name"] + " é mais jovem do que " + str(posicao) + '% das pessoas', fontsize=20)
    plt.xlabel("Idade das Pessoas", fontsize=18)
    plt.ylabel("Número de Pessoas", fontsize=18)
    plt.xticks(fontsize=14, rotation=90)
    plt.yticks(fontsize=14, rotation=90)
    plt.plot(markers_on_x, markers_on_y, 'v', markersize=30)
    plt.plot(markers_on_xs, markers_on_ys, 'r', markersize=35, marker='$VOCÊ$')
    plt.fill_between(x, y, color='#539ecd')
    df_total['idade'].value_counts().sort_index().plot(kind='line',figsize=(19,7))
    plt.grid()
    st.pyplot(fig)



# Carrega o dataframe
df_total = get_data()

# criando a interface no Streamlit
# título
st.title("App - Ranking de Saúde")

# subtítulo
st.markdown("Esta é uma Aplicação para que os médicos consultem o estado geral de um paciente, comparado com outros individuos da população de uma base de dados.")

# verificando o dataset
st.subheader("Segue uma pequena amostra de pacientes:")

# atributos para serem exibidos por padrão
defaultcols = ["id","first_name","last_name","idade","peso","altura"]

# defindo atributos a partir do multiselect
cols = st.multiselect("Atributos", defaultcols, default=defaultcols)

# exibindo os top 10 registro do dataframe
st.dataframe(df_total[cols].head(10))


st.sidebar.subheader("Escolha um paciente:")

# inserindo os pacientes que vao servir de amostra
PACIENTES = {0: "Joao", 1 : "Mariana", 2: "Antonio", 3: "Camila"}

#retorna a descricao do bairro pelo codigo
def desc_paciente(paciente):
    return PACIENTES[paciente]

# cria uma caixa de selecao com os pacientes para o usuario escolher um
paciente = st.sidebar.selectbox("Nome do Paciente", options=list(PACIENTES.keys()), format_func=desc_paciente)
st.sidebar.write(f"Você selecionou o paciente {paciente} chamado {desc_paciente(paciente)}")

# inserindo um botão na tela
btn_show = st.sidebar.button("Mostrar o Ranking")

# verifica se o botão foi acionado
if btn_show:
    # pega o nome do paciente 
    result = desc_paciente(paciente)

    st.subheader("O paciente escolhido foi: ")    
    
    # imprime o resultado na tela
    st.write(result)

    # imprime os graficos do paciente
    show_data(paciente)

