from mysql.connector import Error
import mysql.connector
from data_random import data


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
        
        
        cursor.executemany("""INSERT INTO empleados(Employee_ID, Full_Name, Job_Title,
            Department, Business_Unit, Gender, Ethnicity, Age, Annual_Salary,
            Bonus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", data) 

        if (len(data) == cursor.rowcount):
            connection.commit()
            print("✅ {} Filas insertadas.".format(len(data)))

            # INSERCIÓN DE UNA CONSULTA SQL (SELECT)
            
            
            sql_select_all = "SELECT Employee_ID, Full_Name, Annual_Salary FROM empleados LIMIT 5"
            cursor.execute(sql_select_all)
            
            # Obtener y mostrar resultados
            resultados = cursor.fetchall()
            print("\n--- ✅ Resultados de la Consulta SQL (Primeras 5 filas) ---")
            
            for row in resultados:
               

                employee_id, full_name, annual_salary = row
                salario_formateado = "{:,}".format(annual_salary).replace(",", "X").replace(".", ",").replace("X", ".")
                print(f"ID: {employee_id}, Nombre: {full_name}, Salario: ${salario_formateado}")
            
            print("-----------------------------------------------------")

        else:
            connection.rollback()
            print("❌ Error de inserción. Rollback ejecutado.")
            
except Error as ex:
    print("❌ Error en la conexion o la operación: {}".format(ex))
finally:
    if connection and connection.is_connected():
        connection.close()
        print("Conexion cerrada.")