grammar ArduinoLite;

// --- Reglas del parser ---
program
    : (statement SEMICOLON | block)* EOF
    ;

statement
    : prenderled
    | apagarled
    | leersensor
    | moverservo
    | esperar
    | asignacion
    | condicion
    | tocarbuzzer
    | escribirlcd
    | encendermotor
    | apagarmotor
    | activarrele
    | desactivarrele
    | prenderrgb
    | apagarrgb
    ;

block
    : LBRACE (statement SEMICOLON)* RBRACE
    ;

// --- Instrucciones originales ---
prenderled     : PRENDERLED LPAREN expr COMMA expr RPAREN ;
apagarled      : APAGARLED LPAREN expr RPAREN ;
leersensor     : ID '=' LEERSENSOR LPAREN expr RPAREN ;
moverservo     : MOVERSERVO LPAREN expr COMMA expr RPAREN ;
esperar        : ESPERAR LPAREN expr RPAREN ;
asignacion     : ID '=' expr ;
condicion      : SI LPAREN expr comparador expr RPAREN ENTONCES block ;

// --- Instrucciones nuevas (actuadores) ---
tocarbuzzer    : TOCARBUZZER LPAREN expr COMMA expr RPAREN ;
escribirlcd    : ESCRIBIRLCD LPAREN expr COMMA expr COMMA STRING RPAREN ;
encendermotor  : ENCENDERMOTOR LPAREN expr COMMA expr RPAREN ;
apagarmotor    : APAGARMOTOR LPAREN expr RPAREN ;
activarrele    : ACTIVARRELE LPAREN expr RPAREN ;
desactivarrele : DESACTIVARRELE LPAREN expr RPAREN ;
prenderrgb     : PRENDERRGB LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN ;
apagarrgb      : APAGARRGB LPAREN expr COMMA expr COMMA expr RPAREN ;

// --- Expresiones y operadores ---
expr
    : expr op=('*'|'/') expr
    | expr op=('+'|'-') expr
    | INT
    | ID
    ;

comparador
    : EQ | NEQ | LT | LE | GT | GE
    ;

// --- Tokens del lexer ---
// Palabras clave
PRENDERLED      : 'Prenderled' ;
APAGARLED       : 'Apagarled' ;
LEERSENSOR      : 'LeerSensor' ;
MOVERSERVO      : 'MoverServo' ;
ESPERAR         : 'Esperar' ;
SI              : 'si' ;
ENTONCES        : 'entonces' ;
TOCARBUZZER     : 'TocarBuzzer' ;
ESCRIBIRLCD     : 'EscribirLCD' ;
ENCENDERMOTOR   : 'EncenderMotor' ;
APAGARMOTOR     : 'ApagarMotor' ;
ACTIVARRELE     : 'ActivarRele' ;
DESACTIVARRELE  : 'DesactivarRele' ;
PRENDERRGB      : 'PrenderRGB' ;
APAGARRGB       : 'ApagarRGB' ;

// Operadores de comparación
EQ      : '==' ;
NEQ     : '!=' ;
LT      : '<' ;
LE      : '<=' ;
GT      : '>' ;
GE      : '>=' ;
AS      : '=' ;

// Otros tokens
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACE      : '{' ;
RBRACE      : '}' ;
COMMA       : ',' ;
SEMICOLON   : ';' ;
ID          : [a-zA-Z_][a-zA-Z_0-9]* ;
INT         : [0-9]+ ;
STRING      : '"' (~["\r\n] | '\\"')* '"' ;
WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
//---error si encuentra simbolos no validos---
ERROR_CHAR: . { raise Exception("Se encontro un caracter no valido ") };
