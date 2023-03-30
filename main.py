import re

# Definir palabras clave en C
claves = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern',
            'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

# Definir operadores en C
operadores = ['+', '-', '*', '/', '%', '=', '++', '--', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~',
             '<<', '>>', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=']

# Definir signos de puntuación en C
separadores = ['(', ')', '{', '}', '[', ']', ';', ',', '.', ':']


# Función para determinar si una cadena es un identificador válido
def esIdentificador(token):
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
        return True
    return False



# Función para determinar si una cadena es un número válido
def esNumero(token):
    if re.match(r'^[0-9]+(\.[0-9]+)?$', token):
        return True
    return False


# Función para dividir la cadena de código fuente en tokens
def tokenizar(code):
    # Agregar un espacio en blanco antes y después de cada signo de puntuación
    for p in separadores:
        code = code.replace(p, ' ' + p + ' ')

    # Dividir la cadena en palabras y eliminar espacios en blanco innecesarios
    tokens = code.split()

    # Eliminar comentarios de una o varias líneas
    tokens = [t for t in tokens if not t.startswith('/*') and not t.endswith('*/')]

    # Eliminar comentarios de una sola línea
    tokens = [t for t in tokens if not t.startswith('//')]

    # Identificar cada token
    for i in range(len(tokens)):
        token = tokens[i]
        if token in claves:
            tokens[i] = ('Reservada', token)
        elif token in operadores:
            tokens[i] = ('Operador', token)
        elif token in separadores:
            tokens[i] = ('Separador', token)
        elif esNumero(token):
            tokens[i] = ('Numero', token)
        elif esIdentificador(token):
            tokens[i] = ('Identificador', token)
        else:
            tokens[i] = ('unknown', token)
    return tokens


def limpiador():
    a_file = open("Codigo.txt")
    contenido = a_file.read()
    contenido = contenido.replace("\\n", '')
    print(contenido)
    return contenido


print(tokenizar(limpiador()))