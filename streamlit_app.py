import streamlit as st

# Função para calcular o custo total dos convites
def calcular_custo_total(convidados, convite0, convite50, convite80, convite100, valor_convite):
    convite_restante = convidados - convite0 - convite50 - convite80 - convite100
    custo_total = (convite0 * 0) + (convite50 * (valor_convite * 0.5)) + (convite80 * (valor_convite * 0.8)) + (convite100 * valor_convite) 
    return custo_total, convite_restante

# Interface Streamlit
st.title("Simulação da Festa de Aniversário")

# Barras dinâmicas (sliders) para os valores de entrada
convidados = st.slider("Número de Convidados:", 90, 140, step=1)
convite0 = st.slider("Número de Convites Gratuitos:", 0, convidados, step=1)
convite50 = st.slider("Número de Convites com 50% de Desconto:", 0, convidados - convite0, step=1)
convite80 = st.slider("Número de Convites com 20% de Desconto:", 0, convidados - convite0 - convite50, step=1)
convite100 = convidados - convite0 - convite50 - convite80
valor_convite = st.slider("Valor do Convite:", 90.0, 150.0, step=10)

# Botão para calcular
if st.button("Calcular"):
    custo_total, convite_restante = calcular_custo_total(convidados, convite0, convite50, convite80, convite100, valor_convite)
    st.write(f"O custo total dos convites é: R${custo_total:.2f}")
    st.write(f"Número de Convites Restantes: {convite_restante}")
