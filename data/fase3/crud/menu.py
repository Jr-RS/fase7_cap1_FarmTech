import oracle_connect as conn
import agro_nutriente as an
import os

while conn.vb_connect:
  os.system('cls')

  print("---- CONSULTA DE DADOS E MANUTENÇÃO DE NUTRIENTES----")
  print("""
  1 - Listar Dados Máquina Agrícola Ordenado por Data
  2 - Inserir dados da Máquina Agrícola ate 4 dias atrás
  3 - Diagrama de variação do nutriente pH por data
  5 - SAIR
  """)
  # Captura a escolha do usuário
  vn_option = int(input( ' ' + "Escolha -> "))

  match vn_option:
   case 1:
    an.data_select()
   case 2:
    an.data_generate_data()
   case 3:
    an.data_diagram()
   case 5:
    break
