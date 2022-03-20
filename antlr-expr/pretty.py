from py3.antlr_expressionParser import antlr_expressionParser
from py3.antlr_expressionVisitor import antlr_expressionVisitor

class Visitor(antlr_expressionVisitor):
    # Visit a parse tree produced by antlr_expressionParser#file_.
    def visitFile_(self, ctx:antlr_expressionParser.File_Context):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by antlr_expressionParser#expr.
    def visitExpr(self, ctx:antlr_expressionParser.ExprContext):
        if isinstance(ctx.getChild(0), antlr_expressionParser.ExprContext):
            lhs = ctx.getChild(0).accept(self)
            op = ctx.getChild(1).getSymbol()
            rhs = ctx.getChild(2).accept(self)
            return f"({lhs}{op.text}{rhs})"
        elif ctx.getChildCount() == 3:
            return ctx.getChild(1).accept(self)
        else: # ctx.getChildCount() == 1
            return ctx.getChild(0).getSymbol().text
