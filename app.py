from PIL import Image
import os

# Rutas de las carpetas con imágenes PNG
carpetas = [
    "/Users/User/Desktop/PROYECTOS/PROYECTO 4/NCC-LSTM/caminando",
    "/Users/User/Desktop/PROYECTOS/PROYECTO 4/NCC-LSTM/escondiendo",
    "/Users/User/Desktop/PROYECTOS/PROYECTO 4/NCC-LSTM/caminando_salida",
    "/Users/User/Desktop/PROYECTOS/PROYECTO 4/NCC-LSTM/tomando_producto",
    "/Users/User/Desktop/PROYECTOS/PROYECTO 4/NCC-LSTM/saliendo"
]

# Crear una carpeta para guardar las imágenes JPG
carpeta_jpg = "/Users/User/Desktop/PROYECTOS/PROYECTO 4/NCC-LSTM/JPG"
os.makedirs(carpeta_jpg, exist_ok=True)

# Convertir todas las imágenes PNG a JPG
for carpeta in carpetas:
    nombre_carpeta = os.path.basename(carpeta)  # Obtener el nombre de la carpeta (caminando, escondiendo, etc.)
    nueva_carpeta = os.path.join(carpeta_jpg, nombre_carpeta)
    os.makedirs(nueva_carpeta, exist_ok=True)  # Crear una carpeta para las imágenes JPG
    
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".png"):
            ruta_png = os.path.join(carpeta, archivo)
            imagen = Image.open(ruta_png)
            
            # Convertir a JPG y guardar
            nombre_jpg = archivo.replace(".png", ".jpg")
            ruta_jpg = os.path.join(nueva_carpeta, nombre_jpg)
            imagen.convert("RGB").save(ruta_jpg, "JPEG")  # Convertir a RGB y guardar como JPG

print("Conversión de PNG a JPG completada.")