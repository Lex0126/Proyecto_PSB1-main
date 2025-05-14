# Generated from ArduinoLite.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,2,1,2,1,
        2,1,2,5,2,73,8,2,10,2,12,2,76,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,3,18,185,8,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,193,8,18,10,
        18,12,18,196,9,18,1,19,1,19,1,19,0,1,36,20,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,0,3,1,0,1,2,1,0,3,4,1,0,20,25,199,
        0,46,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,79,1,0,0,0,8,86,1,0,0,0,
        10,91,1,0,0,0,12,98,1,0,0,0,14,105,1,0,0,0,16,110,1,0,0,0,18,114,
        1,0,0,0,20,123,1,0,0,0,22,130,1,0,0,0,24,139,1,0,0,0,26,146,1,0,
        0,0,28,151,1,0,0,0,30,156,1,0,0,0,32,161,1,0,0,0,34,172,1,0,0,0,
        36,184,1,0,0,0,38,197,1,0,0,0,40,41,3,2,1,0,41,42,5,32,0,0,42,45,
        1,0,0,0,43,45,3,4,2,0,44,40,1,0,0,0,44,43,1,0,0,0,45,48,1,0,0,0,
        46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,
        0,0,1,50,1,1,0,0,0,51,67,3,6,3,0,52,67,3,8,4,0,53,67,3,10,5,0,54,
        67,3,12,6,0,55,67,3,14,7,0,56,67,3,16,8,0,57,67,3,18,9,0,58,67,3,
        20,10,0,59,67,3,22,11,0,60,67,3,24,12,0,61,67,3,26,13,0,62,67,3,
        28,14,0,63,67,3,30,15,0,64,67,3,32,16,0,65,67,3,34,17,0,66,51,1,
        0,0,0,66,52,1,0,0,0,66,53,1,0,0,0,66,54,1,0,0,0,66,55,1,0,0,0,66,
        56,1,0,0,0,66,57,1,0,0,0,66,58,1,0,0,0,66,59,1,0,0,0,66,60,1,0,0,
        0,66,61,1,0,0,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,
        1,0,0,0,67,3,1,0,0,0,68,74,5,29,0,0,69,70,3,2,1,0,70,71,5,32,0,0,
        71,73,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,
        0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,30,0,0,78,5,1,0,0,0,79,
        80,5,5,0,0,80,81,5,27,0,0,81,82,3,36,18,0,82,83,5,31,0,0,83,84,3,
        36,18,0,84,85,5,28,0,0,85,7,1,0,0,0,86,87,5,6,0,0,87,88,5,27,0,0,
        88,89,3,36,18,0,89,90,5,28,0,0,90,9,1,0,0,0,91,92,5,33,0,0,92,93,
        5,26,0,0,93,94,5,7,0,0,94,95,5,27,0,0,95,96,3,36,18,0,96,97,5,28,
        0,0,97,11,1,0,0,0,98,99,5,8,0,0,99,100,5,27,0,0,100,101,3,36,18,
        0,101,102,5,31,0,0,102,103,3,36,18,0,103,104,5,28,0,0,104,13,1,0,
        0,0,105,106,5,9,0,0,106,107,5,27,0,0,107,108,3,36,18,0,108,109,5,
        28,0,0,109,15,1,0,0,0,110,111,5,33,0,0,111,112,5,26,0,0,112,113,
        3,36,18,0,113,17,1,0,0,0,114,115,5,10,0,0,115,116,5,27,0,0,116,117,
        3,36,18,0,117,118,3,38,19,0,118,119,3,36,18,0,119,120,5,28,0,0,120,
        121,5,11,0,0,121,122,3,4,2,0,122,19,1,0,0,0,123,124,5,12,0,0,124,
        125,5,27,0,0,125,126,3,36,18,0,126,127,5,31,0,0,127,128,3,36,18,
        0,128,129,5,28,0,0,129,21,1,0,0,0,130,131,5,13,0,0,131,132,5,27,
        0,0,132,133,3,36,18,0,133,134,5,31,0,0,134,135,3,36,18,0,135,136,
        5,31,0,0,136,137,5,35,0,0,137,138,5,28,0,0,138,23,1,0,0,0,139,140,
        5,14,0,0,140,141,5,27,0,0,141,142,3,36,18,0,142,143,5,31,0,0,143,
        144,3,36,18,0,144,145,5,28,0,0,145,25,1,0,0,0,146,147,5,15,0,0,147,
        148,5,27,0,0,148,149,3,36,18,0,149,150,5,28,0,0,150,27,1,0,0,0,151,
        152,5,16,0,0,152,153,5,27,0,0,153,154,3,36,18,0,154,155,5,28,0,0,
        155,29,1,0,0,0,156,157,5,17,0,0,157,158,5,27,0,0,158,159,3,36,18,
        0,159,160,5,28,0,0,160,31,1,0,0,0,161,162,5,18,0,0,162,163,5,27,
        0,0,163,164,3,36,18,0,164,165,5,31,0,0,165,166,3,36,18,0,166,167,
        5,31,0,0,167,168,3,36,18,0,168,169,5,31,0,0,169,170,3,36,18,0,170,
        171,5,28,0,0,171,33,1,0,0,0,172,173,5,19,0,0,173,174,5,27,0,0,174,
        175,3,36,18,0,175,176,5,31,0,0,176,177,3,36,18,0,177,178,5,31,0,
        0,178,179,3,36,18,0,179,180,5,28,0,0,180,35,1,0,0,0,181,182,6,18,
        -1,0,182,185,5,34,0,0,183,185,5,33,0,0,184,181,1,0,0,0,184,183,1,
        0,0,0,185,194,1,0,0,0,186,187,10,4,0,0,187,188,7,0,0,0,188,193,3,
        36,18,5,189,190,10,3,0,0,190,191,7,1,0,0,191,193,3,36,18,4,192,186,
        1,0,0,0,192,189,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,
        1,0,0,0,195,37,1,0,0,0,196,194,1,0,0,0,197,198,7,2,0,0,198,39,1,
        0,0,0,7,44,46,66,74,184,192,194
    ]

class ArduinoLiteParser ( Parser ):

    grammarFileName = "ArduinoLite.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'Prenderled'", 
                     "'Apagarled'", "'LeerSensor'", "'MoverServo'", "'Esperar'", 
                     "'si'", "'entonces'", "'TocarBuzzer'", "'EscribirLCD'", 
                     "'EncenderMotor'", "'ApagarMotor'", "'ActivarRele'", 
                     "'DesactivarRele'", "'PrenderRGB'", "'ApagarRGB'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'='", 
                     "'('", "')'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PRENDERLED", "APAGARLED", "LEERSENSOR", 
                      "MOVERSERVO", "ESPERAR", "SI", "ENTONCES", "TOCARBUZZER", 
                      "ESCRIBIRLCD", "ENCENDERMOTOR", "APAGARMOTOR", "ACTIVARRELE", 
                      "DESACTIVARRELE", "PRENDERRGB", "APAGARRGB", "EQ", 
                      "NEQ", "LT", "LE", "GT", "GE", "AS", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "COMMA", "SEMICOLON", "ID", "INT", 
                      "STRING", "WS", "COMMENT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_prenderled = 3
    RULE_apagarled = 4
    RULE_leersensor = 5
    RULE_moverservo = 6
    RULE_esperar = 7
    RULE_asignacion = 8
    RULE_condicion = 9
    RULE_tocarbuzzer = 10
    RULE_escribirlcd = 11
    RULE_encendermotor = 12
    RULE_apagarmotor = 13
    RULE_activarrele = 14
    RULE_desactivarrele = 15
    RULE_prenderrgb = 16
    RULE_apagarrgb = 17
    RULE_expr = 18
    RULE_comparador = 19

    ruleNames =  [ "program", "statement", "block", "prenderled", "apagarled", 
                   "leersensor", "moverservo", "esperar", "asignacion", 
                   "condicion", "tocarbuzzer", "escribirlcd", "encendermotor", 
                   "apagarmotor", "activarrele", "desactivarrele", "prenderrgb", 
                   "apagarrgb", "expr", "comparador" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PRENDERLED=5
    APAGARLED=6
    LEERSENSOR=7
    MOVERSERVO=8
    ESPERAR=9
    SI=10
    ENTONCES=11
    TOCARBUZZER=12
    ESCRIBIRLCD=13
    ENCENDERMOTOR=14
    APAGARMOTOR=15
    ACTIVARRELE=16
    DESACTIVARRELE=17
    PRENDERRGB=18
    APAGARRGB=19
    EQ=20
    NEQ=21
    LT=22
    LE=23
    GT=24
    GE=25
    AS=26
    LPAREN=27
    RPAREN=28
    LBRACE=29
    RBRACE=30
    COMMA=31
    SEMICOLON=32
    ID=33
    INT=34
    STRING=35
    WS=36
    COMMENT=37
    ERROR_CHAR=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ArduinoLiteParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.StatementContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ArduinoLiteParser.SEMICOLON)
            else:
                return self.getToken(ArduinoLiteParser.SEMICOLON, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.BlockContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.BlockContext,i)


        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ArduinoLiteParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9127851872) != 0):
                self.state = 44
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 33]:
                    self.state = 40
                    self.statement()
                    self.state = 41
                    self.match(ArduinoLiteParser.SEMICOLON)
                    pass
                elif token in [29]:
                    self.state = 43
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(ArduinoLiteParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prenderled(self):
            return self.getTypedRuleContext(ArduinoLiteParser.PrenderledContext,0)


        def apagarled(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ApagarledContext,0)


        def leersensor(self):
            return self.getTypedRuleContext(ArduinoLiteParser.LeersensorContext,0)


        def moverservo(self):
            return self.getTypedRuleContext(ArduinoLiteParser.MoverservoContext,0)


        def esperar(self):
            return self.getTypedRuleContext(ArduinoLiteParser.EsperarContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(ArduinoLiteParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(ArduinoLiteParser.CondicionContext,0)


        def tocarbuzzer(self):
            return self.getTypedRuleContext(ArduinoLiteParser.TocarbuzzerContext,0)


        def escribirlcd(self):
            return self.getTypedRuleContext(ArduinoLiteParser.EscribirlcdContext,0)


        def encendermotor(self):
            return self.getTypedRuleContext(ArduinoLiteParser.EncendermotorContext,0)


        def apagarmotor(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ApagarmotorContext,0)


        def activarrele(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ActivarreleContext,0)


        def desactivarrele(self):
            return self.getTypedRuleContext(ArduinoLiteParser.DesactivarreleContext,0)


        def prenderrgb(self):
            return self.getTypedRuleContext(ArduinoLiteParser.PrenderrgbContext,0)


        def apagarrgb(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ApagarrgbContext,0)


        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ArduinoLiteParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.prenderled()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.apagarled()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.leersensor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.moverservo()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.esperar()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.asignacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.condicion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.tocarbuzzer()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.escribirlcd()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 60
                self.encendermotor()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 61
                self.apagarmotor()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 62
                self.activarrele()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 63
                self.desactivarrele()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 64
                self.prenderrgb()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 65
                self.apagarrgb()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ArduinoLiteParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ArduinoLiteParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.StatementContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ArduinoLiteParser.SEMICOLON)
            else:
                return self.getToken(ArduinoLiteParser.SEMICOLON, i)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ArduinoLiteParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ArduinoLiteParser.LBRACE)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8590980960) != 0):
                self.state = 69
                self.statement()
                self.state = 70
                self.match(ArduinoLiteParser.SEMICOLON)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(ArduinoLiteParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrenderledContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRENDERLED(self):
            return self.getToken(ArduinoLiteParser.PRENDERLED, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(ArduinoLiteParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_prenderled

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrenderled" ):
                listener.enterPrenderled(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrenderled" ):
                listener.exitPrenderled(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrenderled" ):
                return visitor.visitPrenderled(self)
            else:
                return visitor.visitChildren(self)




    def prenderled(self):

        localctx = ArduinoLiteParser.PrenderledContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_prenderled)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ArduinoLiteParser.PRENDERLED)
            self.state = 80
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 81
            self.expr(0)
            self.state = 82
            self.match(ArduinoLiteParser.COMMA)
            self.state = 83
            self.expr(0)
            self.state = 84
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApagarledContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APAGARLED(self):
            return self.getToken(ArduinoLiteParser.APAGARLED, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_apagarled

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApagarled" ):
                listener.enterApagarled(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApagarled" ):
                listener.exitApagarled(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApagarled" ):
                return visitor.visitApagarled(self)
            else:
                return visitor.visitChildren(self)




    def apagarled(self):

        localctx = ArduinoLiteParser.ApagarledContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_apagarled)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ArduinoLiteParser.APAGARLED)
            self.state = 87
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 88
            self.expr(0)
            self.state = 89
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeersensorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArduinoLiteParser.ID, 0)

        def AS(self):
            return self.getToken(ArduinoLiteParser.AS, 0)

        def LEERSENSOR(self):
            return self.getToken(ArduinoLiteParser.LEERSENSOR, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_leersensor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeersensor" ):
                listener.enterLeersensor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeersensor" ):
                listener.exitLeersensor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeersensor" ):
                return visitor.visitLeersensor(self)
            else:
                return visitor.visitChildren(self)




    def leersensor(self):

        localctx = ArduinoLiteParser.LeersensorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_leersensor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ArduinoLiteParser.ID)
            self.state = 92
            self.match(ArduinoLiteParser.AS)
            self.state = 93
            self.match(ArduinoLiteParser.LEERSENSOR)
            self.state = 94
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 95
            self.expr(0)
            self.state = 96
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoverservoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVERSERVO(self):
            return self.getToken(ArduinoLiteParser.MOVERSERVO, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(ArduinoLiteParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_moverservo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoverservo" ):
                listener.enterMoverservo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoverservo" ):
                listener.exitMoverservo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoverservo" ):
                return visitor.visitMoverservo(self)
            else:
                return visitor.visitChildren(self)




    def moverservo(self):

        localctx = ArduinoLiteParser.MoverservoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_moverservo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ArduinoLiteParser.MOVERSERVO)
            self.state = 99
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 100
            self.expr(0)
            self.state = 101
            self.match(ArduinoLiteParser.COMMA)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EsperarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESPERAR(self):
            return self.getToken(ArduinoLiteParser.ESPERAR, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_esperar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEsperar" ):
                listener.enterEsperar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEsperar" ):
                listener.exitEsperar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEsperar" ):
                return visitor.visitEsperar(self)
            else:
                return visitor.visitChildren(self)




    def esperar(self):

        localctx = ArduinoLiteParser.EsperarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_esperar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ArduinoLiteParser.ESPERAR)
            self.state = 106
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 107
            self.expr(0)
            self.state = 108
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArduinoLiteParser.ID, 0)

        def AS(self):
            return self.getToken(ArduinoLiteParser.AS, 0)

        def expr(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,0)


        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = ArduinoLiteParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ArduinoLiteParser.ID)
            self.state = 111
            self.match(ArduinoLiteParser.AS)
            self.state = 112
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(ArduinoLiteParser.SI, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def comparador(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ComparadorContext,0)


        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def ENTONCES(self):
            return self.getToken(ArduinoLiteParser.ENTONCES, 0)

        def block(self):
            return self.getTypedRuleContext(ArduinoLiteParser.BlockContext,0)


        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = ArduinoLiteParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ArduinoLiteParser.SI)
            self.state = 115
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 116
            self.expr(0)
            self.state = 117
            self.comparador()
            self.state = 118
            self.expr(0)
            self.state = 119
            self.match(ArduinoLiteParser.RPAREN)
            self.state = 120
            self.match(ArduinoLiteParser.ENTONCES)
            self.state = 121
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TocarbuzzerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOCARBUZZER(self):
            return self.getToken(ArduinoLiteParser.TOCARBUZZER, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(ArduinoLiteParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_tocarbuzzer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTocarbuzzer" ):
                listener.enterTocarbuzzer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTocarbuzzer" ):
                listener.exitTocarbuzzer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTocarbuzzer" ):
                return visitor.visitTocarbuzzer(self)
            else:
                return visitor.visitChildren(self)




    def tocarbuzzer(self):

        localctx = ArduinoLiteParser.TocarbuzzerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tocarbuzzer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ArduinoLiteParser.TOCARBUZZER)
            self.state = 124
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 125
            self.expr(0)
            self.state = 126
            self.match(ArduinoLiteParser.COMMA)
            self.state = 127
            self.expr(0)
            self.state = 128
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscribirlcdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIBIRLCD(self):
            return self.getToken(ArduinoLiteParser.ESCRIBIRLCD, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ArduinoLiteParser.COMMA)
            else:
                return self.getToken(ArduinoLiteParser.COMMA, i)

        def STRING(self):
            return self.getToken(ArduinoLiteParser.STRING, 0)

        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_escribirlcd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscribirlcd" ):
                listener.enterEscribirlcd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscribirlcd" ):
                listener.exitEscribirlcd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscribirlcd" ):
                return visitor.visitEscribirlcd(self)
            else:
                return visitor.visitChildren(self)




    def escribirlcd(self):

        localctx = ArduinoLiteParser.EscribirlcdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_escribirlcd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ArduinoLiteParser.ESCRIBIRLCD)
            self.state = 131
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 132
            self.expr(0)
            self.state = 133
            self.match(ArduinoLiteParser.COMMA)
            self.state = 134
            self.expr(0)
            self.state = 135
            self.match(ArduinoLiteParser.COMMA)
            self.state = 136
            self.match(ArduinoLiteParser.STRING)
            self.state = 137
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EncendermotorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENCENDERMOTOR(self):
            return self.getToken(ArduinoLiteParser.ENCENDERMOTOR, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def COMMA(self):
            return self.getToken(ArduinoLiteParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_encendermotor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEncendermotor" ):
                listener.enterEncendermotor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEncendermotor" ):
                listener.exitEncendermotor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEncendermotor" ):
                return visitor.visitEncendermotor(self)
            else:
                return visitor.visitChildren(self)




    def encendermotor(self):

        localctx = ArduinoLiteParser.EncendermotorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_encendermotor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ArduinoLiteParser.ENCENDERMOTOR)
            self.state = 140
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 141
            self.expr(0)
            self.state = 142
            self.match(ArduinoLiteParser.COMMA)
            self.state = 143
            self.expr(0)
            self.state = 144
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApagarmotorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APAGARMOTOR(self):
            return self.getToken(ArduinoLiteParser.APAGARMOTOR, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_apagarmotor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApagarmotor" ):
                listener.enterApagarmotor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApagarmotor" ):
                listener.exitApagarmotor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApagarmotor" ):
                return visitor.visitApagarmotor(self)
            else:
                return visitor.visitChildren(self)




    def apagarmotor(self):

        localctx = ArduinoLiteParser.ApagarmotorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_apagarmotor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ArduinoLiteParser.APAGARMOTOR)
            self.state = 147
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 148
            self.expr(0)
            self.state = 149
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActivarreleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIVARRELE(self):
            return self.getToken(ArduinoLiteParser.ACTIVARRELE, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_activarrele

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActivarrele" ):
                listener.enterActivarrele(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActivarrele" ):
                listener.exitActivarrele(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActivarrele" ):
                return visitor.visitActivarrele(self)
            else:
                return visitor.visitChildren(self)




    def activarrele(self):

        localctx = ArduinoLiteParser.ActivarreleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_activarrele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ArduinoLiteParser.ACTIVARRELE)
            self.state = 152
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 153
            self.expr(0)
            self.state = 154
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DesactivarreleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESACTIVARRELE(self):
            return self.getToken(ArduinoLiteParser.DESACTIVARRELE, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_desactivarrele

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesactivarrele" ):
                listener.enterDesactivarrele(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesactivarrele" ):
                listener.exitDesactivarrele(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesactivarrele" ):
                return visitor.visitDesactivarrele(self)
            else:
                return visitor.visitChildren(self)




    def desactivarrele(self):

        localctx = ArduinoLiteParser.DesactivarreleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_desactivarrele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ArduinoLiteParser.DESACTIVARRELE)
            self.state = 157
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 158
            self.expr(0)
            self.state = 159
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrenderrgbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRENDERRGB(self):
            return self.getToken(ArduinoLiteParser.PRENDERRGB, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ArduinoLiteParser.COMMA)
            else:
                return self.getToken(ArduinoLiteParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_prenderrgb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrenderrgb" ):
                listener.enterPrenderrgb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrenderrgb" ):
                listener.exitPrenderrgb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrenderrgb" ):
                return visitor.visitPrenderrgb(self)
            else:
                return visitor.visitChildren(self)




    def prenderrgb(self):

        localctx = ArduinoLiteParser.PrenderrgbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_prenderrgb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ArduinoLiteParser.PRENDERRGB)
            self.state = 162
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 163
            self.expr(0)
            self.state = 164
            self.match(ArduinoLiteParser.COMMA)
            self.state = 165
            self.expr(0)
            self.state = 166
            self.match(ArduinoLiteParser.COMMA)
            self.state = 167
            self.expr(0)
            self.state = 168
            self.match(ArduinoLiteParser.COMMA)
            self.state = 169
            self.expr(0)
            self.state = 170
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApagarrgbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APAGARRGB(self):
            return self.getToken(ArduinoLiteParser.APAGARRGB, 0)

        def LPAREN(self):
            return self.getToken(ArduinoLiteParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ArduinoLiteParser.COMMA)
            else:
                return self.getToken(ArduinoLiteParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(ArduinoLiteParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_apagarrgb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApagarrgb" ):
                listener.enterApagarrgb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApagarrgb" ):
                listener.exitApagarrgb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApagarrgb" ):
                return visitor.visitApagarrgb(self)
            else:
                return visitor.visitChildren(self)




    def apagarrgb(self):

        localctx = ArduinoLiteParser.ApagarrgbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_apagarrgb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ArduinoLiteParser.APAGARRGB)
            self.state = 173
            self.match(ArduinoLiteParser.LPAREN)
            self.state = 174
            self.expr(0)
            self.state = 175
            self.match(ArduinoLiteParser.COMMA)
            self.state = 176
            self.expr(0)
            self.state = 177
            self.match(ArduinoLiteParser.COMMA)
            self.state = 178
            self.expr(0)
            self.state = 179
            self.match(ArduinoLiteParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def INT(self):
            return self.getToken(ArduinoLiteParser.INT, 0)

        def ID(self):
            return self.getToken(ArduinoLiteParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArduinoLiteParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArduinoLiteParser.ExprContext,i)


        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArduinoLiteParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 182
                self.match(ArduinoLiteParser.INT)
                pass
            elif token in [33]:
                self.state = 183
                self.match(ArduinoLiteParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 192
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ArduinoLiteParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 186
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 187
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ArduinoLiteParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 189
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 190
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expr(4)
                        pass

             
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(ArduinoLiteParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ArduinoLiteParser.NEQ, 0)

        def LT(self):
            return self.getToken(ArduinoLiteParser.LT, 0)

        def LE(self):
            return self.getToken(ArduinoLiteParser.LE, 0)

        def GT(self):
            return self.getToken(ArduinoLiteParser.GT, 0)

        def GE(self):
            return self.getToken(ArduinoLiteParser.GE, 0)

        def getRuleIndex(self):
            return ArduinoLiteParser.RULE_comparador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparador" ):
                listener.enterComparador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparador" ):
                listener.exitComparador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparador" ):
                return visitor.visitComparador(self)
            else:
                return visitor.visitChildren(self)




    def comparador(self):

        localctx = ArduinoLiteParser.ComparadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




