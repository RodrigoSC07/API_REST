import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
empleados = requests.get(url).json()
data = empleados['data']

# Cuantos empleados son:
total_empleados = 0
for empleado in data:
    total_empleados += 1
print(f'La empresa ha contratado {total_empleados} empleados en total')

# Cual es promedio de salario de los empleados
salarios = []
for salario in data:
    salarios.append(salario['employee_salary'])
promedio_salario = sum(salarios) / len(salarios)
print(f'El promedio de salario de los empleados es: {promedio_salario:.2f}')

# Cual es el promedio de edad de los empleados
edades = []
for edad in data:
    edades.append(edad['employee_age'])
promedio_edad = sum(edades) / len(edades)
print(f'El promedio de edad de los Analistas de Datos es: {promedio_edad:.2f}')

# Salario mínimo y máximo
salario_minimo = salarios[0]
salario_maximo = salarios[0]
for salario in salarios:
    if salario < salario_minimo:
        salario_minimo = salario
    elif salario > salario_maximo:
        salario_maximo = salario
print(f'El salario mínimo es: {salario_minimo} y el maximo es: {salario_maximo}')

# Cual es es la edad menor y mayor de los empleados
edad_menor = edades[0]
edad_mayor = edades[0]
for edad in edades:
    if edad < edad_menor:
        edad_menor = edad
    elif edad > edad_mayor:
        edad_mayor = edad
print(f'La edad menor de los empleados es: {edad_menor} y el mayor es: {edad_mayor}')
