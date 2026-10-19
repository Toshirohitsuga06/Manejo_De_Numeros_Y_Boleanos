"""
Nombre del alumno: Benjamin Balboa Acosta
Matrícula: 2630376
Ingeniería en Mecatrónica
Metodologia de la Programación
Universidad Politécnica de Victoria
Nombre del archivo: 2630376_BalboaBenjamin.py


RESUMEN EJECUTIVO

Las variables tipo int son variables que almacenan numeros enteros 
las variables tipo float almacenan numeros deciales y las variables 
tipo bool almacenan valores de verdadero o falso. las tipo int pueden
almacenar un 2 mientras que las float pueden almacenar un 2.5 y las 
bool pueden almacenar un true o false a traves de una comparacion, si
se cumple con lo que se esta compranado se considera verdadero, si no
se considera falso, es importante revisar los datos que se usan ya que 
existen casos de indeterminacion o de una equivalencia imposible, como 
una division entre cero y una conversion de grados Celsius a kelvin.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Usar tipos de datos apropiados: int para contadores/números enteros, 
  float para decimales, bool para banderas lógicas.
- Evitar duplicar expresiones complejas guardando resultados intermedios 
  en variables descriptivas en lower_snake_case.
- Validar los datos antes de procesar (verificando rangos, valores no 
  negativos y evitando divisiones entre cero).
- Usar UPPER_SNAKE_CASE para los valores constantes.
- Documentar claramente el significado de los booleanos en cada contexto.
"""



"""
Problema 1: Conversor de temperatura y bandera de rango
Descripción: Convierte una temperatura en grados Celsius (float) a Fahrenheit 
y Kelvin. Determina si la temperatura es alta (>= 30.0 °C).

Entradas:
- temp_c (float; temperatura en °C)

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "Temperatura alta:" verdadero|falso

Validaciones:
- Verificar que temp_c contenga caracteres numéricos válidos.
- No permitir temperaturas físicas imposibles en Kelvin (temp_k < 0.0, es decir, temp_c < -273.15).

Casos de prueba:
1) Normal: 25.5 -> Fahrenheit: 77.9, Kelvin: 298.65, Temperatura alta: falso
2) Borde: 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15, Temperatura alta: verdadero
3) Error: "abc" o -300.0 -> "Error: entrada inválida"
"""

print("\n- Problema 1: Conversor de Temperatura -")
temp_c_input = input("Ingrese la temperatura en Celsius: ").strip()

# Validar si es un número flotante 
clean_text = temp_c_input
if clean_text.startswith("-"):
    clean_text = clean_text[1:]

dots = 0
is_valid_float = len(clean_text) > 0 and clean_text != "."
for char in clean_text:
    if char == ".":
        dots += 1
        if dots > 1:
            is_valid_float = False
    elif not char.isdigit():
        is_valid_float = False

if not is_valid_float:
    print("Error: entrada inválida")
else:
    temp_c = float(temp_c_input)
    if temp_c < -273.15:
        print("Error: entrada inválida")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0
        
        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"Temperatura alta: {'verdadero' if is_high_temperature else 'falso'}")


"""
Problema 2: Horas de trabajo y pago de horas extra
Descripción: Calcula el pago total semanal de un trabajador. Hasta 40 horas 
se pagan a la tarifa normal; las horas extra (> 40) se pagan al 150%.

Entradas:
- hours_worked (float)
- hourly_rate (float)

Salidas:
- "Pago regular:" <regular_pay>
- "Pago de horas extra:" <overtime_pay>
- "Pago total:" <total_pay>
- "Tiene horas extra:" verdadero|falso

Validaciones:
- hours_worked >= 0, hourly_rate > 0. De lo contrario, "Error: entrada inválida".

Casos de prueba:
1) Normal: 45 horas, tarifa 10.0 -> Pago regular: 400.0, Pago de horas extra: 75.0, Pago total: 475.0, Tiene horas extra: verdadero
2) Borde: 40 horas, tarifa 15.5 -> Pago regular: 620.0, Pago de horas extra: 0.0, Pago total: 620.0, Tiene horas extra: falso
3) Error: -5 horas, tarifa 10.0 -> "Error: entrada inválida"
"""

print("\n- Problema 2: Horas de Trabajo y Horas Extra -")
hours_input = input("Ingrese las horas trabajadas: ").strip()
rate_input = input("Ingrese la tarifa por hora: ").strip()

# horas trabajadas
clean_hours = hours_input
dots = 0 #contador
valid_hours = len(clean_hours) > 0 and clean_hours != "."
for char in clean_hours:
    if char == ".":
        dots += 1
        if dots > 1:
            valid_hours = False
    elif not char.isdigit():
        valid_hours = False

clean_rate = rate_input
dots = 0
valid_rate = len(clean_rate) > 0 and clean_rate != "."
for char in clean_rate:
    if char == ".":
        dots += 1
        if dots > 1:
            valid_rate = False
    elif not char.isdigit():
        valid_rate = False

if not valid_hours or not valid_rate:
    print("Error: entrada inválida")
else:
    hours_worked = float(hours_input)
    hourly_rate = float(rate_input)
    
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: entrada inválida")
    else:
        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(0.0, hours_worked - 40.0)
        
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40.0
        
        print(f"Pago regular: {regular_pay}")
        print(f"Pago de horas extra: {overtime_pay}")
        print(f"Pago total: {total_pay}")
        print(f"Tiene horas extra: {'verdadero' if has_overtime else 'falso'}")


"""
Problema 3: Elegibilidad de descuento con booleanos
Descripción: Determina si un cliente obtiene un descuento basado en su estatus 
de estudiante, adulto mayor o si el total de la compra es >= 1000.0. 
Aplica un 10% de descuento si es elegible.

Entradas:
- purchase_total (float)
- is_student_text (string: "SI" o "NO")
- is_senior_text (string: "SI" o "NO")

Salidas:
- "Elegible para descuento:" verdadero|falso
- "Total final:" <final_total>

Validaciones:
- purchase_total >= 0.0
- El texto debe ser "SI" o "NO". De lo contrario, "Error: entrada inválida".

Casos de prueba:
1) Normal: 500.0, "SI", "NO" -> Elegible para descuento: verdadero, Total final: 450.0
2) Borde: 1000.0, "NO", "NO" -> Elegible para descuento: verdadero, Total final: 900.0
3) Error: 200.0, "TAL VEZ", "NO" -> "Error: entrada inválida"
"""

print("\n- Problema 3: Elegibilidad de Descuento -")
total_input = input("Ingrese el total de la compra: ").strip()
is_student_text = input("¿Es estudiante? (SI/NO): ").strip().upper()
is_senior_text = input("¿Es adulto mayor? (SI/NO): ").strip().upper()

clean_total = total_input
dots = 0
valid_total = len(clean_total) > 0 and clean_total != "."
for char in clean_total:
    if char == ".":
        dots += 1
        if dots > 1:
            valid_total = False
    elif not char.isdigit():
        valid_total = False

if not valid_total or is_student_text not in ("SI", "NO") or is_senior_text not in ("SI", "NO"):
    print("Error: entrada inválida")
else:
    purchase_total = float(total_input)
    if purchase_total < 0.0:
        print("Error: entrada inválida")
    else:
        is_student = (is_student_text == "SI")
        is_senior = (is_senior_text == "SI")
        
        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        
        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total
            
        print(f"Elegible para descuento: {'verdadero' if discount_eligible else 'falso'}")
        print(f"Total final: {final_total}")


"""
Problema 4: Estadísticas básicas de tres enteros
Descripción: Lee tres números enteros y calcula: suma, promedio, valor máximo, 
valor mínimo y si todos los números son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Suma:" <sum_value>
- "Promedio:" <average_value>
- "Máximo:" <max_value>
- "Mínimo:" <min_value>
- "Todos pares:" verdadero|falso

Validaciones:
- Verificar que los tres valores se puedan convertir a int.

Casos de prueba:
1) Normal: 4, 8, 12 -> Suma: 24, Promedio: 8.0, Máximo: 12, Mínimo: 4, Todos pares: verdadero
2) Borde: 0, 0, 0 -> Suma: 0, Promedio: 0.0, Máximo: 0, Mínimo: 0, Todos pares: verdadero
3) Error: 5, "abc", 10 -> "Error: entrada inválida"
"""

print("\n- Problema 4: Estadísticas Básicas de Tres Enteros -")
n1_input = input("Ingrese el primer entero (n1): ").strip()
n2_input = input("Ingrese el segundo entero (n2): ").strip()
n3_input = input("Ingrese el tercer entero (n3): ").strip()

# Validar enteros (pueden ser negativos)
v1 = n1_input[1:] if n1_input.startswith("-") else n1_input
v2 = n2_input[1:] if n2_input.startswith("-") else n2_input
v3 = n3_input[1:] if n3_input.startswith("-") else n3_input

valid_n1 = v1.isdigit()
valid_n2 = v2.isdigit()
valid_n3 = v3.isdigit()

if not (valid_n1 and valid_n2 and valid_n3):
    print("Error: entrada inválida")
else:
    n1 = int(n1_input)
    n2 = int(n2_input)
    n3 = int(n3_input)
    
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    
    print(f"Suma: {sum_value}")
    print(f"Promedio: {average_value}")
    print(f"Máximo: {max_value}")
    print(f"Mínimo: {min_value}")
    print(f"Todos pares: {'verdadero' if all_even else 'falso'}")

"""
Problema 5: Elegibilidad de préstamo (ingresos y relación de deuda)
Descripción: Determina si una persona es elegible para un préstamo según 
sus ingresos mensuales, deuda mensual y puntaje de crédito.

Entradas:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)

Salidas:
- "Relación de deuda:" <debt_ratio>
- "Elegible:" verdadero|falso

Validaciones:
- monthly_income > 0.0, monthly_debt >= 0.0, credit_score >= 0. De lo contrario, "Error: entrada inválida".

Casos de prueba:
1) Normal: 10000.0, 3000.0, 700 -> Relación de deuda: 0.3, Elegible: verdadero
2) Borde: 8000.0, 3200.0, 650 -> Relación de deuda: 0.4, Elegible: verdadero
3) Error: 0.0, 500.0, 700 -> "Error: entrada inválida"
"""

print("\n- Problema 5: Elegibilidad de Préstamo -")
income_input = input("Ingrese los ingresos mensuales: ").strip()
debt_input = input("Ingrese la deuda mensual: ").strip()
score_input = input("Ingrese el puntaje de crédito: ").strip()

# Validar income (float)
dots = 0
valid_income = len(income_input) > 0 and income_input != "."
for char in income_input:
    if char == ".":
        dots += 1
        if dots > 1:
            valid_income = False
    elif not char.isdigit():
        valid_income = False

# Validar debt (float)
dots = 0
valid_debt = len(debt_input) > 0 and debt_input != "."
for char in debt_input:
    if char == ".":
        dots += 1
        if dots > 1:
            valid_debt = False
    elif not char.isdigit():
        valid_debt = False

# Validar score (int)
valid_score = score_input.isdigit()

if not (valid_income and valid_debt and valid_score):
    print("Error: entrada inválida")
else:
    monthly_income = float(income_input)
    monthly_debt = float(debt_input)
    credit_score = int(score_input)
    
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: entrada inválida")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
        
        print(f"Relación de deuda: {debt_ratio}")
        print(f"Elegible: {'verdadero' if eligible else 'falso'}")

"""
Problema 6: Índice de Masa Corporal (IMC) y bandera de categoría
Descripción: Calcula el Índice de Masa Corporal (BMI) y determina las 
banderas de categoría (bajo peso, normal, sobrepeso).

Entradas:
- weight_kg (float)
- height_m (float)

Salidas:
- "IMC:" <bmi_redondeado>
- "Bajo peso:" verdadero|falso
- "Normal:" verdadero|falso
- "Sobrepeso:" verdadero|falso

Validaciones:
- weight_kg > 0.0, height_m > 0.0. De lo contrario, "Error: entrada inválida".

Casos de prueba:
1) Normal: 70.5, 1.75 -> IMC: 23.02, Bajo peso: falso, Normal: verdadero, Sobrepeso: falso
2) Borde: 56.5, 1.75 -> IMC: 18.45, Bajo peso: verdadero, Normal: falso, Sobrepeso: falso
3) Error: -70.0, 1.75 -> "Error: entrada inválida"
"""

print("\n- Problema 6: Índice de Masa Corporal (IMC) -")
weight_input = input("Ingrese el peso en kg: ").strip()
height_input = input("Ingrese la estatura en metros: ").strip()

# Validar weight (float)
dots = 0
valid_weight = len(weight_input) > 0 and weight_input != "."
for char in weight_input:
    if char == ".":
        dots += 1
        if dots > 1:
            valid_weight = False
    elif not char.isdigit():
        valid_weight = False

# Validar height (float)
dots = 0
valid_height = len(height_input) > 0 and height_input != "."
for char in height_input:
    if char == ".":
        dots += 1
        if dots > 1:
            valid_height = False
    elif not char.isdigit():
        valid_height = False

if not (valid_weight and valid_height):
    print("Error: entrada inválida")
else:
    weight_kg = float(weight_input)
    height_m = float(height_input)
    
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: entrada inválida")
    else:
        bmi = weight_kg / (height_m * height_m)
        rounded_bmi = round(bmi, 2)
        
        is_underweight = bmi < 18.5
        is_normal = (bmi >= 18.5) and (bmi < 25.0)
        is_overweight = bmi >= 25.0
        
        print(f"IMC: {rounded_bmi}")
        print(f"Bajo peso: {'verdadero' if is_underweight else 'falso'}")
        print(f"Normal: {'verdadero' if is_normal else 'falso'}")
        print(f"Sobrepeso: {'verdadero' if is_overweight else 'falso'}")

"""
CONCLUSIONES

Los numeros enteros y flotantes son utiles de manera independiente pero
aun mas cuando se usan en conjunto para realizar operaciones matematicas
ya que cumplen una funcion distina, los enteros son utiles para contar 
y los flotantes para medir cantidades exactas con decimales, mientras que los 
boleanos son utiles para determinar si una condicion es verdadera o falsa, y se
verfiica comparando dos valores, si se cumple la condicion es verdadero y si no es falso,
por ejemplo si se compara 5 > 3 es verdadero y si se compara 4 > 5 es falso y en base a 
eso se toma una decision y estos 3 pueden usarse para solucionar muchos tipos de problemas, como se vio en los problemas resueltos en este archivo.


REFERENCIAS:
1) Python Software Foundation. Built-in Types: Numeric Types (int, float). 
   URL: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
2) Python Software Foundation. Boolean Operations and Truth Value Testing. 
   URL: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
3) Real Python. Basic Input and Output in Python. 
   URL: https://realpython.com/python-input-output/
4) W3Schools. Python Operators (Arithmetic, Comparison, Logical). 
   URL: https://www.w3schools.com/python/python_operators.asp
5) GeeksforGeeks. Python Type Conversion and Casting. 
   URL: https://www.geeksforgeeks.org/type-conversion-in-python/
"""

#Repositorio de GitHub: https://github.com/Toshirohitsuga06/Manejo_De_Numeros_Y_Boleanos.git
