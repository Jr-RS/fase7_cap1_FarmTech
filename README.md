# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

---

# 🌱 FarmTech Solutions – Sistema de Gestão Agrícola Inteligente

## Nome do projeto
Fase 7 - Cap 1 - A consolidação de um sistema

## Nome do grupo
Grupo 42

## 👨‍🎓 Integrantes:
- [Ana Beatriz Duarte Domingues](https://www.linkedin.com/in/)
- [Junior Rodrigues da Silva](https://www.linkedin.com/in/jrsilva051/)
- [Carlos Emilio Castillo Estrada](https://www.linkedin.com/in/)

## 👩‍🏫 Professores:
### Tutor(a)
- [Lucas Gomes Moreira](https://www.linkedin.com/company/inova-fusca)
### Coordenador(a)
- [André Godoi Chiovato](https://www.linkedin.com/company/inova-fusca)

---

## 📜 Descrição

Este projeto integra diversas soluções tecnológicas desenvolvidas ao longo das Fases 1 a 6, consolidando tudo em uma dashboard interativa feita com Python e Streamlit. O objetivo é oferecer um sistema inteligente para monitoramento e gestão de uma fazenda automatizada, utilizando sensores IoT, análise de dados, modelos de Machine Learning e notificações automatizadas por e-mail via AWS.

---

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

---

## 🔁 Fases Integradas

### ✅ Fase 1 – Base de Dados Inicial
- Cálculo da área de plantio e insumos.
- Conexão com API meteorológica.
- Análise estatística com R.
- Base de dados para uso futuro.

### ✅ Fase 2 – Banco de Dados Estruturado
- Modelagem MER/DER.
- Banco relacional preparado para os dados de sensores e análises futuras.

### ✅ Fase 3 – IoT e Automação Inteligente
- Simulação no Wokwi com ESP32 + sensores:
  - DHT22 (umidade/temperatura)
  - HC-SR04 (nível de água)
  - LDR (simula pH)
  - PIR (movimento)
- Controle automático da irrigação.
- Integração com banco de dados.

### ✅ Fase 4 – Dashboard Interativa com Data Science
- Dashboard em **Streamlit**:
  - Visualização de sensores em tempo real.
  - Análises de produtividade.
  - Modelos preditivos com Scikit-Learn.
- LCD + Serial Plotter no ESP32.

### ✅ Fase 5 – Cloud Computing & Segurança
- Hospedagem na **AWS**.
- Segurança baseada nas normas **ISO 27001 e 27002**.

### ✅ Fase 6 – Visão Computacional com YOLO
- Detecção de objetos via YOLO.
- Resultado integrado à dashboard.

---

## 🧠 Fase 7 – Integração Geral

Nesta fase final, todas as soluções desenvolvidas ao longo das fases anteriores foram integradas em uma dashboard interativa construída com **Python e Streamlit**.

A aplicação permite que o usuário:
- Visualize em tempo real os dados coletados pelos sensores simulados no Wokwi.
- Consulte o banco de dados com registros históricos de umidade, temperatura, luminosidade e presença.
- Execute o modelo de Machine Learning treinado para prever o rendimento da safra com base nas condições ambientais.
- Receba uma mensagem por **e-mail (AWS SES)** ou **SMS (AWS SNS)** com o resultado da predição ou alertas personalizados.

Tudo isso pode ser feito por meio de botões e interações simples na interface gráfica, facilitando o uso mesmo para pessoas sem conhecimento técnico.


#### 📸 Prints do alerta AWS:

![Alerta AWS 1](./imgs/alerta_aws_1.png)  
![Alerta AWS 2](./imgs/alerta_aws_2.png)


---

## 🎥 Demonstração em Vídeo

📺 Link do vídeo:  
👉 [https://youtu.be/ZqiAG8-kwcA](https://youtu.be/ZqiAG8-kwcA)

---

## 👨‍💻 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/Jr-RS/fase7_cap1_FarmTech.git
cd fase7_cap1_FarmTech
```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute a dashboard:
```bash
streamlit run app.py
```

## 📚 Histórico de Lançamentos

* 0.1.0 - 20/05/2025
    * Primeira versão do projeto 

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
