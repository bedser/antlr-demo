# Generated from ./filter_expression.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5?\n\5\3\6\3")
        buf.write("\6\3\6\2\4\4\6\7\2\4\6\b\n\2\3\3\2\17\23\2F\2\f\3\2\2")
        buf.write("\2\4\17\3\2\2\2\6\32\3\2\2\2\b>\3\2\2\2\n@\3\2\2\2\f\r")
        buf.write("\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17\20\b\3\1\2\20\21")
        buf.write("\5\6\4\2\21\27\3\2\2\2\22\23\f\3\2\2\23\24\7\3\2\2\24")
        buf.write("\26\5\6\4\2\25\22\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\5\3\2\2\2\31\27\3\2\2\2\32\33\b\4\1")
        buf.write("\2\33\34\5\b\5\2\34\"\3\2\2\2\35\36\f\3\2\2\36\37\7\4")
        buf.write("\2\2\37!\5\b\5\2 \35\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3")
        buf.write("\2\2\2#\7\3\2\2\2$\"\3\2\2\2%&\7\5\2\2&\'\5\4\3\2\'(\7")
        buf.write("\6\2\2(?\3\2\2\2)*\7\16\2\2*+\7\7\2\2+?\5\n\6\2,-\7\16")
        buf.write("\2\2-.\7\b\2\2.?\5\n\6\2/\60\7\16\2\2\60\61\7\t\2\2\61")
        buf.write("?\5\n\6\2\62\63\7\16\2\2\63\64\7\n\2\2\64?\5\n\6\2\65")
        buf.write("\66\7\16\2\2\66\67\7\13\2\2\67?\5\n\6\289\7\16\2\29:\7")
        buf.write("\f\2\2:?\5\n\6\2;<\7\16\2\2<=\7\r\2\2=?\5\n\6\2>%\3\2")
        buf.write("\2\2>)\3\2\2\2>,\3\2\2\2>/\3\2\2\2>\62\3\2\2\2>\65\3\2")
        buf.write("\2\2>8\3\2\2\2>;\3\2\2\2?\t\3\2\2\2@A\t\2\2\2A\13\3\2")
        buf.write("\2\2\5\27\">")
        return buf.getvalue()


class filter_expressionParser ( Parser ):

    grammarFileName = "filter_expression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'or'", "'and'", "'('", "')'", "'='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'matches'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
                      "STRING_LIT", "DATETIME_LIT", "WS" ]

    RULE_file_ = 0
    RULE_expr = 1
    RULE_andExpr = 2
    RULE_relExpr = 3
    RULE_literalExpr = 4

    ruleNames =  [ "file_", "expr", "andExpr", "relExpr", "literalExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    IDENTIFIER=12
    INT_LIT=13
    FLOAT_LIT=14
    BOOL_LIT=15
    STRING_LIT=16
    DATETIME_LIT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(filter_expressionParser.ExprContext,0)


        def EOF(self):
            return self.getToken(filter_expressionParser.EOF, 0)

        def getRuleIndex(self):
            return filter_expressionParser.RULE_file_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_" ):
                return visitor.visitFile_(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = filter_expressionParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr(0)
            self.state = 11
            self.match(filter_expressionParser.EOF)
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

        def andExpr(self):
            return self.getTypedRuleContext(filter_expressionParser.AndExprContext,0)


        def expr(self):
            return self.getTypedRuleContext(filter_expressionParser.ExprContext,0)


        def getRuleIndex(self):
            return filter_expressionParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = filter_expressionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.andExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = filter_expressionParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 16
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 17
                    self.match(filter_expressionParser.T__0)
                    self.state = 18
                    self.andExpr(0) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relExpr(self):
            return self.getTypedRuleContext(filter_expressionParser.RelExprContext,0)


        def andExpr(self):
            return self.getTypedRuleContext(filter_expressionParser.AndExprContext,0)


        def getRuleIndex(self):
            return filter_expressionParser.RULE_andExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def andExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = filter_expressionParser.AndExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_andExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.relExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = filter_expressionParser.AndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpr)
                    self.state = 27
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 28
                    self.match(filter_expressionParser.T__1)
                    self.state = 29
                    self.relExpr() 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(filter_expressionParser.ExprContext,0)


        def IDENTIFIER(self):
            return self.getToken(filter_expressionParser.IDENTIFIER, 0)

        def literalExpr(self):
            return self.getTypedRuleContext(filter_expressionParser.LiteralExprContext,0)


        def getRuleIndex(self):
            return filter_expressionParser.RULE_relExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)




    def relExpr(self):

        localctx = filter_expressionParser.RelExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relExpr)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(filter_expressionParser.T__2)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(filter_expressionParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(filter_expressionParser.IDENTIFIER)
                self.state = 40
                self.match(filter_expressionParser.T__4)
                self.state = 41
                self.literalExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(filter_expressionParser.IDENTIFIER)
                self.state = 43
                self.match(filter_expressionParser.T__5)
                self.state = 44
                self.literalExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(filter_expressionParser.IDENTIFIER)
                self.state = 46
                self.match(filter_expressionParser.T__6)
                self.state = 47
                self.literalExpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(filter_expressionParser.IDENTIFIER)
                self.state = 49
                self.match(filter_expressionParser.T__7)
                self.state = 50
                self.literalExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.match(filter_expressionParser.IDENTIFIER)
                self.state = 52
                self.match(filter_expressionParser.T__8)
                self.state = 53
                self.literalExpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.match(filter_expressionParser.IDENTIFIER)
                self.state = 55
                self.match(filter_expressionParser.T__9)
                self.state = 56
                self.literalExpr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 57
                self.match(filter_expressionParser.IDENTIFIER)
                self.state = 58
                self.match(filter_expressionParser.T__10)
                self.state = 59
                self.literalExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(filter_expressionParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(filter_expressionParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(filter_expressionParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(filter_expressionParser.STRING_LIT, 0)

        def DATETIME_LIT(self):
            return self.getToken(filter_expressionParser.DATETIME_LIT, 0)

        def getRuleIndex(self):
            return filter_expressionParser.RULE_literalExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)




    def literalExpr(self):

        localctx = filter_expressionParser.LiteralExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << filter_expressionParser.INT_LIT) | (1 << filter_expressionParser.FLOAT_LIT) | (1 << filter_expressionParser.BOOL_LIT) | (1 << filter_expressionParser.STRING_LIT) | (1 << filter_expressionParser.DATETIME_LIT))) != 0)):
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
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.andExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def andExpr_sempred(self, localctx:AndExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




