import cv2
import face_recognition
import os
import numpy
from datetime import datetime


# Crear BD

ruta = "personas"
imagenes = []
nombres = []
lista_personas = os.listdir(ruta)

for nombre in lista_personas:
    imagen_actual = cv2.imread(f'{ruta}\{nombre}')
    imagenes.append(imagen_actual)
    nombres.append(os.path.splitext(nombre.title())[0])


def codificar(imagenes):
    # crear una lista nueva
    lista_codificada = []
    
    # pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        if len(face_recognition.face_encodings(imagen)) > 0:
            
            # codificar las imagenes
            codificacion = face_recognition.face_encodings(imagen)[0]
            # añadir la codificacion a la lista
            lista_codificada.append(codificacion)
        
    return lista_codificada


def registrar_ingresos(persona):
    f = open("registro.csv", "r+")
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(",")
        nombres_registro.append(ingreso[0])
    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime("%H:%M:%S")
        f.writelines(f'\n{persona}, {string_ahora}')
        

print(imagenes)
print(len(imagenes))
lista_personas_codificada = codificar(imagenes)

# tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de la camara
exito, imagen = captura.read()

if not exito:
    print("Ha fallado la captura")
else:
    # reconocer cara en captura
    cara_capturada = face_recognition.face_locations(imagen)
    # codificar cara
    cara_capturada_codificada = face_recognition.face_encodings(imagen, cara_capturada)
    # buscar coincidencias
    for caracod, caraubic in zip(cara_capturada_codificada, cara_capturada):
        coincidencias = face_recognition.compare_faces(lista_personas_codificada, caracod)
        distancias = face_recognition.face_distance(lista_personas_codificada, caracod)
        
        print(coincidencias)
        print(distancias)
        
        indice_coincidencias = numpy.argmin(distancias)
        
        print(f'indice de coincidencia de argmin {indice_coincidencias}')
        
        if distancias[indice_coincidencias] > 0.6:
            print("No coincide")
        else:
            nombre = nombres[indice_coincidencias]
            
            y1, x2, y2, x1 = caraubic
            
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.rectangle(imagen, (x1, y2-35), (x2, y2), (255, 0, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
            registrar_ingresos(nombre)
            cv2.imshow('Imagen Web', imagen)
            print("Coincide")
            cv2.waitKey(0)