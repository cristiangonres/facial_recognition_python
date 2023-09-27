import cv2
import face_recognition
import numpy as np

foto_control = face_recognition.load_image_file("obama.jpg")
foto_prueba = face_recognition.load_image_file("obama2.jpg")

# TRANSFORMAR IMÁGENES A RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# LOCALIZAR CARA CONTROL
localizacion_control = face_recognition.face_locations(foto_control)[0]
face_encoding = face_recognition.face_encodings(foto_control)[0]

# MOSTRAR RECTÁNGULO
cv2.rectangle(foto_control, (localizacion_control[3], localizacion_control[0]), (localizacion_control[1], localizacion_control[2]), (0, 255, 0), 2)

# LOCALIZAR CARA CONTROL
localizacion_prueba = face_recognition.face_locations(foto_prueba)[0]
face_encoding2 = face_recognition.face_encodings(foto_prueba)[0]

# MOSTRAR RECTÁNGULO
cv2.rectangle(foto_prueba, (localizacion_prueba[3], localizacion_prueba[0]), (localizacion_prueba[1], localizacion_prueba[2]), (0, 255, 0), 2)

# COMPARAR CARAS
resultados = face_recognition.compare_faces([face_encoding], face_encoding2, 0.4)
print(resultados)

# Medir la distancia
distancia = face_recognition.face_distance([face_encoding], face_encoding2)
print(distancia)

cv2.putText(foto_prueba,
            f'{resultados} {distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 0, 255),
            2)

# MOSTRAR FOTOS
cv2.imshow("foto_control", foto_control)
cv2.imshow("foto_prueba", foto_prueba)

# MANTENER ABIERTO
cv2.waitKey(0)