cadena1 = 'texto uno'
cadena2 = 'texto dos'

# dir que metodos puedo usar en los tipo de texto
#print(dir(cadena1))

# Funcion
#resultado = upper(cadena1)

# Metodo
# Convertido en mayuscula
resultado = cadena1.upper()
print (resultado)
# Convertido en minuscula
resultado = resultado.lower()
print (resultado)
# Convertido en primer letra mayuscula
resultado = resultado.capitalize()
print (resultado)

# Convertido en buscar una cadena en otra
resultado = resultado.find("Texto")
print (resultado) # devuelve la posicion en donde esta el texto
# si tira -1 es decir que no existe

# Convertido en buscar una cadena dentro de otra cadean
resultado = cadena1.index("u")
print (resultado) # devuelve la posicion en donde esta el texto
#tira un lanza una excepcion 

# verifica si el texto solo tien nuemros
resultado_numerico = '18513215'
print (resultado_numerico.isnumeric())

# verifica si tiene texto
resultado_numerico = 'Benjamin'
print (resultado_numerico.isalpha())

#contar cuantas considencias 
resutlado_considencia = cadena1.count('u')
print (resutlado_considencia)

#contar cuantas considencias 
resutlado_size = len(cadena1)
print (resutlado_size)

# verificacion si la cadena empieza (start) con otra cadena , si no devuelve True
# verificacion si la cadena termina (end) con otra cadena , si no devuelve True
resutlado = cadena1.startswith('u')
print (resutlado)

# Replaza una parte por otra 
cadena1 = 'texto uno'
replaza = cadena1.replace('texto','hola')
print (replaza)

# Replaza una parte por otra 
cadena3 = 'benjamin de jesus perez aguilar'
replaza = cadena3.split(' ')
print (replaza)