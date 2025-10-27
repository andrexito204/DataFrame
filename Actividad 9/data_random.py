# data_random.py

from faker import Faker
import random

# 1. Inicialización
fake = Faker('es_CO')
data = [] 

# --- Listas Personalizadas para Campos Específicos ---

DEPARTMENTS = ['Ventas', 'Recursos Humanos', 'Ingeniería', 'Marketing', 'Finanzas', 'Operaciones', 'Servicios al Cliente']
BUSINESS_UNITS = ['Retail', 'Digital', 'Corporativo', 'Proyectos Especiales', 'Manufactura']
JOB_TITLES = ['Gerente', 'Analista Senior', 'Desarrollador Backend', 'Asistente Administrativo', 'Director', 'Especialista QA', 'Técnico de Soporte']
ETHNICITIES = ['Mestizo', 'Afrocolombiano', 'Indígena', 'Blanco', 'Otro']
GENDERS = ['Masculino', 'Femenino', 'No binario']

# Definimos cuántas filas queremos generar
NUM_RECORDS = 100

# 2. Bucle de Generación
for i in range(1, NUM_RECORDS + 1):
    
    # Datos Falsos Generados
    employee_id = i + 1
    full_name = fake.name() 
    job_title = random.choice(JOB_TITLES)
    department = random.choice(DEPARTMENTS)
    business_unit = random.choice(BUSINESS_UNITS)
    gender = random.choice(GENDERS)
    ethnicity = random.choice(ETHNICITIES)
    age = random.randint(22, 65)
    

    annual_salary = random.randint(30000000, 150000000) 
    bonus_amount = int(annual_salary * random.uniform(0.05, 0.25)) 
   
    # 3. Creación de la Tupla (¡Ahora con 10 elementos!)
    # El orden debe coincidir con la sentencia INSERT: (ID, Name, Title, Dept, etc.)
    record = (
        employee_id,      
        full_name,        
        job_title,        
        department,       
        business_unit,   
        gender,           
        ethnicity,        
        age,            
        annual_salary,   
        bonus_amount    
    )
    
    data.append(record)
