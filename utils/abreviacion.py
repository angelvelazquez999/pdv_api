vocales = "aeiouáéíóú"

def abreviacion(texto: str) -> str:
    texto = texto.replace(" ", "")  # elimina espacios
    return "".join(
        letra for letra in texto
        if letra.lower() not in vocales
    ).upper()
