#Importamos biblioteca para procesamiento de imagenes
import cv2

#Transformo la imágen  a escala de grises
imagen = cv2.imread('imagen.png' , cv2.IMREAD_GRAYSCALE)

umbral = 128
_, imagen_binaria = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)

cv2.imwrite('imagen_binaria.png',imagen_binaria)

# Nombre del archivo de texto donde se guardarán los valores binarios
nombre_archivo = 'valores_binarios.txt'

# Abre el archivo en modo escritura
with open(nombre_archivo, 'w') as archivo:
    for fila in imagen_binaria:
        for pixel in fila:
            archivo.write(f"{pixel} ")
        archivo.write("\n")

print(f"Valores binarios guardados en '{nombre_archivo}'.")

