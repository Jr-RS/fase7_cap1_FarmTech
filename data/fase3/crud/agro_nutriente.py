import pandas as pd
import oracle_connect as conn
import sqlite3
import datetime
import plotly.express as px

def data_select():
    print("----- LISTAR TIPOS DE SOLO -----\n")
    data_list = []
    conn.inst_select.execute('SELECT * FROM T_AGRO_NUTRIENTE')
    data = conn.inst_select.fetchall()
    for dt in data:
        data_list.append(dt)

    data_list = sorted(data_list)

    data_df = pd.DataFrame.from_records(data_list)

    if data_df.empty:
        print(f'Não há nutrientes cadastrados, gerar datos na opção 2!')
    else:
        print(data_df)
    print('\nListados!')
    input('Pressione ENTER')

def data_save(vl_nut_p,vl_nut_k,vl_nut_ph,vl_nut_um,vl_nut_lum,dt_data_reg):
    try:
        formatted_date = dt_data_reg.strftime("%Y-%m-%d %H:%M:%S")
        register = f"""
                    INSERT INTO T_AGRO_NUTRIENTE (vl_nut_p, vl_nut_k, vl_nut_ph, vl_nut_um, vl_nut_lum, dt_data_reg)
                    VALUES (:vl_nut_p, :vl_nut_k, :vl_nut_ph, :vl_nut_um, :vl_nut_lum, TO_DATE(:dt_data_reg, 'YYYY-MM-DD HH24:MI:SS'))
                    """
        print(register)
        conn.inst_include.execute(register, {
            "vl_nut_p": vl_nut_p,
            "vl_nut_k": vl_nut_k,
            "vl_nut_ph": vl_nut_ph,
            "vl_nut_um": vl_nut_um,
            "vl_nut_lum": vl_nut_lum,
            "dt_data_reg": formatted_date
        })
        conn.conn.commit()

    except Exception as e:
            print('Error: ', e)

def data_edit(vl_nut_p,vl_nut_k,vl_nut_ph,vl_nut_um,vl_nut_lum,dt_data_reg,cd_nut):
    try:
        formatted_date = dt_data_reg.strftime("%Y-%m-%d %H:%M:%S")
        register = f"""
                    UPDATE T_AGRO_NUTRIENTE
                    SET vl_nut_p = :vl_nut_p, vl_nut_k = :vl_nut_k, vl_nut_ph = :vl_nut_ph,
                        vl_nut_um = :vl_nut_um, vl_nut_lum = :vl_nut_lum, dt_data_reg = TO_DATE(:dt_data_reg, 'YYYY-MM-DD HH24:MI:SS')
                    WHERE cd_nut = :cd_nut
                    """
        print(register)
        conn.inst_update.execute(register, {
            "vl_nut_p": vl_nut_p,
            "vl_nut_k": vl_nut_k,
            "vl_nut_ph": vl_nut_ph,
            "vl_nut_um": vl_nut_um,
            "vl_nut_lum": vl_nut_lum,
            "dt_data_reg": formatted_date,
            "cd_nut": cd_nut
        })
        conn.conn.commit()

    except Exception as e:
            print('Error: ', e)

def data_delete(cd_nut):
    try:
        register = f"""
                    DELETE T_AGRO_NUTRIENTE
                    WHERE cd_nut = :cd_nut
                    """
        print(register)
        conn.inst_exclude.execute(register, {
            "cd_nut": cd_nut
        })
        conn.conn.commit()

    except Exception as e:
            print('Error: ', e)

def data_delete_all():
    try:
        register = f"""
                    DELETE T_AGRO_NUTRIENTE    
                    """
        print(register)
        conn.inst_exclude.execute(register)
        conn.conn.commit()

    except Exception as e:
            print('Error: ', e)

def data_generate_data():
    try:
        data_delete_all()
        today = datetime.datetime.now()
        date_before_one =  today - datetime.timedelta(days=1)
        date_before_two =  today - datetime.timedelta(days=2)
        date_before_three =  today - datetime.timedelta(days=3)

        data_save(0, 0,8, 18,5,today)
        data_save(0, 0, 8, 18, 5, today)
        data_save(0, 0, 8, 18, 5, today)
        data_save(0, 0, 8, 18, 5, today)
        data_save(0, 0, 9, 18, 5, today)
        data_save(0, 0, 8, 18, 5, today)
        data_save(0, 0, 8, 18, 5, today)
        data_save(0, 0, 7, 18, 5, today)
        data_save(0, 0, 7, 18, 5, today)

        data_save(0, 0, 8, 18, 5, date_before_one)
        data_save(0, 0, 8, 18, 5, date_before_one)
        data_save(0, 0, 8, 18, 5, date_before_one)
        data_save(0, 0, 8, 18, 5, date_before_one)
        data_save(0, 0, 8, 18, 5, date_before_one)
        data_save(0, 0, 8, 18, 5, date_before_one)
        data_save(0, 0, 7, 18, 5, date_before_one)

        data_save(0, 0, 8, 17, 5, date_before_two)
        data_save(0, 0, 8, 17, 5, date_before_two)
        data_save(0, 0, 8, 17, 5, date_before_two)
        data_save(0, 0, 9, 17, 5, date_before_two)
        data_save(0, 0, 8, 17, 5, date_before_two)
        data_save(0, 0, 8, 17, 5, date_before_two)
        data_save(0, 0, 7, 17, 5, date_before_two)

        data_save(0, 0, 6, 17, 5, date_before_three)
        data_save(0, 0, 6, 18, 5, date_before_three)
        data_save(0, 0, 8, 18, 5, date_before_three)
        data_save(0, 0, 9, 17, 5, date_before_three)
        data_save(0, 0, 8, 17, 5, date_before_three)
        data_save(0, 0, 8, 17, 5, date_before_three)
        data_save(0, 0, 7, 17, 5, date_before_three)

    except Exception as e:
            print('Error: ', e)


def data_diagram(return_df=False, return_fig=False):
    import pandas as pd
    import plotly.express as px

    data_list = []
    conn.inst_select.execute('SELECT cd_nut, vl_nut_p, vl_nut_k, vl_nut_ph, vl_nut_um, vl_nut_lum, dt_data_reg FROM T_AGRO_NUTRIENTE')
    data = conn.inst_select.fetchall()

    for dt in data:
        data_list.append(dt)

    data_list = sorted(data_list)
    data_df = pd.DataFrame.from_records(data_list, columns=["ID", "P", "K", "PH", "UMIDADE", "LUMINOSIDADE", "DATA_HORA"])

    # Se o usuário quiser apenas o DataFrame
    if return_df:
        return data_df

    # Se o usuário quiser apenas a figura
    if return_fig:
        fig = px.line(data_df, x="DATA_HORA", y="PH", title="Variação do pH ao longo do tempo")
        fig.update_layout(
            xaxis_title="Data - Hora",
            yaxis_title="Nutriente pH"
        )
        return fig

    # Comportamento padrão: exibir o gráfico e o DataFrame no terminal
    print(data_df)
    fig = px.line(data_df, x="DATA_HORA", y="PH", title="Variação do pH ao longo do tempo")
    fig.update_layout(
        xaxis_title="Data - Hora",
        yaxis_title="Nutriente pH"
    )
    fig.show()

def inserir_dado(p, k, ph, umidade, luminosidade):
    datahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = """
        INSERT INTO T_AGRO_NUTRIENTE (
            VL_NUT_P, VL_NUT_K, VL_NUT_PH, VL_NUT_UM, VL_NUT_LUM, DT_DATA_REG
        ) VALUES (
            :1, :2, :3, :4, :5, TO_DATE(:6, 'YYYY-MM-DD HH24:MI:SS')
        )
    """
    conn.inst_include.execute(query, (p, k, ph, umidade, luminosidade, datahora))
    conn.conn.commit()