from ArduinoLiteVisitor import ArduinoLiteVisitor
from ArduinoLiteParser import ArduinoLiteParser

class ArduinoIDEVisitor(ArduinoLiteVisitor):
    def visitProgram(self, ctx:ArduinoLiteParser.ProgramContext):
        print("\n--- VISITANDO PROGRAMA ---")
        return self.visitChildren(ctx)

    def visitPrenderled(self, ctx:ArduinoLiteParser.PrenderledContext):
        pin = ctx.expr(0).getText()
        estado = ctx.expr(1).getText()
        print(f"[Prenderled] Pin: {pin}, Estado: {estado}")
        return None

    def visitApagarled(self, ctx:ArduinoLiteParser.ApagarledContext):
        pin = ctx.expr().getText()
        print(f"[Apagarled] Pin: {pin}")
        return None

    def visitLeersensor(self, ctx:ArduinoLiteParser.LeersensorContext):
        var = ctx.ID().getText()
        pin = ctx.expr().getText()
        print(f"[LeerSensor] Variable: {var}, Pin: {pin}")
        return None

    def visitAsignacion(self, ctx:ArduinoLiteParser.AsignacionContext):
        var = ctx.ID().getText()
        val = ctx.expr().getText()
        print(f"[Asignacion] {var} = {val}")
        return None

    def visitEsperar(self, ctx:ArduinoLiteParser.EsperarContext):
        tiempo = ctx.expr().getText()
        print(f"[Esperar] Tiempo: {tiempo} ms")
        return None

    def visitMoverservo(self, ctx:ArduinoLiteParser.MoverservoContext):
        pin = ctx.expr(0).getText()
        grado = ctx.expr(1).getText()
        print(f"[MoverServo] Pin: {pin}, Grado: {grado}")
        return None

    def visitCondicion(self, ctx:ArduinoLiteParser.CondicionContext):
        left = ctx.expr(0).getText()
        right = ctx.expr(1).getText()
        op = ctx.comparador().getText()
        print(f"[Condición] Si {left} {op} {right} entonces...")
        self.visit(ctx.block())
        return None

    def visitBlock(self, ctx:ArduinoLiteParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None