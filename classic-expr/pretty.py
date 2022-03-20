from py3.classic_expressionParser import classic_expressionParser
from py3.classic_expressionVisitor import classic_expressionVisitor

class Visitor(classic_expressionVisitor):
    # Visit a parse tree produced by classic_expressionParser#file_.
    def visitFile_(self, ctx:classic_expressionParser.File_Context):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by classic_expressionParser#expr.
    def visitExpr(self, ctx:classic_expressionParser.ExprContext):
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).accept(self)
        lhs = ctx.getChild(0).accept(self)
        op = ctx.getChild(1).getSymbol()
        rhs = ctx.getChild(2).accept(self)
        return f"({lhs}{op.text}{rhs})"

    # Visit a parse tree produced by classic_expressionParser#term.
    def visitTerm(self, ctx:classic_expressionParser.TermContext):
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).accept(self)
        lhs = ctx.getChild(0).accept(self)
        op = ctx.getChild(1).getSymbol()
        rhs = ctx.getChild(2).accept(self)
        return f"({lhs}{op.text}{rhs})"

    # Visit a parse tree produced by classic_expressionParser#factor.
    def visitFactor(self, ctx:classic_expressionParser.FactorContext):
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).getSymbol().text
        return ctx.getChild(1).accept(self)
