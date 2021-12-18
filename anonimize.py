import pandas as pd
import random
import sqlConnection

connection = sqlConnection.connect()

df = pd.read_sql("SELECT * FROM PACIENTE", connection)


def anonimize_rows(database):
    for row in database:
        row['OCUPACAO'] = 'REDACTED'

        yield row


def geraCPF():

    digits = []
    for number in range(11):
        number = random.randint(0,10)
        digits.append(number)
    
    result = ''.join(str(n) for n in digits)
    CPF = int(result)
    return CPF


def anonimize_database(origem, destino):
    for row in origem:
        idPaciente = origem['ID_PACIENTE']
        CPF = geraCPF()
        dataNascimento = origem['DATA_NASC']
        dataRegistro = origem['DATA_REGISTRO']
        sexo = origem['SEXO']
        endereco = 'REDACTED'
        telefone = 'REDACTED'
        medico = origem['MEDICO']
        ocupacao = origem['OCUPACAO']
        quadro = origem['QUADRO']

        sql_insert = f""" INSERT INTO PACIENTE_ANON VALUES({idPaciente}, {CPF}, TO_DATE('{dataNascimento}','dd/mm/yyyy'), 
                            TO_DATE('{dataRegistro}','dd/mm/yyyy'), '{sexo}', '{endereco}', '{telefone}', '{medico}', 
                                '{ocupacao}', '{quadro}') """
        try:
            cur = connection.cursor()
            cur.execute(sql_insert)
        except Exception as errormessage:
            print('Erro ao inserir os dados ' , errormessage)
        else:
            print('Dados inseridos com sucesso!')

#anonimize_rows(df)
#print(df)

print(geraCPF())