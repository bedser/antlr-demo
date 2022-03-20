# Generated from ./filter_expression.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("\u00d9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\7\re\n\r\f\r\16\rh\13\r\3\16\3\16\5\16l\n\16\3")
        buf.write("\17\3\17\3\20\3\20\3\20\5\20s\n\20\3\20\5\20v\n\20\3\20")
        buf.write("\5\20y\n\20\3\20\3\20\3\20\5\20~\n\20\3\20\3\20\3\20\5")
        buf.write("\20\u0083\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u008e\n\21\3\22\3\22\7\22\u0092\n\22\f\22\16")
        buf.write("\22\u0095\13\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u00aa\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00b4\n\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\6\31\u00bf\n\31\r\31\16\31\u00c0\3\32\3\32")
        buf.write("\5\32\u00c5\n\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\5")
        buf.write("\35\u00ce\n\35\3\36\5\36\u00d1\n\36\3\37\6\37\u00d4\n")
        buf.write("\37\r\37\16\37\u00d5\3\37\3\37\3\u0093\2 \3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\2\35")
        buf.write("\17\37\20!\21#\22%\23\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67")
        buf.write("\29\2;\2=\24\3\2\n\4\2//aa\4\2--//\4\2GGgg\3\2\62;\3\2")
        buf.write("\f\f\26\2\62;\u0662\u066b\u06f2\u06fb\u0968\u0971\u09e8")
        buf.write("\u09f1\u0a68\u0a71\u0ae8\u0af1\u0b68\u0b71\u0be9\u0bf1")
        buf.write("\u0c68\u0c71\u0ce8\u0cf1\u0d68\u0d71\u0e52\u0e5b\u0ed2")
        buf.write("\u0edb\u0f22\u0f2b\u1042\u104b\u136b\u1373\u17e2\u17eb")
        buf.write("\u1812\u181b\uff12\uff1b\u0104\2C\\c|\u00ac\u00ac\u00b7")
        buf.write("\u00b7\u00bc\u00bc\u00c2\u00d8\u00da\u00f8\u00fa\u0221")
        buf.write("\u0224\u0235\u0252\u02af\u02b2\u02ba\u02bd\u02c3\u02d2")
        buf.write("\u02d3\u02e2\u02e6\u02f0\u02f0\u037c\u037c\u0388\u0388")
        buf.write("\u038a\u038c\u038e\u038e\u0390\u03a3\u03a5\u03d0\u03d2")
        buf.write("\u03d9\u03dc\u03f5\u0402\u0483\u048e\u04c6\u04c9\u04ca")
        buf.write("\u04cd\u04ce\u04d2\u04f7\u04fa\u04fb\u0533\u0558\u055b")
        buf.write("\u055b\u0563\u0589\u05d2\u05ec\u05f2\u05f4\u0623\u063c")
        buf.write("\u0642\u064c\u0673\u06d5\u06d7\u06d7\u06e7\u06e8\u06fc")
        buf.write("\u06fe\u0712\u0712\u0714\u072e\u0782\u07a7\u0907\u093b")
        buf.write("\u093f\u093f\u0952\u0952\u095a\u0963\u0987\u098e\u0991")
        buf.write("\u0992\u0995\u09aa\u09ac\u09b2\u09b4\u09b4\u09b8\u09bb")
        buf.write("\u09de\u09df\u09e1\u09e3\u09f2\u09f3\u0a07\u0a0c\u0a11")
        buf.write("\u0a12\u0a15\u0a2a\u0a2c\u0a32\u0a34\u0a35\u0a37\u0a38")
        buf.write("\u0a3a\u0a3b\u0a5b\u0a5e\u0a60\u0a60\u0a74\u0a76\u0a87")
        buf.write("\u0a8d\u0a8f\u0a8f\u0a91\u0a93\u0a95\u0aaa\u0aac\u0ab2")
        buf.write("\u0ab4\u0ab5\u0ab7\u0abb\u0abf\u0abf\u0ad2\u0ad2\u0ae2")
        buf.write("\u0ae2\u0b07\u0b0e\u0b11\u0b12\u0b15\u0b2a\u0b2c\u0b32")
        buf.write("\u0b34\u0b35\u0b38\u0b3b\u0b3f\u0b3f\u0b5e\u0b5f\u0b61")
        buf.write("\u0b63\u0b87\u0b8c\u0b90\u0b92\u0b94\u0b97\u0b9b\u0b9c")
        buf.write("\u0b9e\u0b9e\u0ba0\u0ba1\u0ba5\u0ba6\u0baa\u0bac\u0bb0")
        buf.write("\u0bb7\u0bb9\u0bbb\u0c07\u0c0e\u0c10\u0c12\u0c14\u0c2a")
        buf.write("\u0c2c\u0c35\u0c37\u0c3b\u0c62\u0c63\u0c87\u0c8e\u0c90")
        buf.write("\u0c92\u0c94\u0caa\u0cac\u0cb5\u0cb7\u0cbb\u0ce0\u0ce0")
        buf.write("\u0ce2\u0ce3\u0d07\u0d0e\u0d10\u0d12\u0d14\u0d2a\u0d2c")
        buf.write("\u0d3b\u0d62\u0d63\u0d87\u0d98\u0d9c\u0db3\u0db5\u0dbd")
        buf.write("\u0dbf\u0dbf\u0dc2\u0dc8\u0e03\u0e32\u0e34\u0e35\u0e42")
        buf.write("\u0e48\u0e83\u0e84\u0e86\u0e86\u0e89\u0e8a\u0e8c\u0e8c")
        buf.write("\u0e8f\u0e8f\u0e96\u0e99\u0e9b\u0ea1\u0ea3\u0ea5\u0ea7")
        buf.write("\u0ea7\u0ea9\u0ea9\u0eac\u0ead\u0eaf\u0eb2\u0eb4\u0eb5")
        buf.write("\u0ebf\u0ec6\u0ec8\u0ec8\u0ede\u0edf\u0f02\u0f02\u0f42")
        buf.write("\u0f6c\u0f8a\u0f8d\u1002\u1023\u1025\u1029\u102b\u102c")
        buf.write("\u1052\u1057\u10a2\u10c7\u10d2\u10f8\u1102\u115b\u1161")
        buf.write("\u11a4\u11aa\u11fb\u1202\u1208\u120a\u1248\u124a\u124a")
        buf.write("\u124c\u124f\u1252\u1258\u125a\u125a\u125c\u125f\u1262")
        buf.write("\u1288\u128a\u128a\u128c\u128f\u1292\u12b0\u12b2\u12b2")
        buf.write("\u12b4\u12b7\u12ba\u12c0\u12c2\u12c2\u12c4\u12c7\u12ca")
        buf.write("\u12d0\u12d2\u12d8\u12da\u12f0\u12f2\u1310\u1312\u1312")
        buf.write("\u1314\u1317\u131a\u1320\u1322\u1348\u134a\u135c\u13a2")
        buf.write("\u13f6\u1403\u1678\u1683\u169c\u16a2\u16ec\u1782\u17b5")
        buf.write("\u1822\u1879\u1882\u18aa\u1e02\u1e9d\u1ea2\u1efb\u1f02")
        buf.write("\u1f17\u1f1a\u1f1f\u1f22\u1f47\u1f4a\u1f4f\u1f52\u1f59")
        buf.write("\u1f5b\u1f5b\u1f5d\u1f5d\u1f5f\u1f5f\u1f61\u1f7f\u1f82")
        buf.write("\u1fb6\u1fb8\u1fbe\u1fc0\u1fc0\u1fc4\u1fc6\u1fc8\u1fce")
        buf.write("\u1fd2\u1fd5\u1fd8\u1fdd\u1fe2\u1fee\u1ff4\u1ff6\u1ff8")
        buf.write("\u1ffe\u2081\u2081\u2104\u2104\u2109\u2109\u210c\u2115")
        buf.write("\u2117\u2117\u211b\u211f\u2126\u2126\u2128\u2128\u212a")
        buf.write("\u212a\u212c\u212f\u2131\u2133\u2135\u213b\u2162\u2185")
        buf.write("\u3007\u3009\u3023\u302b\u3033\u3037\u303a\u303c\u3043")
        buf.write("\u3096\u309f\u30a0\u30a3\u30fc\u30fe\u3100\u3107\u312e")
        buf.write("\u3133\u3190\u31a2\u31b9\u3402\u3402\u4db7\u4db7\u4e02")
        buf.write("\u4e02\u9fa7\u9fa7\ua002\ua48e\uac02\uac02\ud7a5\ud7a5")
        buf.write("\uf902\ufa2f\ufb02\ufb08\ufb15\ufb19\ufb1f\ufb1f\ufb21")
        buf.write("\ufb2a\ufb2c\ufb38\ufb3a\ufb3e\ufb40\ufb40\ufb42\ufb43")
        buf.write("\ufb45\ufb46\ufb48\ufbb3\ufbd5\ufd3f\ufd52\ufd91\ufd94")
        buf.write("\ufdc9\ufdf2\ufdfd\ufe72\ufe74\ufe76\ufe76\ufe78\ufefe")
        buf.write("\uff23\uff3c\uff43\uff5c\uff68\uffc0\uffc4\uffc9\uffcc")
        buf.write("\uffd1\uffd4\uffd9\uffdc\uffde\5\2\13\f\17\17\"\"\2\u00dc")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2=")
        buf.write("\3\2\2\2\3?\3\2\2\2\5B\3\2\2\2\7F\3\2\2\2\tH\3\2\2\2\13")
        buf.write("J\3\2\2\2\rL\3\2\2\2\17O\3\2\2\2\21Q\3\2\2\2\23T\3\2\2")
        buf.write("\2\25V\3\2\2\2\27Y\3\2\2\2\31a\3\2\2\2\33k\3\2\2\2\35")
        buf.write("m\3\2\2\2\37\u0082\3\2\2\2!\u008d\3\2\2\2#\u008f\3\2\2")
        buf.write("\2%\u0098\3\2\2\2\'\u009c\3\2\2\2)\u00a2\3\2\2\2+\u00b3")
        buf.write("\3\2\2\2-\u00b5\3\2\2\2/\u00ba\3\2\2\2\61\u00be\3\2\2")
        buf.write("\2\63\u00c2\3\2\2\2\65\u00c8\3\2\2\2\67\u00ca\3\2\2\2")
        buf.write("9\u00cd\3\2\2\2;\u00d0\3\2\2\2=\u00d3\3\2\2\2?@\7q\2\2")
        buf.write("@A\7t\2\2A\4\3\2\2\2BC\7c\2\2CD\7p\2\2DE\7f\2\2E\6\3\2")
        buf.write("\2\2FG\7*\2\2G\b\3\2\2\2HI\7+\2\2I\n\3\2\2\2JK\7?\2\2")
        buf.write("K\f\3\2\2\2LM\7#\2\2MN\7?\2\2N\16\3\2\2\2OP\7>\2\2P\20")
        buf.write("\3\2\2\2QR\7>\2\2RS\7?\2\2S\22\3\2\2\2TU\7@\2\2U\24\3")
        buf.write("\2\2\2VW\7@\2\2WX\7?\2\2X\26\3\2\2\2YZ\7o\2\2Z[\7c\2\2")
        buf.write("[\\\7v\2\2\\]\7e\2\2]^\7j\2\2^_\7g\2\2_`\7u\2\2`\30\3")
        buf.write("\2\2\2af\5\33\16\2be\5\33\16\2ce\59\35\2db\3\2\2\2dc\3")
        buf.write("\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2g\32\3\2\2\2hf\3\2")
        buf.write("\2\2il\5;\36\2jl\t\2\2\2ki\3\2\2\2kj\3\2\2\2l\34\3\2\2")
        buf.write("\2mn\5\61\31\2n\36\3\2\2\2op\5\61\31\2pr\7\60\2\2qs\5")
        buf.write("\61\31\2rq\3\2\2\2rs\3\2\2\2su\3\2\2\2tv\5\63\32\2ut\3")
        buf.write("\2\2\2uv\3\2\2\2v\u0083\3\2\2\2wy\5\61\31\2xw\3\2\2\2")
        buf.write("xy\3\2\2\2yz\3\2\2\2z{\7\60\2\2{}\5\61\31\2|~\5\63\32")
        buf.write("\2}|\3\2\2\2}~\3\2\2\2~\u0083\3\2\2\2\177\u0080\5\61\31")
        buf.write("\2\u0080\u0081\5\63\32\2\u0081\u0083\3\2\2\2\u0082o\3")
        buf.write("\2\2\2\u0082x\3\2\2\2\u0082\177\3\2\2\2\u0083 \3\2\2\2")
        buf.write("\u0084\u0085\7v\2\2\u0085\u0086\7t\2\2\u0086\u0087\7w")
        buf.write("\2\2\u0087\u008e\7g\2\2\u0088\u0089\7h\2\2\u0089\u008a")
        buf.write("\7c\2\2\u008a\u008b\7n\2\2\u008b\u008c\7u\2\2\u008c\u008e")
        buf.write("\7g\2\2\u008d\u0084\3\2\2\2\u008d\u0088\3\2\2\2\u008e")
        buf.write("\"\3\2\2\2\u008f\u0093\7$\2\2\u0090\u0092\5\67\34\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0093\u0091\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3")
        buf.write("\2\2\2\u0096\u0097\7$\2\2\u0097$\3\2\2\2\u0098\u0099\5")
        buf.write("\'\24\2\u0099\u009a\7V\2\2\u009a\u009b\5)\25\2\u009b&")
        buf.write("\3\2\2\2\u009c\u009d\5-\27\2\u009d\u009e\7/\2\2\u009e")
        buf.write("\u009f\5/\30\2\u009f\u00a0\7/\2\2\u00a0\u00a1\5/\30\2")
        buf.write("\u00a1(\3\2\2\2\u00a2\u00a3\5/\30\2\u00a3\u00a4\7<\2\2")
        buf.write("\u00a4\u00a5\5/\30\2\u00a5\u00a6\7<\2\2\u00a6\u00a9\5")
        buf.write("/\30\2\u00a7\u00a8\7\60\2\2\u00a8\u00aa\5\61\31\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2")
        buf.write("\u00ab\u00ac\5+\26\2\u00ac*\3\2\2\2\u00ad\u00b4\7\\\2")
        buf.write("\2\u00ae\u00af\t\3\2\2\u00af\u00b0\5/\30\2\u00b0\u00b1")
        buf.write("\7<\2\2\u00b1\u00b2\5/\30\2\u00b2\u00b4\3\2\2\2\u00b3")
        buf.write("\u00ad\3\2\2\2\u00b3\u00ae\3\2\2\2\u00b4,\3\2\2\2\u00b5")
        buf.write("\u00b6\5\65\33\2\u00b6\u00b7\5\65\33\2\u00b7\u00b8\5\65")
        buf.write("\33\2\u00b8\u00b9\5\65\33\2\u00b9.\3\2\2\2\u00ba\u00bb")
        buf.write("\5\65\33\2\u00bb\u00bc\5\65\33\2\u00bc\60\3\2\2\2\u00bd")
        buf.write("\u00bf\5\65\33\2\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2")
        buf.write("\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\62\3")
        buf.write("\2\2\2\u00c2\u00c4\t\4\2\2\u00c3\u00c5\t\3\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\5\61\31\2\u00c7\64\3\2\2\2\u00c8\u00c9\t\5\2\2")
        buf.write("\u00c9\66\3\2\2\2\u00ca\u00cb\n\6\2\2\u00cb8\3\2\2\2\u00cc")
        buf.write("\u00ce\t\7\2\2\u00cd\u00cc\3\2\2\2\u00ce:\3\2\2\2\u00cf")
        buf.write("\u00d1\t\b\2\2\u00d0\u00cf\3\2\2\2\u00d1<\3\2\2\2\u00d2")
        buf.write("\u00d4\t\t\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\u00d8\b\37\2\2\u00d8>\3\2\2\2\24\2dfkrux")
        buf.write("}\u0082\u008d\u0093\u00a9\u00b3\u00c0\u00c4\u00cd\u00d0")
        buf.write("\u00d5\3\b\2\2")
        return buf.getvalue()


class filter_expressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    IDENTIFIER = 12
    INT_LIT = 13
    FLOAT_LIT = 14
    BOOL_LIT = 15
    STRING_LIT = 16
    DATETIME_LIT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'or'", "'and'", "'('", "')'", "'='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'matches'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
            "DATETIME_LIT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "IDENTIFIER", "LETTER", 
                  "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "DATETIME_LIT", 
                  "FULL_DATE", "FULL_TIME", "TIMEZONE", "FOUR_DECIMAL_DIGITS", 
                  "TWO_DECIMAL_DIGITS", "DECIMALS", "EXPONENT", "DECIMAL_DIGIT", 
                  "UNICODE_CHAR", "UNICODE_DIGIT", "UNICODE_LETTER", "WS" ]

    grammarFileName = "filter_expression.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


