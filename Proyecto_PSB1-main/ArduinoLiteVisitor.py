# Generated from ArduinoLite.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArduinoLiteParser import ArduinoLiteParser
else:
    from ArduinoLiteParser import ArduinoLiteParser

# This class defines a complete generic visitor for a parse tree produced by ArduinoLiteParser.

class ArduinoLiteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArduinoLiteParser#program.
    def visitProgram(self, ctx:ArduinoLiteParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#statement.
    def visitStatement(self, ctx:ArduinoLiteParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#block.
    def visitBlock(self, ctx:ArduinoLiteParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#prenderled.
    def visitPrenderled(self, ctx:ArduinoLiteParser.PrenderledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#apagarled.
    def visitApagarled(self, ctx:ArduinoLiteParser.ApagarledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#leersensor.
    def visitLeersensor(self, ctx:ArduinoLiteParser.LeersensorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#moverservo.
    def visitMoverservo(self, ctx:ArduinoLiteParser.MoverservoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#esperar.
    def visitEsperar(self, ctx:ArduinoLiteParser.EsperarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#asignacion.
    def visitAsignacion(self, ctx:ArduinoLiteParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#condicion.
    def visitCondicion(self, ctx:ArduinoLiteParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#tocarbuzzer.
    def visitTocarbuzzer(self, ctx:ArduinoLiteParser.TocarbuzzerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#escribirlcd.
    def visitEscribirlcd(self, ctx:ArduinoLiteParser.EscribirlcdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#encendermotor.
    def visitEncendermotor(self, ctx:ArduinoLiteParser.EncendermotorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#apagarmotor.
    def visitApagarmotor(self, ctx:ArduinoLiteParser.ApagarmotorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#activarrele.
    def visitActivarrele(self, ctx:ArduinoLiteParser.ActivarreleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#desactivarrele.
    def visitDesactivarrele(self, ctx:ArduinoLiteParser.DesactivarreleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#prenderrgb.
    def visitPrenderrgb(self, ctx:ArduinoLiteParser.PrenderrgbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#apagarrgb.
    def visitApagarrgb(self, ctx:ArduinoLiteParser.ApagarrgbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#expr.
    def visitExpr(self, ctx:ArduinoLiteParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoLiteParser#comparador.
    def visitComparador(self, ctx:ArduinoLiteParser.ComparadorContext):
        return self.visitChildren(ctx)



del ArduinoLiteParser