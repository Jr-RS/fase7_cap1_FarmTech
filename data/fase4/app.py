import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load

def main():
    st.title("Dashboard do Sistema de Irrigação")

    # Função para carregar os dados
    @st.cache_data
    def carregar_dados():
        return pd.read_csv("data/fase4/base_preparada.csv", sep=";")

    base = carregar_dados()
    figsize = (15, 8)

    # Gráfico 1: Melhores Dias para Irrigação
    st.subheader("Gráfico: Melhores Dias para Irrigação")
    dia_irrigacao = base.groupby('dia')['irrigacao'].mean().reset_index()
    dia_map = {0: 'Domingo', 1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado'}
    dia_irrigacao['dia'] = dia_irrigacao['dia'].map(dia_map)
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(data=dia_irrigacao, x='dia', y='irrigacao', ax=ax)
    ax.set_title("Taxa de Irrigação por Dia da Semana")
    ax.set_ylabel("Taxa de Irrigação")
    ax.set_xlabel("Dia da Semana")
    st.pyplot(fig)

    # Gráfico 2: Melhores Horários
    st.subheader("Gráfico: Melhores Horários para Irrigação")
    base['dia_nome'] = base['dia'].map(dia_map)
    hora_dia_irrigacao = base.groupby(['hora', 'dia_nome'])['irrigacao'].mean().reset_index()
    media_geral = base.groupby('hora')['irrigacao'].mean().reset_index()
    media_geral['dia_nome'] = 'Média Geral'
    hora_dia_irrigacao = pd.concat([hora_dia_irrigacao, media_geral], ignore_index=True)
    dias_selecionados = st.multiselect(
        "Selecione os dias da semana:",
        options=list(dia_map.values()) + ['Média Geral'],
        default=['Média Geral']
    )
    dados_filtrados = hora_dia_irrigacao[hora_dia_irrigacao['dia_nome'].isin(dias_selecionados)]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=dados_filtrados, x='hora', y='irrigacao', hue='dia_nome', marker="o", ax=ax)
    ax.set_title("Taxa de Irrigação por Horário e Dia da Semana")
    ax.set_ylabel("Taxa Média de Irrigação")
    ax.set_xlabel("Hora do Dia")
    ax.legend(title="Dia da Semana", loc='upper right')
    st.pyplot(fig)

    # Gráfico 3: Mapa de Calor de Umidade
    st.subheader("Gráfico: Umidade ao Longo do Dia e da Semana")
    heatmap_data = base.pivot_table(index="dia_nome", columns="hora", values="umidade", aggfunc="mean")
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(heatmap_data, cmap="Blues", ax=ax, annot=True, fmt=".1f", linewidths=.5, cbar_kws={'label': 'Umidade Média'})
    ax.set_title("Mapa de Calor: Umidade por Dia e Hora", fontsize=14)
    ax.set_ylabel("Dia da Semana")
    ax.set_xlabel("Hora do Dia")
    st.pyplot(fig)

    # Previsão de Irrigação
    st.subheader("Análise Preditiva: Ativar Irrigação?")
    modelo = load("data/fase4/modelo.pkl")

    umidade_input = st.number_input("Umidade (%)", min_value=0.0, max_value=100.0, value=50.0)
    nutrientes_input = st.number_input("Nutrientes", min_value=0.0, max_value=100.0, value=20.0)
    hora_input = st.slider("Hora do Dia", min_value=0, max_value=23, value=12)
    dia_input = st.selectbox("Dia da Semana", list(dia_map.values()))
    dia_input_num = {v: k for k, v in dia_map.items()}[dia_input]

    if st.button("Prever"):
        try:
            nova_amostra = np.array([[umidade_input, nutrientes_input, hora_input, dia_input_num]])
            predicao = modelo.predict(nova_amostra)

            if predicao[0] == 1:
                st.success("🌿 Recomendação: Ativar a Irrigação!")
            else:
                st.info("✅ Recomendação: Não é necessário ativar a irrigação agora.")
        except Exception as e:
            st.error(f"Erro ao realizar a predição: {e}")