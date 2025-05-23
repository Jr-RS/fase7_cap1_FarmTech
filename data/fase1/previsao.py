import requests

def obter_previsao(cidade):
    api_key = "0388f59b182246722de1adb20b0d7c27"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    resposta = requests.get(url)

    print(resposta)

    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            "temperatura": dados["main"]["temp"],
            "sensacao": dados["main"]["feels_like"],
            "umidade": dados["main"]["humidity"]
        }
    else:
        return None
