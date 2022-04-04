import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import streamlit as st
import json
from pycaret.classification import *

# development path 
PATH_DEV = '../data'

# production path
PATH_PROD = 'data'

# change to match your enviroment
ENV_PATH = PATH_PROD


# função para carregar o dataset
#@st.cache(allow_output_mutation=True)
def get_populacao_data():
    return pd.read_csv(ENV_PATH + "/populacao.csv")

def get_paciente_data():
 
    # Opening JSON file
    f = open(ENV_PATH + '/pacientes.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    pacientes_temp = []
    for pacient in data:
        pacientes_temp.append(pacient)
        
    # Closing file
    f.close()

    return pacientes_temp


def load_pacient(paciente):
    return pacientes[paciente]


def show_data():
    # criando um dataframe
    st.write("Gerando gráficos incríveis...")
    
    #dict_paciente = load_pacient(paciente)

    total = len(df_total)
    
    # Grafico de Peso
    peso_usuario = dict_paciente['peso'] 

    df_menor = df_total[df_total['peso'] < peso_usuario]

    total_menor = len(df_menor)

    posicao = (1 - (total_menor / total)) * 100

    posicao = round(posicao, 2)
    
    x = df_total["peso"].value_counts().sort_index().index.values
    y = df_total["peso"].value_counts().sort_index().values

    
    max_y = max(y) + 2
    max_ys = max_y + 3

    markers_on_x = [peso_usuario]
    markers_on_xs = [peso_usuario]
    markers_on_y = [max_y]
    markers_on_ys = [max_ys]

    fig = plt.figure(figsize = (19, 7))    
    fig.suptitle(dict_paciente["nome"] + " é mais leve do que " + str(posicao) + '% das pessoas', fontsize=20)
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

    posicao = round(posicao, 2)


    x = df_total["altura"].value_counts().sort_index().index.values
    y = df_total["altura"].value_counts().sort_index().values

    
    max_y = max(y) + 2
    max_ys = max_y + 3

    markers_on_x = [altura_usuario]
    markers_on_xs = [altura_usuario]
    markers_on_y = [max_y]
    markers_on_ys = [max_ys]

    fig = plt.figure(figsize = (19, 7))    
    fig.suptitle(dict_paciente["nome"] + " é mais alto(a) do que " + str(posicao) + '% das pessoas', fontsize=20)
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

    posicao = round(posicao, 2)
    
    x = df_total["idade"].value_counts().sort_index().index.values
    y = df_total["idade"].value_counts().sort_index().values

    
    max_y = max(y) + 2
    max_ys = max_y + 3

    markers_on_x = [idade_usuario]
    markers_on_xs = [idade_usuario]
    markers_on_y = [max_y]
    markers_on_ys = [max_ys]

    fig = plt.figure(figsize = (19, 7))    
    fig.suptitle(dict_paciente["nome"] + " é mais jovem do que " + str(posicao) + '% das pessoas', fontsize=20)
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

    st.markdown("""<hr style="height:1px;border:none;color:blue;background-color:blue;" /> """, unsafe_allow_html=True)
    
    # Grafico de IMC    
    imc_usuario = int(dict_paciente["peso"] / ((dict_paciente["altura"] / 100) ** 2))

    df_menor = df_total[df_total['imc'] < imc_usuario]

    total_menor = len(df_menor)

    posicao = (1 - (total_menor / total)) * 100

    posicao = round(posicao, 2)
    
    x = df_total["imc"].value_counts().sort_index().index.values
    y = df_total["imc"].value_counts().sort_index().values

    
    max_y = max(y) + 2
    max_ys = max_y + 5

    markers_on_x = [imc_usuario]
    markers_on_xs = [imc_usuario]
    
    markers_on_y = [max_y]
    markers_on_ys = [max_ys]    

    fig = plt.figure(figsize = (19, 7))    
    fig.suptitle(dict_paciente["nome"] + " tem o IMC menor do que " + str(posicao) + '% das pessoas', fontsize=20)
    plt.xlabel("IMC das Pessoas", fontsize=18)
    plt.ylabel("Número de Pessoas", fontsize=18)
    plt.xticks(fontsize=14, rotation=90)
    plt.yticks(fontsize=14, rotation=90)
    plt.plot(markers_on_x, markers_on_y, 'v', markersize=30)
    plt.plot(markers_on_xs, markers_on_ys, 'r', markersize=35, marker='$VOCÊ$')
    plt.fill_between(x, y, color='#539ecd')
    df_total['imc'].value_counts().sort_index().plot(kind='line',figsize=(19,7))
    plt.grid()
    st.pyplot(fig)


def show_prescription(dict_paciente):
    
    st.subheader("Recomendações de saúde para o seu grupo no ranking: ")    

    imc_usuario = int(dict_paciente["peso"] / ((dict_paciente["altura"] / 100) ** 2))
    idade_usuario = int(dict_paciente["idade"])
    gestante = int(dict_paciente["gestante"])

    st.subheader('IMC – INDICE DE MASSA CORPORAL')

    texto_recomendacao = '''    
    A obesidade está relacionada ao aumento do risco para outras doenças como as do coração, diabetes, hipertensão arterial sistêmica, doença do fígado e diversos tipos de câncer (como o de cólon, de reto e de mama), problemas renais, asma, agravamento da covid-19, dores nas articulações, entre outras, reduzindo a qualidade e a expectativa de vida. Intervenções de saúde podem ser necessárias.\n
    CÁLCULO: Peso / altura²\n
    '''
    st.write(texto_recomendacao)
 
    resultado_modelo = '<p style="font-family:Courier; color:Blue; font-size: 20px;">'+ 'Seu IMC é: ' + str(imc_usuario) +'</p>'
    st.markdown(resultado_modelo, unsafe_allow_html=True)


    d = {'IMC (peso/altura²)': ['Menor que 18,5', '18,5 a 24,99', '25 a 29,99', 'Maior que 30'], 'ESTADO NUTRICIONAL': ['Você está com baixo peso!', 'O seu peso está adequado.', 'Alerta: sobrepeso!', 'Alerta: obesidade!']}
    
    df_imc = pd.DataFrame(data=d)

    defaultcols = ["IMC (peso/altura²)","ESTADO NUTRICIONAL"]

    # exibindo os top 10 registro do dataframe
    st.dataframe(df_imc[defaultcols].head(10))    

    st.subheader('DIABETES')

    texto_recomendacao = '''    
    Causado pela produção insuficiente ou má absorção de insulina.\n
    Surge quando há alguma disfunção na produção de insulina, um hormônio com origem no pâncreas que é essencial para a produção de energia.\n
    Tipos:\n
    - Diabete 1;\n
    - Diabete 2;\n
    - Pré-diabete;\n
    - Diabete gestacional.\n
    \nDiabete tipo 1\n
    Ocorre geralmente em crianças e adultos jovens.\n
    Causa: Surge devido a uma reação autoimune onde o corpo produz pouca ou nenhuma insulina.\n
    Sintomas: sede anormal, boca seca, perda de peso repentina, vontade de fazer xixi excessivamente, falta de energia, cansaço, fome constante e visão embaçada.\n
    Diabete tipo 2\n
    O tipo mais comum.\n
    O pâncreas produz a insulina, mas o corpo não responde a ela, o que é chamado de resistência à insulina.\n
    Uma vez que o hormônio não funciona adequadamente, os níveis de glicose no sangue continuam altos, provocando a liberação de mais insulina.\n
    Está diretamente relacionado a histórico familiar, excesso de peso, má alimentação, sedentarismo e pressão alta.\n
    Sintomas: Sede, vontade de urinar, cansaço, cicatrização lenta, infecções recorrentes na pele e dormência nas mãos e nos pés.\n
    Pré-diabete\n
    Quando os níveis de glicose no sangue estão mais altos do que o normal, mas ainda é possível reverter a situação prevenindo a evolução da doença e o aparecimento de complicações.\n
    Diabete gestacional\n
    É o tipo temporário da doença que pode acontecer durante a gravidez, trazendo risco de complicações não só durante a gestação, como no parto. As taxas de açúcar no sangue da mãe ficam acima do considerado ideal, mas ainda baixo do valor para ser classificado como diabetes tipo 2.\n
    Prevenção\n
    Não há ainda intervenção eficaz para o desenvolvimento da doença autoimune, porém, diabetes tipo 2 e o pré diabetes estão relacionados ao estilo de vida. Então é possível prevenir mantendo o peso ideal, realizando atividades físicas regularmente e com uma alimentação saudável.\n
    OBSERVAÇÃO \n
    Uma pesquisa publicada pela AMERICAN DIABETES ASSOCIATION realizada em indivíduos com pré diabetes mostrou que a intervenção com exercícios isoladamente reduziu em 46% o risco de diabetes tipo 2, enquanto a mudança do cardápio por si só, foi associada a uma redução de 31% do risco.\n
    '''
    
    st.write(texto_recomendacao) 
    
    st.subheader('INFARTO DO MIOCÁRDIO / ATAQUE CARDÍACO')

    texto_recomendacao = '''    
    É a morte das células de uma região do músculo do coração por conta da formação de um coágulo que interrompe o fluxo sanguíneo de forma súbita e intensa.\n
    Placas de gordura se acumulam no interior das artérias coronárias, chegando a obstrui-las. Na maioria dos casos, ocorre quando há o rompimento de uma dessas placas, levando à formação do coágulo e interrupção do fluxo sanguíneo. \n
    Sintomas: Principalmente dor ou desconforto na região peitoral, podendo irradiar para as costas, rosto, braço esquerdo e raramente o braço direito, sensação de peso ou aperto sobre tórax, acompanhados de suor frio, palidez, falta de ar, sensação de desmaio. A dor também pode ser no abdome, semelhante à dor de uma gastrite ou esofagite de refluxo.\n
    Causas: Os principais inimigos do infarto são o tabagismo e o colesterol em excesso, pois podem se acumular e levar à formação de placas de gordura, hipertensão, obesidade, estresse, depressão e diabetes. Os diabéticos tem duas a quatro vezes mais chances de sofrer um infarto.\n
    Prevenção: Prática de exercícios físicos, alimentação adequada, cessação do tabagismo, prevenção de doenças como a aterosclerose, diabetes e obesidade são fundamentais para evitar o entupimento das artérias e consequentemente, infarto.\n
    '''
    
    st.write(texto_recomendacao) 

    st.subheader('ATIVIDADE FÍSICA')
    
    texto_recomendacao = '''    
    Atividade física é um comportamento que envolve os movimentos voluntários do corpo, com gasto de energia acima do nível de repouso, promovendo interações sociais e com o ambiente. Você pode fazer atividade física no seu tempo livre (como forma de lazer, por exemplo), para deslocamento, no ambiente de trabalho ou estudo e nas tarefas domésticas.\n
    É importante saber que a prática regular de atividade física traz diversos benefícios, como:\n
    •	Previne diversas doenças, como hipertensão, diabetes e câncer;\n
    •	Ajuda a controlar o peso, prevenindo a obesidade;\n
    •	Diminui a necessidade de utilização de medicamentos;\n
    •	Melhora o sono;\n
    •	Melhora a saúde mental;\n
    •	Estimula os vínculos sociais\n
    A OMS – Organização Mundial da Saúde recomenda:\n
    Se você tem de 6 a 17 anos: 60 minutos ou mais de atividade física por dia;\n
    Se você tem 18 anos ou mais: 150 minutos de atividade física de intensidade moderada ou pelo menos, 75 minutos de atividade física, por semana.\n
    A partir de 65 anos: atividade física moderada semelhante à da faixa de 18 a 64 anos, três dias por semana no mínimo, em intensidade que varia de acordo com as condições de saúde e de mobilidade de cada um.\n\n

    Exemplo de atividades:\n
    Moderada: Jogar Volei, hidroginástica, pedalar, dança, caminhada em ritmo rápido.\n
    Intensa: Corrida, pular corda, jogar futebol e natação.\n
    '''
    
    st.write(texto_recomendacao) 

    st.subheader('ALIMENTAÇÃO')

    texto_recomendacao = '''    
    De acordo com o Ministério da Saúde, uma alimentação saudável deve ser baseada em:\n
    1. Respeito e valorização as práticas alimentares culturalmente identificadas: o alimento tem significações culturais diversas que precisam ser estimuladas. A soberania alimentar deve ser fortalecida por meio deste resgate.\n
    2. A garantia de acesso, sabor e custo acessível. Uma alimentação saudável não é cara, pois se baseia em alimentos in natura e produzidos regionalmente. O apoio e o fomento à agricultores familiares e cooperativas para a produção e a comercialização de produtos saudáveis como legumes, verduras e frutas é uma importante alternativa para que além da melhoria da qualidade da alimentação, estimule geração de renda para comunidades. As práticas de marketing muitas vezes vinculam a alimentação saudável ao consumo de alimentos industrializados especiais e não privilegiam os alimentos não processados e menos refinados como, por exemplo, a mandioca que é um (tubérculo) alimento saboroso, muito nutritivo, típico e de fácil produção em várias regiões brasileiras e tradicionalmente saudável.\n
    3. Variada: fomentar o consumo de vários tipos de alimentos que forneçam os diferentes nutrientes necessários para o organismo, evitando a monotonia alimentar que limita o acesso de todos os nutrientes necessários a uma alimentação adequada.\n
    4. Colorida: como forma de garantir a variedade principalmente em termos de vitaminas e minerais, e também a apresentação atrativa das refeições, destacando o fomento ao aumento do consumo de alimentos saudáveis como legumes, verduras e frutas e tubérculos em geral.\n
    5. Harmoniosa: em termos de quantidade e qualidade dos alimentos consumidos para o alcance de uma nutrição adequada considerando os aspectos culturais, afetivos e comportamentais.\n
    6. Segura: do ponto de vista de contaminação físico-química e biológica e dos possíveis riscos à saúde. Destacado a necessidade de garantia do alimento seguro para consumo populacional.\n
    – Faça pelo menos 3 refeições (café da manhã, almoço e jantar) e 2 lanches saudáveis por dia. Não pule as refeições.\n
    – Inclua diariamente 6 porções do grupo do cereais(arroz, milho, trigo pães e mas¬sas), tubérculos como as batatas e raízes como a mandioca/macaxeira/aipim nas refeições. Dê preferência aos grãos integrais e aos alimen¬tos naturais.\n
    – Coma diariamente pelo menos 3 porções de legumes e verduras como parte das refeições e 3 porções ou mais de frutas nas sobremesas e lanches.\n
    – Coma feijão com arroz todos os dias ou , pelo menos, 5 vezes por semana. Esse pra¬to brasileiro é uma combinação completa de proteínas e bom para a saúde.\n
    – Consuma diariamente 3 porções de leite e derivados e 1 porção de carnes, aves, peixes ou ovos. Retirar a gordura aparente das carnes e a pele das aves antes da preparação torna esses alimentos mais saudáveis!\n
    – Consuma, no máximo, 1 porção por dia de óleos vegetais, azeite, manteiga ou marga¬rina. Fique atento aos rótulos dos alimen¬tos e escolha aqueles com menores quantidades de gorduras trans.\n
    – Evite refrigerantes e sucos industrializa¬dos, bolos, biscoitos doces e recheados, sobremesas doces e outras guloseimas como regra da alimentação.\n
    – Diminua a quantidade de sal na comida e retire o saleiro da mesa. Evite consumir alimentos industrializados com muito sal (sódio) como hambúrguer, charque, sal¬sicha, lingüiça, presunto, salgadinhos, conservas de vegetais, sopas, molhos e temperos prontos.\n
    – Beba pelo menos 2 litros (6 a 8 copos) de água por dia. Dê preferência ao consumo de água nos intervalos das refeições.\n
    – Torne sua vida mais saudável. Pratique pelo menos 30 minutos de atividade físi¬ca todos os dias e evite as bebidas alcoóli¬cas e o fumo. Mantenha o peso dentro de limites saudáveis.\n
    '''

    st.write(texto_recomendacao) 


    st.subheader('TAXA METABOLICA BASAL (TMB)')

    texto_recomendacao = '''        
    É a quantidade de energia necessária para a manutenção das funções vitais do organismo ao longo de 24 horas. É medida em calorias, que é a energia extraída pelo corpo a partir dos micronutrientes que são: carboidratos, proteínas e gorduras totais.\n
    Não existe taxa metabólica ideal, ela varia de acordo com a idade, sexo, metabolismo e etc.\n\n

    Cálculo:\n

    Taxa de atividade.\n
    Sedentarismo (pouco ou nenhum exercício) fator -> 1.2\n
    Levemente ativo (exercícios leves 1 a 3 dias na semana) fator -> 1.375\n
    Moderadamente ativo (exercício moderado, faz esportes 3 a 5 dias por semana) fator -> 1.55\n
    Altamente ativo (exercício pesado de 5 a 6 dias por semana) fator -> 1.725\n
    Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia) fator -> 1.9\n
    Fórmula para homens: TMB = fator da taxa de atividade x {66 + [(13,7 x Peso(kg)) + ( 5 x Altura(cm)) – (6,8 x Idade(anos))]}\n
    Fórmula para mulheres: TMB = fator da taxa de atividade x {655 + [(9,6 x Peso(kg)) + (1,8 x Altura(cm)) – (4,7 x Idade(anos))]}\n\n

    HOMEM\n
    66.5 + (13.75 x kg) + (5.003 x cm) - (6.775 x idade)\n\n
    MULHER\n
    655.1 + (9.563 x kg) + (1.850 x cm) - (4.676 x idade)\n
    '''


    st.write(texto_recomendacao) 

    if(gestante):
        st.subheader('GESTANTES')

        resultado_modelo = '<p style="font-family:Courier; color:Blue; font-size: 20px;">'+ 'PACIENTE GESTANTE: SIM' +'</p>'
        st.markdown(resultado_modelo, unsafe_allow_html=True)

        texto_recomendacao = '''    
        Antes de executar qualquer exercício, consulte o médico para liberação.\n
        No primeiro trimestre, para as gestantes que já realizam regularmente exercícios, eles podem ser mantidos. Para as grávidas sedentárias, a recomendação é iniciar as atividades após a 12° semana, evitando riscos de aborto.\n
        As atividades devem ser de leves a moderadas e podem ser feitas até o parto, ficando atento sempre à intensidade e carga dos exercícios com o avanço da gravidez para não sobrecarregar ainda mais o organismo.\n
        As atividades recomendadas são: hidroginástica, pilates e ioga. \n
        Elas irão ajudar na respiração, fortalecer o sistema cardiorrespiratório e evitar dores nas costas que podem começar a aparecer com o peso da barriga. Musculação também poderá ser realizada, porém com orientação.\n\n
        Uma alimentação gestacional é de extrema importância tanto para saúde da mãe, como para a do bebê. Contribui para a prevenção de diversas ocorrências negativas durante a gravidez, assegura reservas biológicas necessárias ao parto e pós-parto, garante substrato para o período de lactação, como também, favorece o ganho de peso adequado de acordo com o estado nutricional pré-gestacional.\n
        Deve conter todos os grupos alimentares existentes, como:\n
        Vegetais (folhosos e legumes); frutas; carne bovina, frango, fígado (uma vez por semana); ovos e peixes (sardinha, salmão, atum, pescada, cavalinha); leguminosas (feijão, grão de bico, lentilha, ervilha); cereais (arroz integral, batata, milho, entre outros); azeites (de preferência extra virgem); leite e derivados do leite (fora do horário do almoço e jantar).\n
        As carnes deverão ser assadas, grelhadas, ensopadas ou cozidas, evitando as frituras.\n
        Recomenda-se não ingerir gordura vegetal hidrogenada, que pode comprometer o crescimento e o desenvolvimento fetal.\n
        Distribuição das refeições\n
        As refeições devem ser distribuídas em seis vezes ao dia: \n
        Desjejum, colação, almoço, lanche, jantar e ceia. \n
        Os intervalos em média são de três horas entre uma e outra refeição.\n
        Fonte: Fiocruz\n
        '''

        st.write(texto_recomendacao) 


def load_prediction_model(model_path):
    model = load_model(model_path)
    return model

# modelo de previsao de HiperTensao
def model_HT_prediction(model, paciente):
    
    # {"id": 1,  "nome": "joao",  "idade": 34,  "sexo": 0,  "peso": 84,  "altura": 170,  "bpm": 92,  "pressao": 146,  "respiracao": 11,  "temperatura": 37,  "glicemia": 128,  "saturacao_oxigenio": 98,  "estado_atividade": 2,  "dia_de_semana": 1,  "periodo_do_dia": 1,  "semana_do_mes": 2,  "estacao_do_ano": 3,  "passos": 303,  "calorias": 24.24,  "distancia": 378.75,  "tempo": 4.848,  "total_sleep_last_24": 6,  "deep_sleep_last_24": 5,  "light_sleep_last_24": 3,  "awake_last_24": 15,  "fumante": 1,  "genetica": 1,  "gestante": 0,  "frutas": 0,  "vegetais": 0,  "alcool": 1,  "doenca_coracao": 1,  "avc": 1,  "colesterol_alto": 1,  "exercicio": 0,  "timestampstr": "2022-03-20 11:19:28",  "timestamp_epoch": "1647775168"}
    
    data_teste = pd.DataFrame()
    data_teste['HighChol'] = [float(paciente['colesterol_alto'])]
    data_teste['BMI'] = [float(paciente["peso"]) / ((float(paciente["altura"]) / 100) ** 2)]
    data_teste['Smoker'] = [float(paciente["fumante"])] 
    data_teste['Stroke'] = [float(paciente["avc"])]
    data_teste['Sex'] = [float(paciente["sexo"])]
    data_teste['Age'] = [float(paciente["idade"])]
    data_teste['Drink_alcohol'] = [float(paciente["alcool"])]
    data_teste['Weight_kg'] = [float(paciente["peso"])]
    data_teste['Systolic_bp'] = [float(paciente["pressao"])]
    data_teste['Hemoglobin_concentration'] = [float(paciente["glicemia"])]
    data_teste['Congestive_heart_failure'] = [float(paciente["doenca_coracao"])]
    data_teste['Relative_heart_attack'] = [float(paciente["genetica"])]
    data_teste['Exercising'] = [float(paciente["exercicio"])]
    data_teste['Height_cm'] = [float(paciente["altura"])]
    

    #realiza a predição.
    result = predict_model(model, data=data_teste)

    #recupera os resultados.
    classe = result["Label"][0]
    prob = result["Score"][0]*100

    st.subheader("Chance de desenvolver problemas de Hipertensão:")
    st.write("Executando o modelo de machine learning...")
    resultado_modelo = '<p style="font-family:Courier; color:Blue; font-size: 20px;">'+ 'Previsão(0=Não/1=Sim): ' + str(classe) +'</p>'
    precisao_modelo = '<p style="font-family:Courier; color:Blue; font-size: 20px;">'+ 'Precisão do Modelo: ' + str(round(prob,2)) + '%' +'</p>'
    st.markdown(resultado_modelo, unsafe_allow_html=True)
    st.markdown(precisao_modelo, unsafe_allow_html=True)

# Modelo de previsao de Diabetes
def model_DB_prediction(model, paciente):
    
    #data_teste = pd.DataFrame([paciente])
    # incluir os campos abaixo no json e testar se o comando acima pega direito os dados
    
    # {"id": 1,  "nome": "joao",  "idade": 34,  "sexo": 0,  "peso": 84,  "altura": 170,  "bpm": 92,  "pressao": 146,  "respiracao": 11,  "temperatura": 37,  "glicemia": 128,  "saturacao_oxigenio": 98,  "estado_atividade": 2,  "dia_de_semana": 1,  "periodo_do_dia": 1,  "semana_do_mes": 2,  "estacao_do_ano": 3,  "passos": 303,  "calorias": 24.24,  "distancia": 378.75,  "tempo": 4.848,  "total_sleep_last_24": 6,  "deep_sleep_last_24": 5,  "light_sleep_last_24": 3,  "awake_last_24": 15,  "fumante": 1,  "genetica": 1,  "gestante": 0,  "frutas": 0,  "vegetais": 0,  "alcool": 1,  "doenca_coracao": 1,  "avc": 1,  "colesterol_alto": 1,  "exercicio": 0,  "timestampstr": "2022-03-20 11:19:28",  "timestamp_epoch": "1647775168"}

    data_teste = pd.DataFrame()
    if(float(paciente["pressao"]) > 12):
        high_bp = 1
    else:
        high_bp = 0

    if(int(paciente["idade"]) >= 18 and int(paciente["idade"]) <= 24):
        idade = 1
    elif(int(paciente["idade"]) >= 25 and int(paciente["idade"]) <= 29):
        idade = 2
    elif(int(paciente["idade"]) >= 30 and int(paciente["idade"]) <= 34):
        idade = 3
    elif(int(paciente["idade"]) >= 35 and int(paciente["idade"]) <= 39):
        idade = 4
    elif(int(paciente["idade"]) >= 40 and int(paciente["idade"]) <= 44):
        idade = 5
    elif(int(paciente["idade"]) >= 45 and int(paciente["idade"]) <= 49):
        idade = 6
    elif(int(paciente["idade"]) >= 50 and int(paciente["idade"]) <= 54):
        idade = 7
    elif(int(paciente["idade"]) >= 55 and int(paciente["idade"]) <= 59):
        idade = 8
    elif(int(paciente["idade"]) >= 60 and int(paciente["idade"]) <= 64):
        idade = 9
    elif(int(paciente["idade"]) >= 65 and int(paciente["idade"]) <= 69):
        idade = 10
    elif(int(paciente["idade"]) >= 70 and int(paciente["idade"]) <= 75):
        idade = 11
    elif(int(paciente["idade"]) >= 75 and int(paciente["idade"]) <= 79):
        idade = 12
    elif(int(paciente["idade"]) >= 80 and int(paciente["idade"]) <= 99):
        idade = 13
    else:
        idade = 1

    data_teste['HighBP'] = [int(high_bp)]  
    data_teste['HighChol'] = [int(paciente["colesterol_alto"])]
    data_teste['BMI'] = [round((float(paciente["peso"]) / (float(paciente["altura"]) / 100) ** 2),0)]
    data_teste['Smoker'] = [int(paciente["fumante"])] 
    data_teste['Stroke'] = [int(paciente["avc"])]
    data_teste['HeartDiseaseorAttack'] = [int(paciente["doenca_coracao"])] 
    data_teste['Fruits'] = [int(paciente["frutas"])] 
    data_teste['Veggies'] = [int(paciente["vegetais"])]
    data_teste['HvyAlcoholConsump'] = [int(paciente["alcool"])]
    data_teste['Sex'] = [int(paciente["sexo"])]
    data_teste['PhysActivity'] = [int(paciente["exercicio"])]
    data_teste['Age'] = [idade]
    data_teste['Diabetes_012'] = [""]


    #realiza a predição.
    result = predict_model(model, data=data_teste)

    #recupera os resultados.
    classe = result["Label"][0]
    prob = result["Score"][0]*100

    st.subheader("Chance de desenvolver problemas de Diabetes:")
    st.write("Executando o modelo de machine learning...")
    resultado_modelo = '<p style="font-family:Courier; color:Blue; font-size: 20px;">'+ 'Previsão(0=Não/1=Provavelmente Vai Ter/2=Sim): ' + str(classe) +'</p>'
    precisao_modelo = '<p style="font-family:Courier; color:Blue; font-size: 20px;">'+ 'Precisão do Modelo: ' + str(prob) + '%' +'</p>'
    st.markdown(resultado_modelo, unsafe_allow_html=True)
    st.markdown(precisao_modelo, unsafe_allow_html=True)


# Carrega os pacientes
pacientes = get_paciente_data()

# Carrega o dataframe de populacao
df_total = get_populacao_data()

df_total['Diabetes_012'] = ""

# Carrega o Modelo de Machine Learning de previsao de diabetes
DB_model = load_prediction_model(ENV_PATH + '/DB_model')

# Carrega o Modelo de Machine Learning de previsao de diabetes
HT_model = load_prediction_model(ENV_PATH + '/HT_model')

exp_clf101 = setup(data = df_total, target = 'Diabetes_012', use_gpu=False, silent=True)

# cria a coluna de IMC (peso/altura^2)
df_total['imc'] = df_total["peso"] / ((df_total["altura"] / 100) ** 2)

#converte pra inteiro
df_total['imc'] = df_total['imc'].astype(int)


# criando a interface no Streamlit
# título
st.title("App - Ranking de Saúde")

# subtítulo
st.markdown("Esta é uma Aplicação para que os médicos consultem o estado geral de um paciente, comparado com outros individuos da população de uma base de dados.")

# verificando o dataset
st.subheader("Segue uma pequena amostra de pacientes:")

# atributos para serem exibidos por padrão
defaultcols = ["id","nome","idade","peso","altura"]

# defindo atributos a partir do multiselect
cols = st.multiselect("Atributos", defaultcols, default=defaultcols)

# exibindo os top 10 registro do dataframe
st.dataframe(df_total[cols].head(10))

st.subheader("Escolha um paciente no menu ao lado...")

st.sidebar.subheader("Escolha um paciente:")

# inserindo os pacientes que vao servir de amostra
#PACIENTES = {0: "Joao", 1 : "Mariana", 2: "Antonio", 3: "Camila"}

PACIENTES = [d['nome'] for d in pacientes]

# pegando os indices da lista de pacientes
range_pct = range(len(PACIENTES))

#retorna a descricao do bairro pelo codigo
def desc_paciente(paciente):
    return PACIENTES[paciente]

# cria uma caixa de selecao com os pacientes para o usuario escolher um
paciente = st.sidebar.selectbox("Nome do Paciente", options=range_pct, format_func=desc_paciente)
st.sidebar.write(f"Você selecionou o paciente {paciente} chamado {desc_paciente(paciente)}")

# inserindo um botão na tela
btn_show = st.sidebar.button("Mostrar o Ranking")

# verifica se o botão foi acionado
if btn_show:
    # pega o nome do paciente 
    dict_paciente = load_pacient(paciente)

    st.subheader("O paciente escolhido foi: ")    
    
    # imprime o resultado na tela
    st.write(dict_paciente)

    # imprime os graficos do paciente
    show_data()

    # mostra o resultado do modelo de previsao de Hipertensao
    model_HT_prediction(HT_model, dict_paciente)
    
    # mostra o resultado do modelo de previsao de Hipertensao
    model_DB_prediction(DB_model, dict_paciente)

    show_prescription(dict_paciente)
