#Importa modulos
import oracledb
import pandas as pd

try:
    #Connection string
    conn = oracledb.connect(user='rm559855',password='200484',dsn='oracle.fiap.com.br:1521/ORCL')
    #Instruction for module
    inst_include = conn.cursor()
    inst_select  = conn.cursor()
    inst_update  = conn.cursor()
    inst_exclude = conn.cursor()
except Exception as e:
    #Show error
    print('Error: ', e)
    vb_connect = False
else:
    vb_connect = True