# Generated from ./classic_expression.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("K\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\5\b)")
        buf.write("\n\b\3\b\5\b,\n\b\3\b\5\b/\n\b\3\b\3\b\3\b\5\b\64\n\b")
        buf.write("\5\b\66\n\b\3\t\6\t9\n\t\r\t\16\t:\3\n\3\n\5\n?\n\n\3")
        buf.write("\n\3\n\3\13\3\13\3\f\6\fF\n\f\r\f\16\fG\3\f\3\f\2\2\r")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\2\27\n\3\2")
        buf.write("\6\4\2GGgg\4\2--//\3\2\62;\5\2\13\f\17\17\"\"\2O\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2")
        buf.write("\5\33\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r")
        buf.write("#\3\2\2\2\17\65\3\2\2\2\218\3\2\2\2\23<\3\2\2\2\25B\3")
        buf.write("\2\2\2\27E\3\2\2\2\31\32\7-\2\2\32\4\3\2\2\2\33\34\7/")
        buf.write("\2\2\34\6\3\2\2\2\35\36\7,\2\2\36\b\3\2\2\2\37 \7\61\2")
        buf.write("\2 \n\3\2\2\2!\"\7*\2\2\"\f\3\2\2\2#$\7+\2\2$\16\3\2\2")
        buf.write("\2%(\5\21\t\2&\'\7\60\2\2\')\5\21\t\2(&\3\2\2\2()\3\2")
        buf.write("\2\2)+\3\2\2\2*,\5\23\n\2+*\3\2\2\2+,\3\2\2\2,\66\3\2")
        buf.write("\2\2-/\5\21\t\2.-\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61")
        buf.write("\7\60\2\2\61\63\5\21\t\2\62\64\5\23\n\2\63\62\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\66\3\2\2\2\65%\3\2\2\2\65.\3\2\2\2\66")
        buf.write("\20\3\2\2\2\679\5\25\13\28\67\3\2\2\29:\3\2\2\2:8\3\2")
        buf.write("\2\2:;\3\2\2\2;\22\3\2\2\2<>\t\2\2\2=?\t\3\2\2>=\3\2\2")
        buf.write("\2>?\3\2\2\2?@\3\2\2\2@A\5\21\t\2A\24\3\2\2\2BC\t\4\2")
        buf.write("\2C\26\3\2\2\2DF\t\5\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2")
        buf.write("GH\3\2\2\2HI\3\2\2\2IJ\b\f\2\2J\30\3\2\2\2\13\2(+.\63")
        buf.write("\65:>G\3\b\2\2")
        return buf.getvalue()


class classic_expressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NUMBER = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NUMBER", 
                  "DECIMALS", "EXPONENT", "DECIMAL_DIGIT", "WS" ]

    grammarFileName = "classic_expression.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


