import antlr4
import argparse

def parse(expr):
    from py3.filter_expressionLexer import filter_expressionLexer
    from py3.filter_expressionParser import filter_expressionParser
    inputStream = antlr4.InputStream(expr)
    lexer = filter_expressionLexer(inputStream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = filter_expressionParser(stream)
    parser._errHandler = antlr4.error.ErrorStrategy.BailErrorStrategy()
    try:
        return parser.expr()
    except Exception as e:
        raise RuntimeError("Syntax error in attribute expression: " + str(e))

def evaluate(args):
    import evaluator
    import csv
    with open(args.csv, "rt") as fin:
        rows = [row for row in csv.DictReader(fin)]

    visitor = evaluator.Visitor(rows)
    ast = parse(args.expr)
    result = visitor.visit(ast)

    for i, row in enumerate(rows):
        if i in result:
            print(",".join(row.values()))

def main():
    parser = argparse.ArgumentParser(prog="main", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(title="subcommands", description="valid subcommands", help="valid subcommands")

    parser_evaluate = subparsers.add_parser("evaluate", help="evaluate an expression")
    parser_evaluate.add_argument("csv", help="the csv file to filter")
    parser_evaluate.add_argument("expr", help="the expression to evaluate")
    parser_evaluate.set_defaults(func=evaluate)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
