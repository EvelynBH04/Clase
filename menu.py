import opcode
from webbrowser import Elinks
import aritmetica as a
import text as t

Opcion=int(input("Seleccione una opción del menú:"))

if Opcion == 1:
    N1= int(input("Ingrese valores para sumar:"))
    N2= int(input("Segundo valor: "))

    print(a.Sum(N1,N2))
elif Opcion==2:
    N1= int(input("ingrese el primer valor para realizar la resta"))
    N2= int(input("ingrese el segundo valor"))
elif Opcion==3:
    N1= int(input("ingrese el primer valor para realizar multimplicacion"))
    N2= int(input("ingrese el segundo valor"))
elif Opcion==4:
    N1= int(input("ingrese el primer valor para dividir"))
    N2= int(input("ingrese el segundo valor"))
elif Opcion==5:
    n1= int(input("ingrese el primer valor para realizar la potenciacion"))
    N2= int(input("ingrese el segundo valor"))
elif Opcion==6:
    N1= int(input("ingrese el primer valor para realizar la radicacion"))
elif Opcion==7:
    N1= int(input("ingrese el primer valor en radianes"))
elif Opcion==8:
    N1= int(input("ingrese el primer valor en radianes"))
elif Opcion==9:
    n1= int(input("ingrese el primer valor en radianes"))
elif Opcion==10:
    n1= int(input("ingresa el primer valor "))
    

print(a.Sum(N1,N2))
print(a.Sum(468,-781))
print(a.Sum(7751,78587))
print(a.Rest(1,-2))
print(a.Rest(1999,2028))
print(a.Rest(145,174))
print(a.Mult(1123,5))
print(a.Mult(100,749))
print(a.Mult(776,474))
print(a.Div(100,2))
print(a.Div(800,20))
print(a.Div(880,480))
print(a.Pot(20,5))
print(a.Pot(88,7))
print(a.Pot(854,784))
print(a.Rad(70))
print(a.Rad(475))
print(a.Rad(475))
print(a.Tan(76))
print(a.Tan(452))
print(a.Sin(45))
print(a.Sin(464))
print(a.Cos(59))
print(a.Cos(444))
print(a.Tan(66))
print(a.Log(8544))
print(a.Sum(56,45))
print(t.concat("Hola ","Mundo"))
print(t.concat("Buenas ","tardes"))
print(t.concat("Feliz "," Dia"))
print(t.concat("Mi Nombre Es"," Pepe"))