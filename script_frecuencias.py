from string import digits
import operator
def descartar(car):
    descartados = ['0','1','2','3','4','5','6','7','8','9'," ",".",",","\n"]
    return car in descartados

def obtener_frecuencia_de_caracteres(fichero):
    f = open(fichero)
    dicc_frecuencias = {}
    caracteres_totales = 0.0
    for linea in f:
        for caracter in linea:
            if not descartar(caracter):
                if dicc_frecuencias.has_key(caracter):
                    dicc_frecuencias[caracter] = dicc_frecuencias[caracter] + 1
                else:
                    dicc_frecuencias[caracter] = 1
                caracteres_totales += 1
    for k in dicc_frecuencias:
        dicc_frecuencias[k] = round((dicc_frecuencias[k] / caracteres_totales),4)
    dicc_frecuencias = sorted(dicc_frecuencias.items(), key=operator.itemgetter(1), reverse=True)
    print(dicc_frecuencias)
    return dicc_frecuencias

def sustituir_dos_mas_frecuentes(fichero,frecuencia_de_caracteres, traduccion):
    mas_frecuentes_texto = [frecuencia_de_caracteres[0][0],frecuencia_de_caracteres[1][0]]
    print(mas_frecuentes_texto[0])
    print(mas_frecuentes_texto[1])
    mas_frecuentes_absoluto = ['e','a','o','l','s','n','d','r','u','i','t','c','p','m','y','q','b','h','g','f','v','j','n','z','x','k','w']
    print(mas_frecuentes_absoluto[0])
    print(mas_frecuentes_absoluto[1])
    f = open(fichero)
    texto_sustituido = ''
    for linea in f:
        linea = linea.replace(mas_frecuentes_texto[0],mas_frecuentes_absoluto[0])
        linea = linea.replace(mas_frecuentes_texto[1],mas_frecuentes_absoluto[1])
        texto_sustituido = texto_sustituido + linea
    traduccion[mas_frecuentes_texto[0]] = mas_frecuentes_absoluto[0]
    traduccion[mas_frecuentes_texto[1]] = mas_frecuentes_absoluto[1]
    return texto_sustituido,traduccion

def sustituir(texto,traduccion):
    sustituido = input("Que otro caracter quiere sustituir\n")
    sustituto = input("Porque caracter lo quiere sustiuir\n")
    texto = texto.replace(sustituido,sustituto)
    if not traduccion.has_key(sustituido):
        traduccion[sustituido] =sustituto
    return texto,traduccion


directorio_mensaje = "texto_cifrado.txt"
traduccion = {}
frecuencias_texto = obtener_frecuencia_de_caracteres(directorio_mensaje)
print(frecuencias_texto)
res = input("Desea sustuir los dos caracteres mas frecuentes por los dos mas frecuentes en castellano (1 para si, 0 para no)\n")
if res != 0:
    texto,traduccion = sustituir_dos_mas_frecuentes(directorio_mensaje,frecuencias_texto, traduccion)
    print(texto)
    res = input("Desea sustituir mas letras (1 para si, 0 para no)\n")
    while res != 0:
        texto,traduccion = sustituir(texto,traduccion)
        print(texto)
        res = input("Desea sustituir mas letras (1 para si, 0 para no)\n")
    print(traduccion)