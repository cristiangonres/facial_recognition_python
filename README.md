# facial_recognition_python

```markdown
# Reconocimiento Facial en Tiempo Real

Este proyecto es un sistema de reconocimiento facial en tiempo real que utiliza la biblioteca OpenCV y Face Recognition en Python. El sistema es capaz de identificar personas en una transmisión de video en vivo y registrar sus ingresos en un archivo CSV.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- OpenCV (`pip install opencv-python`)
- Face Recognition (`pip install face-recognition`)

## Configuración de la Base de Datos

Este proyecto utiliza una base de datos de imágenes para entrenar el reconocimiento facial. Las imágenes deben estar organizadas en una carpeta llamada "personas". Cada imagen debe estar etiquetada con el nombre de la persona (por ejemplo, "nombre.jpg"). El código carga estas imágenes y las utiliza para entrenar el modelo de reconocimiento facial.

```python
ruta = "personas"
imagenes = []
nombres = []
lista_personas = os.listdir(ruta)
# ...
```

## Codificación de las Imágenes

Las imágenes cargadas se convierten a formato RGB y se codifican utilizando la biblioteca Face Recognition. Las codificaciones se almacenan en la lista `lista_personas_codificada`.

```python
lista_personas_codificada = codificar(imagenes)
# ...
```

## Reconocimiento Facial en Tiempo Real

El código captura el video de la cámara web en tiempo real y realiza el reconocimiento facial en cada fotograma.

```python
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# ...
```

El proceso de reconocimiento facial incluye:

- Detección de caras en el fotograma.
- Codificación de las caras detectadas.
- Comparación de las codificaciones con las codificaciones de la base de datos.
- Dibujado de un rectángulo y etiqueta en la cara si se reconoce a la persona.
- Registro de ingresos en un archivo CSV.

## Registro de Ingresos

El código registra los ingresos de las personas reconocidas en un archivo CSV llamado "registro.csv".

```python
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
```

## Ejecución

Para ejecutar el proyecto, simplemente ejecuta el script Python. Asegúrate de tener una cámara web conectada y que las imágenes de la base de datos estén en la carpeta "personas".

```bash
python asistencia.py
```

## Notas

- Asegúrate de tener todas las bibliotecas necesarias instaladas antes de ejecutar el proyecto.
- Personaliza la carpeta de imágenes y la configuración según tus necesidades.

Este proyecto es un ejemplo simple de reconocimiento facial en tiempo real en Python. Puedes ampliarlo y personalizarlo según tus requerimientos y necesidades.
```

