import os
import sys
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Sistema Agronegócio", layout="wide")

# Menu de navegação
st.sidebar.title("🌾 Menu do Sistema")
fase = st.sidebar.radio(
    "Selecione a fase:",
    (
        "🏠 Visão Geral",
        "🌱 Fase 1 - Cálculo de Área e Meteorologia",
        "🏢 Fase 2 - Gestão do Agronegócio",
        "💧 Fase 3 - IoT e Sensores",
        "📊 Fase 4 - Dashboard e ML",
        "☁️ Fase 5 - Cloud e Alerta AWS",
        "🧠 Fase 6 - Visão Computacional"
    )
)

# Título central
st.markdown("<h1 style='text-align: center;'>🌾 Sistema Integrado para Gestão do Agronegócio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Este painel integra os módulos desenvolvidos nas Fases 1 a 6 do projeto de IA.</p>", unsafe_allow_html=True)
st.divider()

# Conteúdo da tela principal baseado na fase selecionada
if fase == "🏠 Visão Geral":
    st.subheader("Bem-vindo ao sistema!")
    st.markdown("Use o menu lateral à esquerda para acessar os módulos.")

elif fase == "🌱 Fase 1 - Cálculo de Área e Meteorologia":
    import sys
    sys.path.append("data/fase1")
    from script import calcular_area_melancias, calcular_area_eucalipto
    from previsao import obter_previsao

    st.subheader("🌱 Cálculo de Área e Insumos")

    cultura = st.selectbox("Selecione a cultura", ["Melancia", "Eucalipto"])

    if cultura == "Melancia":
        comprimento = st.number_input("Comprimento (m)", min_value=1.0)
        largura = st.number_input("Largura (m)", min_value=1.0)
        if st.button("Calcular"):
            r = calcular_area_melancias(comprimento, largura)
            st.metric("Área Total", f"{r['area_total']:.2f} m²")
            st.metric("Área Utilizável", f"{r['area_utilizavel']:.2f} m²")
            st.metric("Nº de Mudas", f"{r['numero_mudas']:.0f}")
            st.metric("Fertilizante", f"{r['total_fertilizante']:.2f} kg")
            st.metric("Controle de Pragas", f"{r['total_pragas']:.2f} L")

    elif cultura == "Eucalipto":
        largura = st.number_input("Largura (m)", min_value=1.0)
        altura = st.number_input("Comprimento (m)", min_value=1.0)
        if st.button("Calcular"):
            r = calcular_area_eucalipto(largura, altura)
            st.metric("Área Total", f"{r['area_total']:.2f} m²")
            st.metric("Área Utilizável", f"{r['area_utilizavel']:.2f} m²")
            st.metric("Nº de Mudas", f"{r['numero_mudas']:.0f}")
            st.metric("Fertilizante", f"{r['total_fertilizante']:.2f} kg")
            st.metric("Controle de Pragas", f"{r['total_pragas']:.2f} L")

    st.divider()
    st.subheader("☁️ Previsão do Tempo")
    cidade = st.text_input("Informe a cidade para previsão do tempo", value="Sao Paulo,BR")

    if st.button("Consultar previsão"):
        clima = obter_previsao(cidade)
        if clima:
            st.success(f"Temperatura: {clima['temperatura']}°C | Sensação: {clima['sensacao']}°C | Umidade: {clima['umidade']}%")
        else:
            st.error("Erro ao obter previsão do tempo.")


elif fase == "🏢 Fase 2 - Gestão do Agronegócio":
    sys.path.append("data/fase2")
    import crud
    crud.inicializar_db()

    st.title("🏢 Fase 2 - Gestão do Agronegócio")
    tab1, tab2, tab3, tab4 = st.tabs([
        "📅 Cadastrar Pavilhão", 
        "❌ Inativar Pavilhão", 
        "➕ Movimentar Estoque", 
        "🔍 Consultar Estoque"])

    with tab1:
        st.subheader("Cadastro de novo pavilhão")
        nome = st.text_input("Nome do pavilhão")
        if st.button("Salvar pavilhão"):
            if nome:
                crud.cadastrar_pavilhao(nome)
                st.success("Pavilhão cadastrado com sucesso!")
            else:
                st.warning("Informe um nome.")

    with tab2:
        st.subheader("Inativação de pavilhões")
        ativos = crud.listar_pavilhoes_ativos()
        if ativos:
            opcao = st.selectbox("Escolha um pavilhão ativo:", ativos, format_func=lambda x: f"{x[0]} - {x[1]}")
            if st.button("Inativar"):
                crud.inativar_pavilhao(opcao[0])
                st.success("Pavilhão inativado com sucesso!")
        else:
            st.info("Nenhum pavilhão ativo encontrado.")

    with tab3:
        st.subheader("Movimentação de Estoque")
        pavilhoes = crud.listar_pavilhoes_ativos()
        if pavilhoes:
            pav = st.selectbox("Pavilhão:", pavilhoes, format_func=lambda x: f"{x[0]} - {x[1]}")
            tipo_grao = st.text_input("Tipo de grão")
            quantidade = st.number_input("Quantidade", min_value=1)
            tipo_mov = st.radio("Tipo de movimentação", ("E", "S"), format_func=lambda x: "Entrada" if x == "E" else "Saída")
            if st.button("Registrar movimentação"):
                crud.registrar_movimentacao(pav[0], tipo_grao, quantidade, tipo_mov)
                st.success("Movimentação registrada!")
        else:
            st.info("Nenhum pavilhão ativo para movimentar estoque.")

    with tab4:
        st.subheader("Estoque Atual por Pavilhão")
        resultado = crud.consultar_estoque_atual()
        if not resultado.empty:
            st.dataframe(resultado, use_container_width=True)
        else:
            st.info("Nenhum registro de estoque encontrado.")


elif fase == "💧 Fase 3 - IoT e Sensores":
    st.subheader("💧 Fase 3 – Monitoramento com sensores e banco de dados Oracle")

    st.markdown("""
    Nesta fase, simulamos a coleta e visualização de dados ambientais utilizando sensores conectados a um ESP32 e armazenados em banco de dados Oracle.
    """)

    tab1, tab2 = st.tabs(["📊 Aplicação CRUD", "🔌 Simulador Wokwi"])

    with tab1:
        opcao = st.selectbox("Escolha uma ação:", [
            "Listar dados",
            "Inserir dados simulados",
            "Mostrar gráfico de variação (pH)"
        ])

        import sys
        import os
        caminho_crud = os.path.join("data", "fase3", "crud")
        if caminho_crud not in sys.path:
            sys.path.append(caminho_crud)

        import agro_nutriente as an

        if opcao == "Listar dados":
            df = an.data_diagram(return_df=True)  # ⚠️ você precisa adaptar essa função
            st.dataframe(df)
        elif opcao == "Inserir dados simulados":
            st.markdown("#### Preencha os dados simulados conforme visualizado no Wokwi")

            p = st.number_input("Nutriente P", min_value=0, max_value=100, step=1)
            k = st.number_input("Nutriente K", min_value=0, max_value=100, step=1)
            ph = st.slider("pH", min_value=0.0, max_value=14.0, step=0.1, value=7.0)
            umidade = st.number_input("Umidade (%)", min_value=0.0, max_value=100.0, step=0.1)
            luminosidade = st.number_input("Luminosidade", min_value=0, max_value=100)

            if st.button("Salvar dados simulados"):
                an.inserir_dado(p, k, ph, umidade, luminosidade)
                st.success("Dados simulados inseridos com sucesso!")

        elif opcao == "Mostrar gráfico de variação (pH)":
            fig = an.data_diagram(return_fig=True)  # ⚠️ você precisa adaptar essa função
            st.plotly_chart(fig)

    with tab2:
        st.markdown("### 🔌 Simulador IoT - ESP32 com sensores (Wokwi)")
        st.markdown("""
        Abaixo está um simulador virtual em tempo real do circuito desenvolvido com ESP32, sensores de umidade, luz e outros componentes.
        """)

        st.components.v1.iframe(
            src="https://wokwi.com/projects/413661400377385985",
            height=600,
            scrolling=True
        )


elif fase == "📊 Fase 4 - Dashboard e ML":
    st.subheader("📊 Fase 4 – Dashboard e Machine Learning")

    st.markdown("""
    Nesta fase, desenvolvemos um dashboard interativo utilizando **Streamlit** para visualizar dados agrícolas e aplicar modelos de **Machine Learning** com o **Scikit-Learn**. As principais funcionalidades incluem:

    - 📊 **Visualizações Interativas**: Gráficos e métricas para monitorar indicadores agrícolas;
    - 🤖 **Modelos Preditivos**: Previsão de variáveis como umidade e produtividade;
    - 🌐 **Integração com sensores**: Leitura de dados simulados ou reais para alimentar o dashboard;
    - 💡 **Interface amigável**: Pensada para facilitar a tomada de decisão por parte dos gestores.

    Essa solução entrega uma visão clara e estratégica sobre o funcionamento da lavoura em tempo real.
    """)

    # Botão e controle
    st.markdown("### ▶️ Executar Inferência no Dashboard")

    if "exibir_fase4" not in st.session_state:
        st.session_state.exibir_fase4 = False

    if st.button("Carregar dashboard de visualização e predição", key="btn_fase4"):
        st.session_state.exibir_fase4 = True

    if st.session_state.exibir_fase4:
        import sys
        import os

        caminho_fase4 = os.path.join("data", "fase4")
        if caminho_fase4 not in sys.path:
            sys.path.append(caminho_fase4)

        try:
            import app
            app.main()
        except Exception as e:
            st.error(f"Erro ao executar dashboard da Fase 4: {e}")



    st.markdown("### 🔗 Acesso aos recursos do projeto")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <a href="https://colab.research.google.com/github/Jr-RS/fase4_cap1_FarmTech/blob/main/JuniorSilva_rm559451_pbl_fase4.ipynb" target="_blank">
                <div style="background-color:#0e76a8; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                    📘 Abrir notebook no Colab
                </div>
            </a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <a href="https://github.com/Jr-RS/fase4_cap1_FarmTech" target="_blank">
                <div style="background-color:#24292e; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                    📁 Ver repositório no GitHub
                </div>
            </a>
        """, unsafe_allow_html=True)


elif fase == "☁️ Fase 5 - Cloud e Alerta AWS":
    st.subheader("☁️ Fase 5 - Cloud Computing & Segurança")

    st.markdown("""
    Nesta fase, a equipe da **FarmTech Solutions** migrou toda a infraestrutura de dados e aplicações para a **AWS**, visando maior escalabilidade, disponibilidade e segurança. As principais ações realizadas incluem:

    - ☁️ **Hospedagem na AWS**: uso de EC2 para garantir alta disponibilidade e escalabilidade;
    - 🔐 **Segurança da Informação**: alinhamento às normas de proteção dos dados;
    - 📈 **Monitoramento**: ferramentas para acompanhar desempenho e alertas de segurança.

    Essas medidas forneceram uma base confiável para a continuidade e crescimento sustentável da empresa.
    """)

    import sys
    sys.path.append("data/fase5")
    from inferencia import prever

    # Mapeamento necessário para conversão da variável categórica
    culturas = {
        "Cocoa, beans": 1,
        "Oil palm fruit": 2,
        "Rice, paddy": 3,
        "Rubber, natural": 4
    }

    st.subheader("☁️ Previsão de Anomalias com AWS")
    st.markdown("Essas medidas forneceram uma base confiável para a continuidade e crescimento sustentável da empresa.")

    col1, col2 = st.columns(2)
    with col1:
        temperatura = st.number_input("🌡️ Temperature (°C)", value=25.0)
        precipitacao = st.number_input("🌧️ Precipitation (mm)", value=2.0)
        crop = st.selectbox("🌱 Crop", list(culturas.keys()))

    with col2:
        umidade_relativa = st.number_input("💧 Relative Humidity (%)", value=60.0)
        umidade_especifica = st.number_input("💦 Specific Humidity", value=0.01)

    if st.button("🔍 Executar Inferência"):
        entrada = {
            "Crop": culturas[crop],  # converter string em valor numérico
            "Precipitation": precipitacao,
            "SpecificHumidity": umidade_especifica,
            "RelativeHumidity": umidade_relativa,
            "Temperature": temperatura
        }

        try:
            resultado = prever(entrada)
            st.success(f"Resultado da inferência: {resultado:.2f} toneladas/hectare")
        except Exception as e:
            st.error(f"Erro durante a inferência: {e}")



    st.markdown("### 🔗 Acesso aos recursos do projeto")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <a href="https://colab.research.google.com/github/Jr-RS/Fase5_Cap1_FarmTech-na-era-da-cloud-computing/blob/main/JuniorSilva_rm559451_pbl_fase5.ipynb" target="_blank">
                <div style="background-color:#0e76a8; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                    📘 Abrir notebook no Colab
                </div>
            </a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <a href="https://github.com/Jr-RS/Fase5_Cap1_FarmTech-na-era-da-cloud-computing" target="_blank">
                <div style="background-color:#24292e; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                    📁 Ver repositório no GitHub
                </div>
            </a>
        """, unsafe_allow_html=True)


elif fase == "🧠 Fase 6 - Visão Computacional":
    st.subheader("🧠 Fase 6 - Visão Computacional")

    tab0, tab1, tab2 = st.tabs(["🧠 Realizar Detecção de Objetos", "🔍 Detecção com YOLO", "🖼️ Comparando Abordagens"])

    with tab0:
        st.markdown("### 🧠 Realizar Detecção de Objetos")
        st.markdown("""
        Carregue uma imagem da plantação para realizar a detecção automática de objetos.  
        O modelo foi treinado com imagens da base da FarmTech Solutions.

        - 📁 Arquivo aceito: JPG ou PNG  
        - 🧠 Modelo utilizado: `YOLOv5s` customizado (`best.pt`)
        """)

        uploaded_file = st.file_uploader("Selecione uma imagem", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            import os
            from PIL import Image
            import subprocess

            # Salva a imagem no disco
            input_path = os.path.join("data", "fase4", "uploaded.jpg")
            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.image(input_path, caption="Imagem original", use_column_width=True)

            st.markdown("Realizando a detecção...")

            try:
                # Executa o detect.py via subprocesso
                comando = [
                    "python", "data/fase4/yolov5/detect.py",
                    "--weights", "data/fase4/best.pt",
                    "--source", input_path,
                    "--project", "data/fase4",
                    "--name", "resultado",
                    "--exist-ok"
                ]
                resultado = subprocess.run(comando, capture_output=True, text=True)

                if resultado.returncode != 0:
                    st.error("Erro ao rodar a detecção:")
                    st.code(resultado.stderr)
                else:
                    # Caminho da imagem resultante
                    nome_arquivo = os.path.basename(input_path)
                    output_path = os.path.join("data", "fase4", "resultado", nome_arquivo)
                    st.image(output_path, caption="Resultado da Detecção", use_column_width=True)

            except Exception as e:
                st.error(f"Erro ao rodar a detecção: {e}")



    with tab1:
        st.markdown("### 🤖 Sobre o projeto de Visão Computacional (Fase 6)")
        st.markdown("""
        Este módulo utiliza o algoritmo **YOLO** para detectar automaticamente pragas e anomalias em imagens de plantações.
        O modelo foi treinado com imagens rotuladas para identificar situações que impactam o cultivo e ajudar no monitoramento da lavoura.

        Abaixo, você confere exemplos reais de imagens **processadas pelo modelo treinado**, destacando os objetos detectados.
        """)

        # Mostrar imagens do diretório
        pasta_imagens = "data/images_predicted"
        imagens = [img for img in os.listdir(pasta_imagens) if img.endswith((".png", ".jpg", ".jpeg"))]

        if imagens:
            st.markdown("#### 🖼️ Imagens com Detecção YOLO")
            colunas = st.columns(len(imagens))
            for col, img_path in zip(colunas, imagens):
                imagem = Image.open(os.path.join(pasta_imagens, img_path))
                col.image(imagem, caption=img_path, use_column_width=True)
        else:
            st.warning("Nenhuma imagem encontrada no diretório `data/images_predicted`.")

        st.markdown("### 🔗 Acesso aos recursos do projeto")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <a href="https://colab.research.google.com/github/Jr-RS/fase6_cap1_FarmTech/blob/main/JuniorSilva559451_fase6.ipynb" target="_blank">
                    <div style="background-color:#0e76a8; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                        📘 Abrir no Colab
                    </div>
                </a>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <a href="https://github.com/Jr-RS/fase6_cap1_FarmTech" target="_blank">
                    <div style="background-color:#24292e; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                        📁 Ver repositório no GitHub
                    </div>
                </a>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("### 📊 Comparativo entre abordagens de visão computacional (Fase 6 - Entrega 2)")

        st.markdown("""
        Nesta segunda etapa, realizamos uma comparação entre diferentes abordagens de visão computacional para o problema de identificação de objetos (**alface** e **maçã**), visando encontrar a solução mais adequada para o cliente **FarmTech Solutions**.

        Foram aplicadas as seguintes estratégias:

        - 🧠 **YOLO Customizada**: Utilizando o modelo treinado na Entrega 1, adaptado ao nosso conjunto de dados;
        - 📦 **YOLO Padrão** (pré-treinada no COCO): Aplicação do modelo YOLOv5s pré-treinado;
        - 🌀 **CNN Desenvolvida do Zero**: Construção de uma rede convolucional simples para classificar as imagens.

        Cada abordagem foi avaliada com base em:
        - Facilidade de uso e integração;
        - Precisão do modelo;
        - Tempo de treinamento;
        - Tempo de inferência.

        🏆 **Conclusão**: A **YOLO customizada** apresentou o melhor equilíbrio entre **precisão**, **velocidade** e **aplicabilidade** ao cenário da FarmTech Solutions.
        """)

        # Mostrar gráficos comparativos
        st.markdown("### 📈 Resultados comparativos")

        col1, col2 = st.columns(2)
        with col1:
            st.image("data/fase6_entrega2/image1.png", caption="Precisão Final por Modelo", use_column_width=True)
        with col2:
            st.image("data/fase6_entrega2/image2.png", caption="Tempo de Treinamento por Modelo", use_column_width=True)

        st.image("data/fase6_entrega2/image3.png", caption="Tempo Médio de Inferência por Imagem", use_column_width=True)

        # Tabela comparativa (formato visual com st.table)
        st.markdown("### 🧾 Tabela Comparativa")

        import pandas as pd

        tabela = pd.DataFrame({
            "Critério": [
                "Facilidade de uso",
                "Precisão final no conjunto de teste",
                "Tempo de treinamento",
                "Tempo de inferência"
            ],
            "YOLO Customizada": [
                "Médio (exige treino e ajuste)",
                "Alta (~85% mAP@0.5)",
                "Médio (~30 min)",
                "Muito rápido"
            ],
            "YOLO Padrão": [
                "Alto (modelo pronto)",
                "Muito baixa",
                "Nenhum",
                "Muito rápido"
            ],
            "CNN do Zero": [
                "Alto (rede simples)",
                "Boa (90,91% acurácia)",
                "Curto (~5 min)",
                "Rápido"
            ]
        })

        st.table(tabela)

        # Links externos
        st.markdown("### 🔗 Acesso aos recursos do comparativo")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <a href="https://colab.research.google.com/github/Jr-RS/fase6_cap1_FarmTech/blob/main/JuniorSilva559451_fase6_entrega2.ipynb" target="_blank">
                    <div style="background-color:#0e76a8; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                        📘 Abrir comparativo no Colab
                    </div>
                </a>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <a href="https://github.com/Jr-RS/fase6_cap1_FarmTech" target="_blank">
                    <div style="background-color:#24292e; padding:12px; border-radius:8px; text-align:center; color:white; font-weight:bold; font-size:16px; text-decoration:none;">
                        📁 Ver repositório no GitHub
                    </div>
                </a>
            """, unsafe_allow_html=True)