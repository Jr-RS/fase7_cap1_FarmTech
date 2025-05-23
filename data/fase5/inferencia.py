import joblib
import pandas as pd

# Carregar o modelo treinado para prever Yield
modelo = joblib.load("data/fase5/modelo.pkl")

# Dicionário de mapeamento das culturas
culturas = {
    "Cocoa, beans": 1,
    "Oil palm fruit": 2,
    "Rice, paddy": 3,
    "Rubber, natural": 4
}

def prever(dados):
    # Converter o dicionário em DataFrame com colunas ordenadas
    df = pd.DataFrame([dados], columns=["Crop", "Precipitation", "SpecificHumidity", "RelativeHumidity", "Temperature"])
    return modelo.predict(df)[0]
