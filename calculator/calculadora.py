#erickgeovvani
#Declarando y asignando variables
1 == "suma"
2 == "resta"
3 == "multiplicacion"
4 == "division"
5 == "raiz"

a = 0
b = 0
c = 0

#Bienvenida
print("Bienvenido a Calculadora")
print("Escriba su nombre:")
#En espera de el input del usuario
nombre = input()
#Imprimir mensaje de bienvenida con el nombre del usuario.
print("Hola " + nombre + ". Bienvenido")
print("Selecciona la operación deseada.(Solo numero)")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.Raiz Cuadrada")
#En espera de seleccion
seleccion = input()

if 1:
    print("Elegiste Suma")
    print("Ingrese primera cifra")
    a = input()
    print("Ingrese segunda cifra")
    b = input()
    suma1 = int(a)
    suma2 = int(b)
    c = suma1 + suma2
    suma3 =str(c)
    print(a + " + " + b + " = " + suma3)

elif 2:
    print("Elegiste Resta")

else:
    print("Elegiste multiplicacion")


#erickgeo