from antlr4 import *
from ArduinoLiteLexer import ArduinoLiteLexer
from ArduinoLiteParser import ArduinoLiteParser

def afd(input_code):
    input_stream = InputStream(input_code)
    lexer = ArduinoLiteLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ArduinoLiteParser(token_stream)

    tree = parser.program()
    rule_names = parser.ruleNames

    transiciones = []

    def recorrer(nodo):
        actual = rule_names[nodo.getRuleIndex()] if hasattr(nodo, "getRuleIndex") else "TOKEN"
        for i in range(nodo.getChildCount()):
            hijo = nodo.getChild(i)
            siguiente = rule_names[hijo.getRuleIndex()] if hasattr(hijo, "getRuleIndex") else "TOKEN"
            peso = hijo.getText().replace("\n", " ").strip()
            transiciones.append(f"{actual} --{peso}--> {siguiente}")
            recorrer(hijo)

    recorrer(tree)

    print(" === Recorrido AFD ===\n")
    print(" -> ".join(transiciones))
