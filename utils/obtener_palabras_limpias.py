from pathlib import Path
import re
def obtener_palabras_limpias():
    file_path = Path(__file__).parent.parent / 'src' / "revolucion_francesa.txt"
    regex = r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ]'
    with open(file_path, "r", encoding="utf-8") as archivo:
        texto = archivo.read().lower()
        texto = re.sub(regex, " ", texto)
        palabras = texto.split()
    return palabras