import sys
import os
from markitdown import MarkItDown

def convertir_archivo(ruta_origen):
    # Verificar que el archivo exista
    if not os.path.exists(ruta_origen):
        print(f"Error: El archivo no existe en la ruta: {ruta_origen}")
        return

    # Obtener la ruta del directorio y el nombre del archivo sin extensión
    directorio_origen = os.path.dirname(ruta_origen)
    nombre_base = os.path.splitext(os.path.basename(ruta_origen))[0]
    
    # Construir la ruta de salida en la misma ubicación con extensión .md
    ruta_salida = os.path.join(directorio_origen, f"{nombre_base}.md")

    print(f"Procesando: {nombre_base}")
    print("Por favor, espera...")

    try:
        # Inicializar MarkItDown y convertir
        md = MarkItDown()
        resultado = md.convert(ruta_origen)
        
        # Guardar el archivo con codificación UTF-8 explícita
        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.write(resultado.text_content)
            
        print(f"\n¡Éxito! Archivo guardado en:\n{ruta_salida}")
    except Exception as e:
        print(f"\nOcurrió un error durante la conversión:\n{str(e)}")

if __name__ == "__main__":
    # Validar que se haya pasado un archivo como argumento
    if len(sys.argv) > 1:
        convertir_archivo(sys.argv[1])
    else:
        print("No se proporcionó ningún archivo. Arrastra un archivo sobre el ejecutable .bat")