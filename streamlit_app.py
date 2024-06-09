import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o custo total dos convites
def calcular_custo_total(convidados, convite0, convite50, convite80, valor_convite):
    total_convite0 = convite0 * 0
    total_convite50 = convite50 * (valor_convite * 0.5)
    total_convite80 = convite80 * (valor_convite * 0.8)
    total_custo = total_convite0 + total_convite50 + total_convite80
    return total_custo

# Interface Streamlit
st.title("Simulação da Festa de Aniversário")

# Campos de entrada
convidados = st.number_input("Número de Convidados:", min_value=0, step=1)
convite0 = st.number_input("Número de Convites Gratuitos:", min_value=0, step=1)
convite50 = st.number_input("Número de Convites com 50% de Desconto:", min_value=0, step=1)
convite80 = st.number_input("Número de Convites com 20% de Desconto:", min_value=0, step=1)
valor_convite = st.number_input("Valor do Convite:", min_value=0.0, step=0.01)

# Botão para calcular
if st.button("Calcular"):
    custo_total = calcular_custo_total(convidados, convite0, convite50, convite80, valor_convite)
    st.write(f"O custo total dos convites é: R${custo_total:.2f}")

    # Gráfico dinâmico
    labels = ['Convite 0', 'Convite 50%', 'Convite 80%']
    sizes = [convite0, convite50, convite80]
    colors = ['gold', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    ax1.axis('equal')  

    st.pyplot(fig1)
