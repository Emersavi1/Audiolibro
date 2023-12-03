from gtts import gTTS

# Intenta leer el contenido del archivo
try:
    file = open('libro.txt', 'r', encoding='utf-8')
    textBook = file.read()
    file.close()
except FileNotFoundError:
    print("Error: El archivo 'libro.txt' no se encuentra en la ruta especificada")

# Agregar manejo de errores   
except Exception as e:
    print(f"Error al leer el archivo: {e}")

# Imprime el contenido del archivo    
print(textBook)    

# Continúa con la generación de audiosólo si lee el archivo
if 'textBook' in locals():
    audio = gTTS(text=textBook, lang='es')
    audio.save('audioBook.mp3') 
