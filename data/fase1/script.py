import os
import pandas as pd

culturas = ['Melancia', 'Eucalipto']
descricoes =[
    """    Área útil para o plantío de Melancias é de 85% da área total, onde a área total é o comprimento vezes a largura do terreno.
    E 15% da área total é destinada para a construção estradas e áreas impróprias para o plantio.
    A forma geométrica para as melâncias é um retângulo, que facilita o plantio e a colheita, visto que as melâncias são plantadas em fileiras.""",
    """    O plantío de Ecalipito é realizado em 90% da área total, calculada pelo comprimento vezes a largura do terreno.
    Os 10% restantes é destinada para a estradas e áreas impróprias para o plantio, esse percenual pode variar de acordo com a quantidade de água existente no terreno.
    A plantação do eucalipito é feita em um retângulo ou quadrado, sempre visando preencher o espaço com o maior número de plantas possíveis, estradas não são necessárias pois o corte sera feito por máquinas."""
]

menu = f"""
*** FarmTech Solutions ***

Culturas disponíveis:

1. {culturas[0]}
{descricoes[0]}

2. {culturas[1]}
{descricoes[1]}

3. Sair do Programa

Por favor, selecione uma das opções acima: 
"""

def calcular_area(comprimento, largura, percentual_improprio, espacamento):
    area_total = comprimento * largura
    area_utilizavel = area_total * (1 - percentual_improprio)
    numero_mudas = area_utilizavel / espacamento
    return {'area_total': area_total, 'area_utilizavel': area_utilizavel, 'numero_mudas': numero_mudas}

def calcular_insumos(area_utilizavel, dose_fertilizante, dose_pragas):
    total_fertilizante = dose_fertilizante * area_utilizavel
    total_pragas = dose_pragas * area_utilizavel
    return {'total_fertilizante': total_fertilizante, 'total_pragas': total_pragas}

def calcular_area_melancias(comprimento, largura):
    percentual_improprio = 0.15
    espacamento = 2.5
    doses_melancias = {'fertilizante': 0.012, 'pragas': 0.00004}  # Doses recomendadas de fertilizantes e controle de pragas kg/m² e L/m²
    resultado = calcular_area(comprimento, largura, percentual_improprio, espacamento)
    insumos = calcular_insumos(resultado['area_utilizavel'], doses_melancias['fertilizante'], doses_melancias['pragas'])   
    resultado.update(insumos)
    return resultado

def calcular_area_eucalipto(largura, altura):
    percentual_improprio = 0.10
    espacamento = 4
    doses_eucalipto = {'fertilizante': 0.02, 'pragas': 0.00003}   # Doses recomendadas de fertilizantes e controle de pragas kg/m² e L/m²
    resultado = calcular_area(largura, altura, percentual_improprio, espacamento) 
    insumos = calcular_insumos(resultado['area_utilizavel'], doses_eucalipto['fertilizante'], doses_eucalipto['pragas'])
    resultado.update(insumos)
    return resultado

def gerar_relatorio(resultado, titulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n*** Relatório para platio de {titulo} ***\n")
    print(f"Área total: {resultado['area_total']} m²")
    print(f"Área utilizável: {resultado['area_utilizavel']} m²")
    print(f"Número de mudas: {resultado['numero_mudas']:.0f}")
    print(f"Fertilizante necessário: {resultado['total_fertilizante']:.2f} kg")
    print(f"Controle de pragas necessário: {resultado['total_pragas']:.2f} L\n")

def inserir_dados(df, cultura, resultado):
    df.loc[len(df)] = [
        cultura,
        round(resultado['area_total']),
        round(resultado['area_utilizavel'], 2),
        int(resultado['numero_mudas']),
        round(resultado['total_fertilizante'], 2),
        round(resultado['total_pragas'], 3)
    ]
    return df

def executar_programa():
    df = pd.DataFrame(columns=['Cultura', 'AreaTotal', 'AreaUtilizavel', 'NumeroMudas', 'Fertilizante', 'Pragas'])

    print(menu)
    
    while True:
        opcao = input("Digite a opção desejada (1, 2 ou 3): ")

        if opcao == '1' or opcao == 'Melancia':
            comprimento = float(input("Digite o comprimento da área de plantio (em metros): "))
            largura = float(input("Digite a largura da área de plantio (em metros): "))
            resultado = calcular_area_melancias(comprimento, largura)
            gerar_relatorio(resultado, 'Melancia')
            df = inserir_dados(df, 'Melancia', resultado)

        elif opcao == '2' or opcao == 'Eucalipto':
            largura = float(input("Digite o comprimento da área de plantio (em metros): "))
            altura = float(input("Digite a largura da área de plantio (em metros): "))
            resultado = calcular_area_eucalipto(largura, altura)
            gerar_relatorio(resultado, 'Eucalipto')
            df = inserir_dados(df, 'Eucalipto', resultado)

        elif opcao == '3' or opcao == 'Sair':
            print("Saindo do programa...")
            df.to_csv('relatorio.csv', index=False, sep=';')
            break

        else:
            print("Opção inválida! Tente novamente.")