class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto_limpio = ''.join(filter(str.isalnum, texto.lower()))
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida
    
    def contar_vocales(self, texto):
        return sum(1 for char in texto.lower() if char in 'aeiou')
    
    def contar_consonantes(self, texto):
        return sum(1 for char in texto.lower() if char.isalpha() and char not in 'aeiou')
    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        return " ".join(p.capitalize() for p in texto.split())
    
    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())
    
    def es_numero_entero(self, texto):
        if texto.startswith("-"):
            texto = texto[1:]
        return all(char in "0123456789" for char in texto) and len(texto) > 0
    
    def cifrar_cesar(self, texto, desplazamiento):
        cifrado = ""
        for char in texto:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                cifrado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
            else:
                cifrado += char
        return cifrado
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones