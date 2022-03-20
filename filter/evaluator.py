from py3.filter_expressionLexer import filter_expressionLexer
from py3.filter_expressionParser import filter_expressionParser
from py3.filter_expressionVisitor import filter_expressionVisitor
import re

class Visitor(filter_expressionVisitor):
    def __init__(self, data):
        self.data = data # [{col -> value}]

    # Visit a parse tree produced by filter_expressionParser#file_.
    def visitFile_(self, ctx:filter_expressionParser.File_Context):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by filter_expressionParser#expr.
    def visitExpr(self, ctx:filter_expressionParser.ExprContext):
        # -> andExpr
        if isinstance(ctx.getChild(0), filter_expressionParser.AndExprContext):
            return ctx.getChild(0).accept(self)
        # -> expr "or" expr
        elif isinstance(ctx.getChild(0), filter_expressionParser.ExprContext):
            v1 = ctx.getChild(0).accept(self)
            assert ctx.getChild(1).getSymbol().text == "or"
            v2 = ctx.getChild(2).accept(self)
            return v1.union(v2)

    # Visit a parse tree produced by filter_expressionParser#andExpr.
    def visitAndExpr(self, ctx:filter_expressionParser.AndExprContext):
        # -> relExpr
        if isinstance(ctx.getChild(0), filter_expressionParser.RelExprContext):
            return ctx.getChild(0).accept(self)
        # -> andExpr "and" relExpr 
        elif isinstance(ctx.getChild(0), filter_expressionParser.AndExprContext):
            v1 = ctx.getChild(0).accept(self)
            assert ctx.getChild(1).getSymbol().text == "and"
            v2 = ctx.getChild(2).accept(self)
            if v1 is None and not v2 is None:
                v1 = ctx.getChild(0).accept(self)
            elif not v1 is None and v2 is None:
                v2 = ctx.getChild(2).accept(self)
            if v1 is None and v2 is None:
                return None
            return v1.intersection(v2)
        assert False

    # Visit a parse tree produced by filter_expressionParser#relExpr.
    def visitRelExpr(self, ctx:filter_expressionParser.RelExprContext):
        # -> "(" expr ")"
        if ctx.getChild(0).getSymbol().text == "(":
            return ctx.getChild(1).accept(self)
        # -> IDENTIFIER "op" literalExpr
        elif ctx.getChild(0).getSymbol().type == filter_expressionLexer.IDENTIFIER:
            attribute = ctx.getChild(0).getSymbol().text
            op = ctx.getChild(1).getSymbol().text
            value = ctx.getChild(2).accept(self)
            def _lift(x):
                if isinstance(value, int):
                    return int(x)
                if isinstance(value, float):
                    return float(x)
                if isinstance(value, bool):
                    return bool(x)
                if isinstance(value, str):
                    return str(x)
                assert False

            matches = {
                "=":  lambda x : _lift(x) == value,
                "!=": lambda x : _lift(x) != value,
                "<":  lambda x : _lift(x) < value,
                "<=": lambda x : _lift(x) <= value,
                ">":  lambda x : _lift(x) > value,
                ">=": lambda x : _lift(x) >= value,
                "matches": lambda x : re.match(value, x),
            }[op]
            retv = set()
            for i, row in enumerate(self.data):
                m = matches(row[attribute])
                if m:
                    retv.add(i)
            return retv
        assert False

    # Visit a parse tree produced by filter_expressionParser#literalExpr.
    def visitLiteralExpr(self, ctx:filter_expressionParser.LiteralExprContext):
        # -> INT_LIT
        if ctx.getChild(0).getSymbol().type == filter_expressionLexer.INT_LIT:
            return int(ctx.getChild(0).getSymbol().text)
        # -> FLOAT_LIT
        elif ctx.getChild(0).getSymbol().type == filter_expressionLexer.FLOAT_LIT:
            return float(ctx.getChild(0).getSymbol().text)
        # -> BOOL_LIT
        elif ctx.getChild(0).getSymbol().type == filter_expressionLexer.BOOL_LIT:
            return bool(ctx.getChild(0).getSymbol().text)
        # -> STRING_LIT
        elif ctx.getChild(0).getSymbol().type == filter_expressionLexer.STRING_LIT:
            return ctx.getChild(0).getSymbol().text[1:-1]
        # -> DATETIME_LIT
        elif ctx.getChild(0).getSymbol().type == filter_expressionLexer.DATETIME_LIT:
            # TODO
            pass
        assert False
