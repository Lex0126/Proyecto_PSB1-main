from antlr4 import *
from ArduinoLiteLexer import ArduinoLiteLexer
from ArduinoLiteParser import ArduinoLiteParser  # Necesario para obtener nombres de tokens

def lexer(input_code):
    # Código de entrada de ejemplo

    # Crear flujo de entrada
    input_stream = InputStream(input_code)

    # Crear lexer y obtener tokens
    lexer = ArduinoLiteLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()  # Llenar todos los tokens del flujo

    # Obtener los nombres de los tokens desde el parser
    token_names = ArduinoLiteParser.symbolicNames

    print("--- TOKENS GENERADOS POR EL LEXER ---\n")
    for token in tokens.tokens:
        token_type = token.type
        token_name = token_names[token_type] if token_type < len(token_names) else str(token_type)
        print(f"Token: {token.text}\tTipo: {token_name}")

