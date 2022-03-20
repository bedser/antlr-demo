# Generated from ./filter_expression.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .filter_expressionParser import filter_expressionParser
else:
    from filter_expressionParser import filter_expressionParser

# This class defines a complete generic visitor for a parse tree produced by filter_expressionParser.

class filter_expressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by filter_expressionParser#file_.
    def visitFile_(self, ctx:filter_expressionParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_expressionParser#expr.
    def visitExpr(self, ctx:filter_expressionParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_expressionParser#andExpr.
    def visitAndExpr(self, ctx:filter_expressionParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_expressionParser#relExpr.
    def visitRelExpr(self, ctx:filter_expressionParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by filter_expressionParser#literalExpr.
    def visitLiteralExpr(self, ctx:filter_expressionParser.LiteralExprContext):
        return self.visitChildren(ctx)



del filter_expressionParser