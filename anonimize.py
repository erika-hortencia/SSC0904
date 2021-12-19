import pandas as pd
import random
import json
import sqlConnection

"""
Function to import oracle database
"""
def importOracleDB():
    connection =  sqlConnection.connect()
    #Read database
    df = pd.read_sql("SELECT * FROM PACIENTE",connection)

    return df


"""
Function to delete the original database, finalizes anonimization by making the process irreversible
"""
def deleteDB():
    connection =  sqlConnection.connect()
    cur = connection.cursor()
    cur.execute("DELETE FROM PACIENTE")
    connection.commit()
    

"""
Auxiliary function no anonimize personal data by genarating random valid social security number
"""
def geraCPF():

    digits = []
    for number in range(11):
        number = random.randint(0,10)
        digits.append(number)
    
    result = ''.join(str(n) for n in digits)
    CPF = int(result)
    return CPF


"""
Function to create anonimized database
"""
def anonimize_database(origem):
    #Resets the json file
    filename = "./anonimized_data.json"
    records = []
    with open("./anonimized_data.json", 'w') as json_file:
            json.dump(records, json_file)

    #Reads dataframe, redacts sensitive info then writes is to json file
    for row in range(len(origem.index)):

        item_data = {}
        with open("./anonimized_data.json", 'r') as json_file:
            temp = json.load(json_file)
        item_data["ID_PACIENTE"] = int(origem.iat[row, 0])
        item_data["CPF"] = geraCPF()
        item_data["NOME"] = 'REDACTED'
        item_data["DATA_NASC"] = str(origem.iat[row, 3])
        item_data["DATA_REGISTRO"] = str(origem.iat[row, 4])
        item_data["SEXO"] = origem.iat[row, 5]
        item_data["ENDERECO"] = 'REDACTED'
        item_data["TELEFONE"] = 'REDACTED'
        item_data["MEDICO"] = origem.iat[row, 8]
        item_data["OCUPACAO"] =  'REDACTED' #origem.iat[row, 9]
        item_data["QUADRO"] = origem.iat[row, 10]
        temp.append(item_data)
        with open("./anonimized_data.json", 'w') as json_file:
            json.dump(temp, json_file, indent=4)
    
    #Returns an anonimized dataframe
    anondf = pd.read_json(filename, orient='columns')

    deleteDB()

    return anondf