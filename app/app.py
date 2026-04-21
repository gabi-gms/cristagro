import streamlit as st
import pandas as pd
import joblib

# carregar modelo e colunas salvas
model = joblib.load("models/model.pkl")
model_columns = joblib.load("models/columns.pkl")

st.set_page_config(page_title="Cristagro", page_icon="🌱")

st.title("🌱 Cristagro")
st.write("Sistema simples de previsão de produtividade agrícola.")

st.subheader("Informe os dados da safra")

# inputs do usuário
cultura = st.selectbox("Cultura", ["milho", "soja", "café"])
temperatura = st.number_input(
    "Temperatura média (°C)",
    min_value=0.0,
    max_value=50.0,
    value=25.0,
    step=0.1
)
chuva = st.number_input(
    "Chuva acumulada",
    min_value=0.0,
    max_value=500.0,
    value=100.0,
    step=1.0
)
solo = st.selectbox("Tipo de solo", ["argiloso", "arenoso", "misto"])
irrigacao = st.selectbox("Irrigação", ["sim", "não"])

if st.button("Prever produtividade"):
    # criar dataframe com os dados do usuário
    input_data = pd.DataFrame([{
        "cultura": cultura,
        "temperatura": temperatura,
        "chuva": chuva,
        "solo": solo,
        "irrigacao": irrigacao
    }])

    # transformar igual ao treino
    input_encoded = pd.get_dummies(
        input_data,
        columns=["cultura", "solo", "irrigacao"],
        drop_first=True
    )

    # garantir mesmas colunas do treino
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # previsão
    prediction = model.predict(input_encoded)[0]

    # classificação simples
    if prediction >= 5.5:
        nivel = "Alta produtividade"
        mensagem = "As condições informadas indicam um cenário favorável para a safra."
    elif prediction >= 4.0:
        nivel = "Produtividade moderada"
        mensagem = "As condições são razoáveis, mas há espaço para otimização."
    else:
        nivel = "Baixa produtividade"
        mensagem = "As condições informadas sugerem maior risco de desempenho reduzido."

    st.success(f"Produtividade prevista: {prediction:.2f} ton/ha")
    st.subheader("Interpretação do resultado")
    st.write(f"**Classificação:** {nivel}")
    st.write(mensagem)

    st.subheader("Resumo dos dados informados")
    st.write(f"**Cultura:** {cultura}")
    st.write(f"**Temperatura média:** {temperatura:.1f} °C")
    st.write(f"**Chuva acumulada:** {chuva:.1f}")
    st.write(f"**Tipo de solo:** {solo}")
    st.write(f"**Irrigação:** {irrigacao}")