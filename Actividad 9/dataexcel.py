import pandas as pd
from mysql.connector import Error
import mysql.connector


df = pd.read_excel('E:/Uniminutos/Base De Datos Relacionales/Actividad 9/data1.xlsx', sheet_name='Data')

filas = []

for index, row in df.iterrows():
	filas.append(row.tolist())


try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='mi_db_1'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO empleados(
        	Employee_ID,
        	Full_Name, 
        	Job_Title,
         	Department, 
         	Business_Unit, 
         	Gender, 
         	Ethnicity,
         	Age,
         	Annual_Salary,
         	Bonus, 
         	Country, 
         	City) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", filas)
        if (len(filas) == cursor.rowcount):
            connection.commit()
            print("{} Filas insertadas.".format(len(filas)))
        else:
            connection.rollback()

except Error as ex:
    print("Error en la conexion: {}".format(ex))

finally:
    if connection.is_connected():
        connection.close()
        print("Conexion cerrada.")


