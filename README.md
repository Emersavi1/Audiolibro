# Audiolibro
Este código en Python tiene como objetivo principal leer un archivo de texto llamado 'libro.txt', imprimir su contenido y 
luego generar un archivo de audio en formato MP3 utilizando el módulo gTTS.
1. Lectura del Archivo:
- Se utiliza un bloque try-except para manejar excepciones.
- Intenta abrir el archivo 'libro.txt' en modo de lectura ('r') con codificación UTF-8.
- Si el archivo no se encuentra, imprime un mensaje de error específico para ese caso (FileNotFoundError).
- Si ocurre cualquier otra excepción durante la lectura del archivo, imprime un mensaje de error general (Exception).
- Si la lectura tiene éxito, el contenido del archivo se almacena en la variable textBook.

2. Impresión del Contenido del Archivo:
Imprime el contenido del archivo usando la función print. Este paso es opcional y se realiza solo con fines de verificación. 
El contenido se imprimirá incluso si hay un error al leer el archivo.

3. Generación de Audio:
- Verifica si la variable textBook está definida en el ámbito local (es decir, si se pudo leer el archivo correctamente).
- Si textBook está definido, utiliza el módulo gTTS para convertir el texto en voz.
- La voz se genera en español ('es').
- Guarda la salida de texto a voz en un archivo MP3 llamado 'audioBook.mp3'.

4. Manejo de Errores:
El código incluye manejo de errores para casos específicos, como la falta del archivo o cualquier otra excepción durante la lectura.

Resumiendo, el código siguiente lee un archivo de texto, imprime su contenido y genera un archivo de audio en MP3 con el contenido del archivo de texto. 
Además, maneja posibles errores durante la lectura del archivo.
