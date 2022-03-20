import antlr4
import argparse

def parse(expr):
    from py3.antlr_expressionLexer import antlr_expressionLexer
    from py3.antlr_expressionParser import antlr_expressionParser
    inputStream = antlr4.InputStream(expr)
    lexer = antlr_expressionLexer(inputStream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = antlr_expressionParser(stream)
    parser._errHandler = antlr4.error.ErrorStrategy.BailErrorStrategy()
    try:
        return parser.expr()
    except Exception as e:
        raise RuntimeError("Syntax error in attribute expression: " + str(e))

def evaluate(args):
    import evaluator
    visitor = evaluator.Visitor()
    ast = parse(args.expr)
    result = visitor.visit(ast)
    print(args.expr, "=", result)

def pretty(args):
    import pretty
    visitor = pretty.Visitor()
    ast = parse(args.expr)
    result = visitor.visit(ast)
    print(result)

def main():
    parser = argparse.ArgumentParser(prog="main", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands", help="valid subcommands")

    parser_evaluate = subparsers.add_parser("evaluate", help="evaluate an expression")
    parser_evaluate.add_argument("expr", help="the expression to evaluate")
    parser_evaluate.set_defaults(func=evaluate)

    parser_pretty = subparsers.add_parser("pretty", help="pretty print an expression")
    parser_pretty.add_argument("expr", help="the expression to print")
    parser_pretty.set_defaults(func=pretty)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
