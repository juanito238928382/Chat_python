from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 🧠 BASE DE CONOCIMIENTO LOCAL (AMPLIADA)
guia_python = {
    "variable": "Una variable es un espacio en memoria donde guardas datos. Ejemplo:\n\nx = 5\nnombre = 'Camila'\n\nSe usan para almacenar valores que pueden cambiar.",
    "python": "Python es un lenguaje de programación interpretado, fácil de aprender y usado en inteligencia artificial, web, videojuegos y ciencia de datos.",
    "funcion": "Una función es un bloque de código reutilizable. Se define con 'def'. Ejemplo:\n\ndef saludar():\n    print('Hola!')\n\nsaludar()",
    "for": "El bucle for se usa para repetir un bloque de código una cantidad de veces. Ejemplo:\n\nfor i in range(5):\n    print(i)",
    "while": "El bucle while repite un bloque mientras una condición sea verdadera. Ejemplo:\n\nx = 0\nwhile x < 5:\n    print(x)\n    x += 1",
    "if": "La sentencia if permite ejecutar código solo si se cumple una condición. Ejemplo:\n\nif edad >= 18:\n    print('Eres mayor de edad')",
    "lista": "Una lista guarda varios elementos en una sola variable. Ejemplo:\n\nfrutas = ['manzana', 'pera', 'uva']\nfrutas.append('mango')",
    "diccionario": "Un diccionario guarda datos en pares clave:valor. Ejemplo:\n\npersona = {'nombre': 'Ana', 'edad': 20}\nprint(persona['nombre'])",
    "tupla": "Una tupla es como una lista, pero sus valores no pueden cambiar. Ejemplo:\n\ncoordenadas = (10, 20)",
    "set": "Un set es una colección de elementos únicos. Ejemplo:\n\nnumeros = {1, 2, 3, 3}  # Resultado: {1, 2, 3}",
    "clase": "Una clase define el molde para crear objetos. Ejemplo:\n\nclass Persona:\n    def __init__(self, nombre):\n        self.nombre = nombre",
    "objeto": "Un objeto es una instancia de una clase. Tiene atributos (propiedades) y métodos (acciones). Ejemplo:\n\np = Persona('Ana')\nprint(p.nombre)",
    "poo": "La Programación Orientada a Objetos (POO) organiza el código en clases y objetos para hacerlo más ordenado y reutilizable.",
    "operadores": "Los operadores son símbolos que realizan operaciones matemáticas o lógicas. Ejemplo: +, -, *, /, %, **, //, ==, !=, >, <.",
    "comentarios": "Los comentarios explican el código. Se escriben con #. Ejemplo:\n\n# Esto es un comentario",
    "input": "La función input() permite pedir datos al usuario. Ejemplo:\n\nnombre = input('¿Cómo te llamas? ')\nprint('Hola', nombre)",
    "print": "La función print() muestra información en pantalla. Ejemplo:\n\nprint('Hola mundo!')",
    "tipos de datos": "Python tiene varios tipos: int (números), float (decimales), str (texto), bool (True/False), list, tuple, dict, set.",
    "modulo": "Un módulo es un archivo con código Python que puedes reutilizar. Se importa con 'import'. Ejemplo:\n\nimport math\nprint(math.sqrt(16))",
    "archivo": "Puedes abrir archivos con 'open'. Ejemplo:\n\nf = open('datos.txt', 'r')\ncontenido = f.read()\nf.close()",
    "excepcion": "Las excepciones se usan para manejar errores con try y except. Ejemplo:\n\ntry:\n    print(10/0)\nexcept:\n    print('Error al dividir')",
    "lambda": "Una función lambda es una función corta y anónima. Ejemplo:\n\ncuadrado = lambda x: x*x\nprint(cuadrado(5))",
    "import": "La palabra clave 'import' se usa para traer módulos. Ejemplo:\n\nimport random\nprint(random.randint(1,10))",
    "range": "La función range() genera una secuencia de números. Ejemplo:\n\nfor i in range(5):\n    print(i)",
    "len": "len() devuelve la longitud de una lista, cadena o diccionario. Ejemplo:\n\nlen('Hola') → 4",
    "type": "type() muestra el tipo de dato. Ejemplo:\n\ntype(3.14) → <class 'float'>"
}

# 🧩 FUNCIÓN PRINCIPAL PARA RESPONDER
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    for palabra_clave, respuesta in guia_python.items():
        if palabra_clave in mensaje:
            return respuesta
    return "No tengo una respuesta exacta para eso 😅, pero puedo ayudarte a buscar más información sobre Python."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preguntar', methods=['POST'])
def preguntar():
    datos = request.get_json()
    mensaje = datos.get('mensaje', '')
    respuesta = obtener_respuesta(mensaje)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
