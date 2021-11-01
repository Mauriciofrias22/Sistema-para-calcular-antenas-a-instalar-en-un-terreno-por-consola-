# Sistema-para-calcular-antenas-a-instalar-en-un-terreno-por-consola-

sistema para determinar la cantidad a instalar de nuevas antenas para la transmisión de información en múltiples zonas rurales o de difícil acceso en varios departamentos, en pos del mejoramiento de la calidad de vida de los ciudadanos.
Para ello, el sistema debe leer la información del archivo data.csv, que contiene los siguientes campos / columnas:
•	id_department: El número identificador del departamento (entre 1 y 32).
•	department_name: El nombre del departamento donde se encuentra el terreno.
•	terrain_area: El área del terreno en el que se quieren instalar las nuevas antenas en m2.
•	old_antenna: La cantidad de antenas previamente instaladas (mayor o igual a 0).
•	new_antenna_type: El tipo de las nuevas antenas que se desean instalar (tipos ‘a’, ‘b’, ‘c’, ‘d’ o ‘e’).
Las antenas previamente instaladas tienen un rango de alcance de 8400 m2 y las nuevas antenas a instalar tienen un rango de 33600 m2, 48900 m2, 17000 m2, 21000 m2 y 42600 m2 para los tipos “a”, “b”, “c”, “d” y “e” respectivamente.
Si la cantidad de nuevas antenas a instalar es negativa, se toma la esta cantidad como 0.
Adicionalmente, se debe recibir como entrada varios números identificadores de distintos departamentos.

El programa debe mostrar por pantalla para cada uno de los departamentos leídos previamente, en orden ascendente, la siguiente información haciendo uso de los datos del archivo data.csv:
•	El número identificador del departamento y el nombre del departamento.
•	La cadena ‘terrain area’.
•	La cadena ‘mean’, seguido de la media (promedio) del área de todos los terrenos en ese departamento, formateado a 2 cifras decimales.
•	La cadena ‘std’, seguido de la desviación estándar muestral del área de todos los terrenos en ese departamento, formateado a 2 cifras decimales.
•	La cadena ‘min’, seguido del área mínima de los terrenos en ese departamento, formateado a 2 cifras decimales.
•	La cadena ‘max’, seguido del área máxima de los terrenos en ese departamento, formateado a 2 cifras decimales.
•	La cadena ‘total’, seguido de la suma de las áreas de todos los terrenos en ese departamento, formateado a 2 cifras decimales.
•	La cadena ‘old antenna’.
•	La cadena ‘mean’, seguido de la media (promedio) de la cantidad de todas las antenas previamente instaladas en ese departamento, formateado a 2 cifras decimales.
•	La cadena ‘std’, seguido de la desviación estándar muestral de la cantidad de todas las antenas previamente instaladas en ese departamento, formateado a 2 cifras decimales.
•	La cadena ‘min’, seguido de la cantidad mínima de antenas previamente instaladas en ese departamento.
•	La cadena ‘max’, seguido de la cantidad máxima de antenas previamente instaladas en ese departamento.
•	La cadena ‘total’, seguido del total de antenas previamente instaladas en ese departamento.
•	La cadena ‘new antenna’.
•	La cadena ‘a’, seguido de la cantidad total de nuevas antenas instaladas de tipo ‘a’ en ese departamento.
•	La cadena ‘b’, seguido de la cantidad total de nuevas antenas instaladas de tipo ‘b’ en ese departamento.
•	La cadena ‘c’, seguido de la cantidad total de nuevas antenas instaladas de tipo ‘c’ en ese departamento.
•	La cadena ‘d’, seguido de la cantidad total de nuevas antenas instaladas de tipo ‘d’ en ese departamento.
•	La cadena ‘e’, seguido de la cantidad total de nuevas antenas instaladas de tipo ‘e’ en ese departamento.

Ejemplos para prueba

Ejemplo 1

Entrada Esperada

1

Salida Esperada

1 Amazonas
terrain area
mean 1000421.50
std 577146.83
min 600.00
max 1999000.00
total 3136321400.00
old antenna
mean 15.14
std 8.79
min 0
max 30
total 47457
new antenna
a 16887
b 11835
c 32662
d 26492
e 12767


Ejemplo 2

Entrada Esperada

5 1 3

Salida Esperada

1 Amazonas
terrain area
mean 1000421.50
std 577146.83
min 600.00
max 1999000.00
total 3136321400.00
old antenna
mean 15.14
std 8.79
min 0
max 30
total 47457
new antenna
a 16887
b 11835
c 32662
d 26492
e 12767
3 Arauca
terrain area
mean 1013679.59
std 574310.27
min 200.00
max 1999000.00
total 3158625600.00
old antenna
mean 14.97
std 8.92
min 0
max 30
total 46635
new antenna
a 16410
b 11387
c 31782
d 26825
e 14481
5 Bolivar
terrain area
mean 1006779.55
std 573224.74
min 600.00
max 1998800.00
total 3170348800.00
old antenna
mean 14.84
std 8.81
min 0
max 30
total 46724
new antenna
a 15468
b 11410
c 36193
d 28089
e 13131
