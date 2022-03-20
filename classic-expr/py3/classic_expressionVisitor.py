# Generated from ./classic_expression.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .classic_expressionParser import classic_expressionParser
else:
    from classic_expressionParser import classic_expressionParser

# This class defines a complete generic visitor for a parse tree produced by classic_expressionParser.

class classic_expressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by classic_expressionParser#file_.
    def visitFile_(self, ctx:classic_expressionParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by classic_expressionParser#expr.
    def visitExpr(self, ctx:classic_expressionParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by classic_expressionParser#term.
    def visitTerm(self, ctx:classic_expressionParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by classic_expressionParser#factor.
    def visitFactor(self, ctx:classic_expressionParser.FactorContext):
        return self.visitChildren(ctx)



del classic_expressionParser