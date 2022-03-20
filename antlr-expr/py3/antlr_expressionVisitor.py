# Generated from ./antlr_expression.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .antlr_expressionParser import antlr_expressionParser
else:
    from antlr_expressionParser import antlr_expressionParser

# This class defines a complete generic visitor for a parse tree produced by antlr_expressionParser.

class antlr_expressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by antlr_expressionParser#file_.
    def visitFile_(self, ctx:antlr_expressionParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by antlr_expressionParser#expr.
    def visitExpr(self, ctx:antlr_expressionParser.ExprContext):
        return self.visitChildren(ctx)



del antlr_expressionParser