import sys
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # Ruta base = carpeta actual de este archivo
sys.path.append(os.path.join(BASE_DIR, "..")) # Agrega rutas al sys.path
import otras_f.f2 as f2
from funciones_python import funciones as f1


# ctrl b para ocultar barra lateral
# ctrl shift p para abrir paleta de comandos

            # c     sort line ascending en paleta de comandos
        # a           shift tab borrar identacion
    # b          alt ↑↓ mover linea arriba o abajo

lista_numeros = [5, 3, 8, 1, 2]
print(f2.mayor(lista_numeros))  #ctrl click te lleva a la funcion
print(f1.suma(lista_numeros))   #alt f12 abre la funcion en una ventana emergente
                                #ctrl p puedes buscar archivos por nombre y con @puedes buscar funciones dentro de un archivo

#ctrl shift -> o <- selecciona automaticamente una parte de la linea, con ctrl solo te mueves
#hacer cambio de nombre a todas las lista_numeros
# ctrl w y ctrl shift t funcionan para cerrar y reabrir
#ctrl shift k borra una linea
#aaaaa  ctrl shift l elige todas esas incidencias y luego se pueden borrar todas a la vez
#aaaaa  shift alt + arriba o abajo copia la linea inmediatamente
#aaaaa
#aaaaa
#aaaaa
#aaaaa

#ctrl alt arriba abajo para elegir mas de una linea y poder escribir en ellas a la vez (esc para salir)
# print("")
# print("")
# print("")
# print("")


#ctrl + l selecciona toda la linea pero deja el cursor abajo, con shift + end queda al final
z = "me llamo z y estoy ENSEÑANDOLE a esta criaturita a programar mas rapido"
y = "me llamo y y estoy enseñandole a esta CRIATURITA a programar mas rapido"
#palette: transform to uppercase, lowercase, titlecase, etc

#shift all i -> palette cursor end lines, pone cursor al final de cada linea 



# ctrl ñ abre y oculta terminal, ctrl shift ñ abre terminal nueva, tener extension de terminal instalada

#palette: :numero te lleva directo a esa linea (ctrl g)

#ctrl inicio y ctrl fin te llevan al inicio y fin del archivo

#con extension todo highlight poner //TODO: O //FIXME: y luego en palette poner todo highlight y aparece el listado de lo pendiente


#SHIFT ALT A comentario en varias lineas
#PALETTE: TOGGLE LINE COMMENT COMENTAR CODIGO DE UNA->>> CTRL + } (yo elegi shift + |)


# TODO: ejemplos
var="asies" #snippet prv



#snipet forej
suma_for= 0
for i in range(len(lista_numeros)):
    print(f"Elemento {i}: {lista_numeros[i]}") 
    contador += lista_numeros[i]
print(f"La suma de los elementos es: {suma_for}")







