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
convite50_max = max(0, convidados - convite0)
convite50 = st.slider("Número de Convites com 50% de Desconto:", 0, convite50_max, step=1)
convite80_max = max(0, convidados - convite0 - convite50)
convite80 = st.slider("Número de Convites com 20% de Desconto:", 0, convite80_max, step=1)
convite100_max = max(0, convidados - convite0 - convite50 - convite80)
convite100 = st.slider("Número de Convites Pagos:", 0, convite100_max, step=1)
valor_convite = st.slider("Valor do Convite:", 90.0, 150.0, step=0.01)

# Calcular o custo total dos convites e número de convites restantes
custo_total, convite_restante = calcular_custo_total(convidados, convite0, convite50, convite80, convite100, valor_convite)

# Mostrar o valor total dos convites e o número de convites restantes
st.write(f"O custo total dos convites é: R${custo_total:.2f}")
st.write(f"Número de Convites Restantes: {convite_restante}")
