#solicita datos para identificar al usuario
nombre = input("ingresa tu nombre: ")
print(f"hola, {nombre} bienvenido a la calculadora de años: ")
#solicita datos para la operacion propuesta.
año_nacimiento = int (input("ingresa tu año de nacimiento: "))
año_actual = int (input("ingresa el año actual: "))
#Calculo de la edad del usuario
edad = año_actual - año_nacimiento
#Envia los resultados al usuario
print (f"hola { nombre} tu edad es {edad} años")


#pedir al usuario el primer numero
num1 = int(input("ingresa el primer numero: "))
#pedir al usuario el segundo numero
num2 = int(input("ingresa el segundo numero: "))
#calcular la suma de ambos numeros
suma = num1 + num2
#mostrar el resultado de la suma
print (f"la suma de, {num1} y {num2} es: {suma} ")


#pedir la base de triangulo al usuario
base = float(input("introduce la base del triangulo en metros: "))
#pedir al usuario la altura de triangulo
altura = float(input("introduce la altura del triangulo en metros: "))
#calcular el area del triangulo
area = (base * altura) / 2
#mostrar el resultado al usuario
print (f"el area del trianfulo es igual a {area} m")



#pedir al usuario que ingrese la temperatura a grados celsius
celsius = float(input("introduce la temperatura en grados celsius: "))
#calcular la temperatura en farenheit
farenheit = (celsius * 9/5) + 32
#mostrar el resultado
print(f"{celsius} equivale a {farenheit} grados farenheit")

#consulta los tipos de variables usados anteriormente
print(type(celsius), type(num1), type(nombre), type(base), type(altura))


edad_actual = int(input("ingresa tu edad actual: " ))
edad_furura = edad_actual + 10
print (f"en 10 años tendras {edad_furura}años:")


#Verificar si es mayor o menor de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")